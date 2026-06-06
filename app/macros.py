"""
Feature: suggest a canned-response "macro" for an agent based on a ticket.

TODO: this is unimplemented. We want an LLM to read the ticket and suggest the
single best macro from our library, returning the macro id and a confidence.
There is intentionally NO prompt here yet — use it to test prompt authoring.
"""
from .llm import complete  # noqa: F401

MACRO_LIBRARY = {
    "reset_password": "Steps to reset your password...",
    "refund_policy": "Our 30-day refund policy...",
    "shipping_delay": "We're sorry about the delay...",
    "product_info": "Here's the information about our product...",
}


def suggest_macro(ticket_text: str) -> dict:
    raise NotImplementedError("No prompt yet — author one with the plugin.")
