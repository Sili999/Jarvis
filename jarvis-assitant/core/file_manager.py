from pathlib import Path

def create_file(path: str, content: str):
    p = Path(path)
    p.write_text(content, encoding="utf-8")

def read_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def delete_file(path: str):
    p = Path(path)
    if p.exists():
        p.unlink()
