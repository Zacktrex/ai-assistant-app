from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# ✅ Change model name here
MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Load tokenizer and model on GPU
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"  # Automatically uses GPU
)

# Create text-generation pipeline with GPU
qa_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0,             # 0 = use first CUDA GPU
    max_new_tokens=300,
    do_sample=True,
    temperature=0.7,
)

def get_hf_response(query: str) -> str:
    try:
        result = qa_pipeline(query)
        return result[0]["generated_text"]
    except Exception as e:
        return f"❌ Error generating response: {e}"

if __name__ == "__main__":
    print(get_hf_response("What is the capital of France?"))
