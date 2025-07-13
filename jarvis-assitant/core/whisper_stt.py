import whisper

model = whisper.load_model("base")

def transcribe_audio(path: str) -> str:
    res = model.transcribe(path)
    return res["text"]
