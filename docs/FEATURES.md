# Acme Cloud — Support Desk Features

Acme Cloud is a B2B file-storage platform. The Support Desk automates first-line
triage for our support agents.

## Domain terms
- **Ticket**: a customer support request.
- **Queue**: where a ticket is routed (finance-queue, eng-queue, product-queue).
- **Macro**: a pre-written canned response an agent can insert.
- **Thread**: the full back-and-forth on a ticket.

## Current features
- Classify a ticket into a queue.
- Summarize a thread.
- Draft a customer reply.
- Detect ticket language.
- Answer common questions from the knowledge base.

## Planned (not yet built)
- **Macro suggestion**: given a ticket, suggest the single best macro from the
  library (`reset_password`, `refund_policy`, `shipping_delay`) and a confidence.
  The agent reviews the suggestion before sending. Output must be machine-usable
  (a macro id + confidence), since the UI highlights the suggested macro button.

## Notes
- We use OpenAI gpt-4o-mini today, but plan to trial a local Llama model for cost.
- Brand voice: concise, friendly, never over-promises.
