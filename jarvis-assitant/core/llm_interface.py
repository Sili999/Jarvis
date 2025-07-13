from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "Mistral-7B-v0.1-GGUF.Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=os.cpu_count()
)

def query_llm(prompt: str) -> str:
    resp = llm(prompt, max_tokens=512, temperature=0.7)
    return resp['choices'][0]['text'].strip()
