<a id="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Ollama Vision to Prompt for Forge Neo</h3>

  <p align="center">
    An extension for Forge Neo (and Automatic1111) that uses local Ollama vision-language models to generate prompts from images directly within the WebUI.
    <br />
    <a href="#usage"><strong>Explore the usage »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    &middot;
    <a href="#">Report Bug</a>
    &middot;
    <a href="#">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This extension provides a dedicated interface in **Forge Neo** to interact with **Ollama** vision models. It allows users to interrogate images locally and instantly transfer the generated descriptions to the main prompt fields.

### Key goals:

* **Direct WebUI Integration**: No need to switch between apps; interrogate images directly in txt2img or img2img.
* **Prompt Injection**: One-click transfer of generated text to the main Stable Diffusion prompt box.
* **Local & Private**: Everything runs on your machine via Ollama—no API keys or cloud tracking.
* **Customizable Workflow**: Use preset system prompts to tailor the output for SDXL, Anime, or Inpainting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Gradio](https://gradio.app/)
* [Forge Neo / Automatic1111](https://github.com/lllyasviel/stable-diffusion-webui-forge)
* [Ollama](https://ollama.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

* **Forge Neo** (or a compatible Stable Diffusion WebUI)
* **Ollama** installed and running
* A vision-capable model pulled (e.g., `ollama pull llava` or `ollama pull moondream`)

### Installation

1. Open your Forge Neo `extensions` folder.
2. Clone this repository:
   ```sh
   git clone https://github.com/JuanBerta/sd-webui-ollama-vl.git
   ```
3. Install requirements:
4. ``` sh
   pip install -r requirements.txt
   ```
5. Restart your Forge Neo WebUI.
6. The extension will appear as a new accordion labeled Ollama VL Prompt.

## Usage
* **Locate the Module**: Open the Ollama VL Prompt accordion in the txt2img or img2img tab.
* **Select Model & Preset**: Choose your desired Ollama model and a preset (e.g., SDXL, Anime).
* **Input Image**: Upload the image you want to describe to the Vision Input Image box.
* **Generate**: Click 🔍 Run Ollama Query. The AI's description will appear in the output textbox.
* **Transfer**: Click ➡️ Send to Main Prompt to automatically fill the main prompt field with the generated text.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Configuration
* Custom settings can be managed in the standard Settings tab under the Ollama VL Prompt section:
* Default Ollama Model: Set which model should be selected by default when the UI loads.
* Ollama Keep Alive: Configure how long the model stays in GPU memory (e.g., 5m for five minutes, 0m to unload immediately).
* If you change these settings, use the 🔄 Sync with Settings button inside the extension accordion to update the module without a full UI reload.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap
* [x] Automatic Ollama model detection
* [x] Persistent custom settings tab
* [x] One-click "Send to Main Prompt" functionality
* [x] JSON-based preset system prompts
* [x] UI Synchronization button
* [ ] Batch processing for multiple images
* [ ] Support for tag-based interrogation (Danbooru style)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing
* **Fork the project**
* **Create your feature branch** (git checkout -b feature/AmazingFeature)
* **Commit your changes**
* **Push to the branch**
* **Open a Pull Request**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License
* **Distributed under the MIT License.**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
* Juan – GitHub: https://github.com/JuanBerta
* Project Link: https://github.com/JuanBerta/sd-webui-ollama-vl

<p align="right">(<a href="#readme-top">back to top</a>)</p>
