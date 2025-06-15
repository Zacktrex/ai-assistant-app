def build_prompt(query: str, context: str = "", memory: list = None) -> str:
    prompt = "You are an expert assistant. Answer clearly, concisely, and in markdown or bullet points.\n\n"

    if context:
        prompt += f"Context:\n{context.strip()}\n\n"

    if memory:
        for turn in memory:
            prompt += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

    prompt += f"User: {query.strip()}\nAssistant:"
    return prompt
