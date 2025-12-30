import os
import json
import gradio as gr
from modules import scripts, shared, script_callbacks
from ollama import chat
from scripts.utils import pil_to_base64, get_local_models

# Path setup
RESOURCES_PATH = os.path.dirname(os.path.realpath(__file__))
PRESETS_FILE = os.path.join(RESOURCES_PATH, "presets.json")

def load_presets():
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {"Default": "Describe this image."}

# --- SETTINGS REGISTRATION ---
def on_ui_settings():
    section = ("ollama_vl", "Ollama VL Prompt")
    
    options = {
        "ollama_keep_alive": shared.OptionInfo(
            "5m", "Ollama Keep Alive (e.g., 5m, 10m, 0m)", section=section
        ),
        "ollama_default_model": shared.OptionInfo(
            "", "Default Ollama Model", gr.Dropdown, 
            lambda: {"choices": get_local_models()}, section=section
        ),
    }

    for k, v in options.items():
        shared.opts.add_option(k, v)

script_callbacks.on_ui_settings(on_ui_settings)

class OllamaForgeScript(scripts.Script):
    def __init__(self):
        super().__init__()
        self.main_prompt_box = None

    def title(self):
        return "Ollama Vision to Prompt"

    def show(self, is_img2img):
        return scripts.AlwaysVisible
    
    def after_component(self, component, **kwargs):
        if kwargs.get("elem_id") == "txt2img_prompt" or kwargs.get("elem_id") == "img2img_prompt":
            self.main_prompt_box = component

    def ui(self, is_img2img):
        presets = load_presets()
        saved_keep_alive = shared.opts.data.get("ollama_keep_alive", "5m")
        saved_model = shared.opts.data.get("ollama_default_model", "")
        models = get_local_models()

        with gr.Accordion("Ollama VL Prompt", open=False):
            with gr.Row():
                model = gr.Dropdown(
                    label="Model", 
                    choices=models, 
                    value=saved_model if saved_model in models else (models[0] if models else ""),
                    interactive=True
                )
                preset = gr.Dropdown(label="Preset", choices=list(presets.keys()), value="SDXL", interactive=True)
            
            user_hint = gr.Textbox(label="User Hint", lines=1)
            input_image = gr.Image(label="Vision Input Image", type="pil")
            keep_alive_local = gr.Textbox(label="Keep Alive", value=str(saved_keep_alive), interactive=True)
            output_text = gr.Textbox(label="Generated Prompt Output", lines=4, show_copy_button=True)
            
            with gr.Row():
                send_query_btn = gr.Button("🔍 Run Ollama Query", variant="primary")
                send_to_main_btn = gr.Button("➡️ Send to Main Prompt")

            refresh_settings_btn = gr.Button("🔄 Sync with Settings", variant="secondary")

            def sync_settings():
                new_model = shared.opts.data.get("ollama_default_model", "")
                new_ka = shared.opts.data.get("ollama_keep_alive", "5m")
                return gr.update(value=new_model), gr.update(value=new_ka)

            refresh_settings_btn.click(
                fn=sync_settings,
                inputs=[],
                outputs=[model, keep_alive_local]
            )

            send_query_btn.click(
                fn=self.run_ollama_query,
                inputs=[model, preset, user_hint, input_image, keep_alive_local],
                outputs=[output_text]
            )

            send_to_main_btn.click(
                fn=lambda x: x,
                inputs=[output_text],
                outputs=[self.main_prompt_box]
            )

        return [model, preset, user_hint, input_image, keep_alive_local]

    def run_ollama_query(self, model, preset, user_hint, input_image, keep_alive):
        if input_image is None: 
            return "Error: Image missing."

        img_b64 = pil_to_base64(input_image)
        presets = load_presets()
        prompt_base = presets.get(preset, "Describe this image.")
        
        if user_hint.strip():
            prompt_base += "\nAdditional instruction: " + user_hint.strip()
        
        try:
            response = chat(
                model=model,
                messages=[{"role": "user", "content": prompt_base, "images": [img_b64]}],
                keep_alive=keep_alive,
            )
            results = response.message.content.replace("\n", ", ").strip()
            return results
        except Exception as e:
            return f"Ollama Error: {str(e)}"