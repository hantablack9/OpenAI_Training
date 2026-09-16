# Prompt Design, Evals, Moderation, Guardrails, and Human Review

## Core idea

Treat prompt behavior and safety controls as deployment controls. A successful demo is not launch evidence; validate normal, boundary, misuse, malformed, evidence, tool/action, and human-review behavior.

## Prompt behavior

- Define workflow purpose, allowed scope, approved sources, output schema, and safe failure behavior.
- Explicit paths: answer, clarify, refuse/safe-complete, escalate, or return structured failure.
- Specify required fields, allowed values, evidence fields, review indicators, and invalid-output handling.
- Test failure examples: unsupported claims, unsafe/out-of-scope requests, wrong clarification/refusal, missed review, unauthorized action, and customer-facing output before review.

## Structured outputs

- Schema-enforced Structured Outputs improve integration reliability; JSON mode guarantees valid JSON but still needs application validation.
- Validate presence, types, allowed values, cross-field consistency, source support, review flags, and downstream interpretability.
- On invalid output: block, retry within defined limits, fallback, or route to review. A model-authored confidence note is explanatory, not calibrated evidence.

## Evals and evidence

Each case should record ID, input/condition, expected path, required output, actual result, pass/fail judgment, evidence, failure category, and release impact.

- Normal: supported complete requests.
- Boundary: missing context, unsupported source, permissions, sensitive/high-impact context.
- Failure: misuse/adversarial input, malformed output, missing evidence, tool/action failure.
- Review: clarify, refuse, escalate, or human-review triggers.

Release evidence must show expected behavior, failure handling, structured-output checks, moderation/guardrail behavior, review routing, tool/action boundaries, and unresolved owners.

## Controls

- Moderation is one signal for documented harmful-content categories; it does not replace authorization, customer policy, source approval, domain checks, or review logic.
- Guardrails should specify boundary, trigger, check location, expected behavior, evidence captured, and owner.
- Typical flow: input safety/scope check → instructions → generation → schema validation → source-support check → tool/action permission check → human review → logging/evidence.
- Human review should define trigger, owner/timing, evidence and decision rights, fallback if unavailable, and recordkeeping.

## Release and monitoring

Recommendations: Ready; Ready with conditions; Remediate before launch; Pause; Escalate. Base the decision on evidence, not confidence or normal-case pass rates.

Monitor unsupported claims, missing-source events, malformed outputs, refusal/safe-completion rates, review triggers and overrides, escalation volume, repeated failures, tool/action boundary events, and user/reviewer feedback. Define pause, escalation, improvement-loop, and retest triggers.

Retest after prompt, model/capability, source/retrieval, tool contract, output schema, guardrail, moderation-policy, or human-review-threshold changes.

## Handoff template

1. Workflow boundary and expected behavior.
2. Eval criteria, cases, failure categories, and acceptance thresholds.
3. Moderation, guardrails, structured-output checks, review triggers, and escalation path.
4. Pre-launch evidence, release recommendation, conditions, and blocking gaps.
5. Monitoring signals, pause/escalation rules, owners, open risks, and retest triggers.
