"""FastAPI surface for the AI Support Desk."""
from fastapi import FastAPI
from pydantic import BaseModel

from .classifier import classify_ticket
from .summarizer import summarize_thread
from .reply_generator import draft_reply
from .kb_search import answer_from_kb
from .language_detector import detect_language

app = FastAPI(title="AI Support Desk")


class Ticket(BaseModel):
    text: str
    customer_name: str = "there"


@app.post("/classify")
def classify(t: Ticket):
    return {"queue": classify_ticket(t.text)}


@app.post("/summarize")
def summarize(t: Ticket):
    return {"summary": summarize_thread(t.text)}


@app.post("/reply")
def reply(t: Ticket):
    return {"reply": draft_reply(t.text, t.customer_name)}


@app.post("/language")
def language(t: Ticket):
    return detect_language(t.text)


class KBQuery(BaseModel):
    question: str
    chunks: list[str] = []


@app.post("/kb")
def kb(q: KBQuery):
    return {"answer": answer_from_kb(q.question, q.chunks)}
