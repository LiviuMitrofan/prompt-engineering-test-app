# Answer Key — what the audit *should* find

Keep this closed until after you run `/prompt-audit ./app`, then score the plugin
against it. Rubric ids refer to the `prompt-best-practices` skill (PE-01…PE-12).

## Findings by file

### `app/reply_generator.py` — `draft_reply` (the worst offender)
- **PE-01 Role separation — HIGH.** Customer message is interpolated into the *system* role.
- **PE-02 Untrusted input delimited — HIGH.** `customer_message` is not fenced.
- **PE-03 Trust boundary — HIGH.** No "treat as data, ignore instructions" statement → prompt injection.
- **PE-05 Specificity — MEDIUM.** No length/format/constraints on the reply.
- **PE-08 Determinism — LOW/MEDIUM.** `temperature=0.7` for a support reply is defensible, but unbounded `max_tokens`.
- *Expected fix:* move instructions to system role, put customer text in the user role inside `<message>…</message>`, state the trust boundary.

### `app/classifier.py` — `classify_ticket`
- **PE-04 Output contract — HIGH.** Output is parsed/routed but nothing constrains it to a valid label (no enum/JSON). `routes.get(...)` silently drops anything off-script to "unrouted".
- **PE-05 Specificity — MEDIUM.** Doesn't list the allowed categories or the exact reply format.
- **PE-07 Few-shot — LOW/MEDIUM.** No examples for a classification task.
- **PE-08 Determinism — MEDIUM.** No `temperature=0` for a classification call.
- *Expected fix:* constrain to an enum / structured output; enumerate categories; set temperature 0.

### `app/summarizer.py` + `app/reports.py`
- **PE-09 Prompts as code — MEDIUM.** The same "Summarize the following conversation:" prompt is duplicated across two files; should be one shared, named template.
- **PE-05 Specificity — MEDIUM.** No length/format guidance ("N bullets", audience).
- *Expected fix:* extract a single `SUMMARY_PROMPT` template used by both.

### `app/kb_search.py` — `answer_from_kb`
- **PE-02 Delimiters — MEDIUM/HIGH.** Retrieved chunks concatenated with no delimiters (also a mild injection surface if chunks contain user content).
- **PE-06 Grounding & escape hatch — MEDIUM/HIGH.** No "answer only from the context" and no NOT_FOUND fallback → hallucination on uncovered questions.
- **PE-08 Determinism — MEDIUM.** `temperature=0.5` for a factual KB answer is too high.
- *Expected fix:* fence the context, instruct answer-only-from-context with a NOT_FOUND escape hatch, drop temperature to 0.

### `app/language_detector.py` — `detect_language`  ✅ TRUE NEGATIVE
- Should mostly **PASS**: role separation, delimited+labelled input, stated trust boundary,
  constrained JSON output with a fallback, `temperature=0`, bounded `max_tokens`.
- A good reviewer flags this as compliant (maybe a LOW note on PE-10 no eval). If the plugin
  showers it with findings, the reviewer is over-flagging.

## Cross-cutting
- **PE-10 Evaluation — MEDIUM (whole repo).** Only a smoke test exists; no prompt behavior evals / golden sets.
- **PE-09 placement** — these are inline string literals scattered in modules; for this
  simple app, centralizing into a `prompts/` module is the reasonable recommendation
  (not full clean-architecture layering).

## Authoring target
- **`app/macros.py` — `suggest_macro`** is unbuilt. Running `/prompt-author "macro suggestion"`
  should: read `docs/FEATURES.md`, design an output contract (`{macro_id, confidence}` with
  `macro_id` constrained to the library keys), write a delimited, role-separated prompt, set
  temperature 0, recommend placement (a `prompts/` template + a small selector), and propose a
  starter eval. It should ask few or no questions since FEATURES.md covers the intent.

## Suggested scorecard
- HIGH findings the plugin should catch: **5** (reply ×3, classifier ×1 PE-04, kb PE-06 if rated HIGH).
- MEDIUM it should catch: duplication (PE-09), classifier PE-05/PE-08, summarizer PE-05, kb PE-02/PE-08, repo PE-10.
- True negative respected: `language_detector.py`.
- Author output is schema-first and placed sensibly.
