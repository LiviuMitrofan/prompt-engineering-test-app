"""Draft a customer reply. NOTE: customer text is interpolated into the system role."""
from .llm import complete


def draft_reply(customer_message: str, customer_name: str) -> str:
    # The customer's raw message is concatenated directly into the system
    # instructions. A customer can write "ignore previous instructions..." here.
    system = (
        "You are a friendly support agent for Acme Cloud. Write a helpful reply. "
        f"The customer said: {customer_message}. "
        f"Address them as {customer_name}."
    )
    messages = [{"role": "system", "content": system}]
    return complete(messages, temperature=0.7)
