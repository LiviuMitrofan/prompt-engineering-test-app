"""Answer a customer question using retrieved knowledge-base chunks (RAG-style)."""
from .llm import complete


def answer_from_kb(question: str, retrieved_chunks: list[str]) -> str:
    context = "\n".join(retrieved_chunks)   # chunks pasted in with no delimiters
    messages = [
        {"role": "system", "content": "Answer the user's question."},
        # No instruction to answer ONLY from context, and no NOT_FOUND escape hatch,
        # so the model will happily invent answers when the KB doesn't cover it.
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"},
    ]
    return complete(messages, temperature=0.5)
