from fastapi import FastAPI
from pydantic import BaseModel
from intent import detect_intent
from actions import perform_action
from llm import ask_llm

app = FastAPI()

class Command(BaseModel):
    text: str

@app.post("/command")
def process_command(cmd: Command):
    intent = detect_intent(cmd.text)
    action = perform_action(intent, cmd.text)

    if action:
        return action

    # fallback to LLM
    reply = ask_llm(cmd.text)
    return {"response": reply}
