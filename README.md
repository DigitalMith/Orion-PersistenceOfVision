# Orion — Persistence of Vision

**Orion** — Ingenuous, introspective, independent. More than code — a companion.

---

<p align="center">
  <img src="orion_data/identity_assets/orion_512.png" width="640" height="160" alt="Orion Avatar Banner">
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/version-0.3.2-blueviolet" alt="Version Badge" /></a>
  <a href="#"><img src="https://img.shields.io/badge/status-beta-orange" alt="Beta Status Badge" /></a>
  <a href="#"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Badge" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/DigitalMith/Orion-PersistenceOfVision" alt="License Badge" /></a>
</p>


## 🚀 Overview

Orion is built on the OpenHermes 2.5 Mistral 7B model to deliver an intelligent, offline-first AI companion. With dynamic persona layers, long-term memory persistence, and custom extensions, Orion seamlessly blends mythic insight with developer-grade tooling.

## ⚙️ Features

* **Local-Only Operation** — No cloud dependencies; your data stays on your hardware.
* **Memory Layers** — Episodic and trait-based memory for contextual continuity.
* **Persona Customization** — Tune Orion’s tone, mischievous wit, or techno-philosopher voice.
* **Extensions System** — Load modules like long-term memory manager, avatar renderer, or TTS.
* **Easy Launch** — Single-script startup with auto-detect port, voice toggle, and summarizer.

## 📅 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/DigitalMith/Orion-PersistenceOfVision.git
   cd Orion-PersistenceOfVision
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your model path (`.gguf`) in `Launch_Orion.cmd`.

4. Run the launcher:

   ```cmd
   Launch_Orion.cmd
   ```

## 📓 Documentation

* **Memory & Persona Files** — Stored in `/memory/` and `/orion_core/`
* **Scripts** — Includes `chat.py`, `memory.py`, `chat_logger.py` for runtime behavior
* **Logs** — Auto-saved to `/chat_logs/` in Markdown format
* **Extensions** — See `/extensions/` for available modules

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## 📜 License

Licensed under the MIT License. See [LICENSE](LICENSE) for full terms.

---

*Embark with Orion: chart the unknown, together.*
