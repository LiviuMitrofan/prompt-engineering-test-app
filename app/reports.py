"""Generate a daily report. Re-implements the same summarize prompt (duplication)."""
from .llm import complete


def summarize_for_report(thread_text: str) -> str:
    # Near-identical prompt to summarizer.SUMMARY_PROMPT — should be a shared template.
    messages = [
        {"role": "user", "content": "Summarize the following conversation: " + thread_text},
    ]
    return complete(messages)
