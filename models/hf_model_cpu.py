from transformers import pipeline

MODEL_NAME = "tiiuae/falcon-7b-instruct"

try:
    hf_pipeline = pipeline(
        "text-generation",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
        device_map="auto",
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True
    )
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model '{MODEL_NAME}': {e}")

def get_hf_response(prompt: str) -> str:
    try:
        result = hf_pipeline(prompt)
        raw = result[0]["generated_text"]
        return raw[len(prompt):].strip() if raw.startswith(prompt) else raw
    except Exception as e:
        return f"❌ Error generating response: {e}"
