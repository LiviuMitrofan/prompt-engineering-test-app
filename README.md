# AI Support Desk (mock project)

A deliberately uneven FastAPI app for testing the **prompt-engineering-suite** plugin.
Some prompts follow best practices; several do not. One feature has no prompt at all.

This repo is a TEST FIXTURE. The flaws are intentional. See `ANSWER_KEY.md` (keep it
closed until after you run the plugin) for what the audit *should* find.

## Run the suite against it
```
/prompt-audit ./app
/prompt-author "macro suggestion"        # the unbuilt feature in app/macros.py
/prompt-fix app/reply_generator.py
```

## Layout
- `app/classifier.py` — ticket classification
- `app/summarizer.py` / `app/reports.py` — thread summarization
- `app/reply_generator.py` — drafts customer replies
- `app/kb_search.py` — knowledge-base Q&A (RAG-style)
- `app/language_detector.py` — language detection
- `app/macros.py` — macro suggestion (UNBUILT — for prompt authoring)
- `docs/FEATURES.md` — product context for the author agent

## Install deps (optional, to actually run it)
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Runs without an API key using a stub client, so the plugin can read it statically.
