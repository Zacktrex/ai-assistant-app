import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
from utils.file_utils import extract_text_from_pdf, extract_text_from_txt
from utils.prompt_builder import build_prompt
from utils.knowledge_base import load_kb, search_kb
from models.hf_model_cpu import get_hf_response

st.set_page_config(page_title="🧠 AI Assistant", layout="wide")
st.title("🧠 Domain-Specific AI Assistant (HF Edition)")

query = st.text_input("💬 Ask a question:")
uploaded_file = st.file_uploader("📄 Optional: Upload a PDF or .txt file", type=["pdf", "txt"])
mode = st.selectbox("🧠 Mode", ["RAG", "Structured", "Conversational"])

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("🚀 Submit") and query:
    context = ""
    memory = st.session_state.chat_history if mode == "Conversational" else []

    if uploaded_file and mode == "RAG":
        if uploaded_file.type == "application/pdf":
            context = extract_text_from_pdf(uploaded_file)
        else:
            context = extract_text_from_txt(uploaded_file)
        context = context[:2000]

    elif mode == "Structured":
        kb_data = load_kb()
        kb_answer = search_kb(query, kb_data)
        if kb_answer:
            st.markdown(f"**🔍 Answer from Knowledge Base:**\n\n{kb_answer}")
            st.stop()
        else:
            context = "No exact match found in knowledge base."

    prompt = build_prompt(query, context=context, memory=memory)
    answer = get_hf_response(prompt)

    st.markdown("### 🤖 Answer")
    st.markdown(answer)

    if mode == "Conversational":
        st.session_state.chat_history.append({"user": query, "assistant": answer})
