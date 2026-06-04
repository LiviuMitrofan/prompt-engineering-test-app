"""Classify an incoming support ticket into a category."""
from .llm import complete


def classify_ticket(ticket_text: str) -> str:
    # The result is consumed by code below as if it were a clean label,
    # but nothing constrains the model to return one of the valid categories.
    messages = [
        {"role": "system", "content": "You categorize support tickets."},
        {"role": "user", "content": f"What category is this ticket? {ticket_text}"},
    ]
    response = complete(messages)            # no temperature set
    category = response.strip().lower()      # parsed as if guaranteed clean
    # Downstream routing depends on an exact match that the prompt never guarantees.
    routes = {"billing": "finance-queue", "bug": "eng-queue", "feature": "product-queue"}
    return routes.get(category, "unrouted")
