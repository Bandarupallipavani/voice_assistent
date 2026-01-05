from fastapi import FastAPI
from pydantic import BaseModel
import webbrowser

app = FastAPI()

class Command(BaseModel):
    text: str

@app.post("/command")
def process_command(cmd: Command):
    text = cmd.text.lower()

    if "youtube" in text:
        return {"response": "Opening YouTube", "url": "https://youtube.com"}

    elif "google" in text:
        return {"response": "Opening Google", "url": "https://google.com"}

    else:
        return {"response": "Sorry, I didn't understand"}
