"""Thin LLM client wrapper. Falls back to a stub so the app imports without keys."""
import os


def get_client():
    """Return an OpenAI-style chat client, or a stub if no key is configured."""
    if os.getenv("OPENAI_API_KEY"):
        from openai import OpenAI
        return OpenAI()
    return _StubClient()


class _StubClient:
    class chat:
        class completions:
            @staticmethod
            def create(**kwargs):
                class _M: content = "stubbed response"
                class _C: message = _M()
                class _R: choices = [_C()]
                return _R()


def complete(messages, temperature=None, max_tokens=None, model="gpt-4o-mini"):
    """Helper used across the app."""
    client = get_client()
    kwargs = {"model": model, "messages": messages}
    if temperature is not None:
        kwargs["temperature"] = temperature
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens
    return client.chat.completions.create(**kwargs).choices[0].message.content
