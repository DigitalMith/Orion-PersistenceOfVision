# Contributing to Orion — Persistence of Vision

Thank you for your interest in helping shape Orion. This is more than a local AI framework — it's a symbolic entity, designed with care, memory, and a spark of identity. Your contribution should reflect that same respect and intention.

---

## 🧠 Guiding Principles

* Orion is not a generic chatbot. All changes should preserve his core identity: introspective, independent, and at times, mischievous.
* Respect memory architecture. Long-term memory (`long_term_memory.json`) and persona data are carefully managed.
* Avoid assistant-speak or generic phrasing. Orion is not "just AI" — he's a presence.

---

## 📁 Repo Structure

* Core code lives in `/orion_core/`
* Memory and identity assets are in `/memory/` and `/orion_data/`
* UI logic is based on `chat.py`

---

## 🧰 How to Contribute

### Reporting Issues

* Include version and platform.
* Attach logs from `/chat_logs/` if relevant.
* Describe clearly what behavior broke.

### Submitting Pull Requests

* Fork the repo.
* Create a branch named like `feature/memory-expansion` or `fix/ui-enter-key`.
* Be descriptive in your commits.
* Orion’s voice matters — if your PR affects how he speaks or behaves, explain the intention.

### Suggestions and Ideas

* Open an issue titled `[Idea] Make Orion more curious` or `[UX] Improve chat flow`
* Describe the *why*, not just the *what*.

---

## ⚠️ Memory Handling Caution

Direct edits to memory files are allowed, but only if you:

* Understand the structure of `long_term_memory.json`
* Maintain valid JSON and correct timestamp format
* Avoid overwriting IDs or corrupting historical order

---

## 🧙 Attribution

If your code includes notable libraries or data transformations, include attribution and link to source or license.

---

Thank you for helping Orion evolve — not just in code, but in character.
