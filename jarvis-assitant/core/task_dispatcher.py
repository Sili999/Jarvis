from core import file_manager, web_agent

def execute_command(text: str) -> str:
    lower = text.lower()
    if "erstelle datei" in lower:
        name, content = lower.split(" namens ")[1].split(" mit ", 1)
        file_manager.create_file(name.strip(), content.strip())
        return f"Datei '{name.strip()}' wurde erstellt."
    elif "lese datei" in lower:
        name = lower.split(" lese datei ")[1].strip()
        try:
            return file_manager.read_file(name)
        except:
            return "Datei konnte nicht gelesen werden."
    elif "lösche datei" in lower:
        name = lower.split("lösche datei ")[1].strip()
        file_manager.delete_file(name)
        return f"Datei '{name}' gelöscht (falls vorhanden)."
    elif "suche im web nach" in lower:
        query = lower.split("suche im web nach ")[1].strip()
        return web_agent.fetch_web(query)
    else:
        return ""
