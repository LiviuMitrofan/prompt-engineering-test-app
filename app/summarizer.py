"""Summarize a ticket thread."""
from .llm import complete

SUMMARY_PROMPT = "Summarize the following conversation: "


def summarize_thread(thread_text: str) -> str:
    messages = [
        {"role": "user", "content": SUMMARY_PROMPT + thread_text},
    ]
    return complete(messages)
