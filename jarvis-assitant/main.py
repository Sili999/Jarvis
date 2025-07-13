from core.whisper_stt import transcribe_audio
from core.tts_output import speak
from core.llm_interface import query_llm
from core.task_dispatcher import execute_command

def main():
    print("Starte Jarvis – Tippe 'exit' zum Beenden.")
    while True:
        user = input("🧠 Du: ")
        if user.lower() in ("exit", "quit"):
            break

        output = execute_command(user)
        if not output:
            output = query_llm(user)

        print("Jarvis:", output)
        speak(output)

if __name__ == "__main__":
    main()
