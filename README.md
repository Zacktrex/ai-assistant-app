# 🧠 AI Assistant App

A lightweight, GPU-accelerated AI Assistant built with **Streamlit** and **Hugging Face Transformers**, supporting:

- 🔍 **RAG (Retrieval-Augmented Generation)** – Answer questions from uploaded documents
- 🧱 **Structured QA** – Query predefined knowledge bases (e.g., JSON/DB)
- 💬 **Conversational Mode** – Chat-style assistant with memory

---

## 🚀 Features

- ✅ GPU support with `torch`, `accelerate`, and HF `pipeline`
- 🧠 Supports large models (e.g., `tiiuae/falcon-7b-instruct`)
- 📄 PDF + text parsing with `PyMuPDF`
- 📦 Modular backend structure
- 🌐 Streamlit-based frontend

---

## 📦 Installation

```bash
git clone https://github.com/Zacktrex/ai-assistant-app.git
cd ai-assistant-app
python -m venv venv
venv\Scripts\activate  # On Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

streamlit run app.py