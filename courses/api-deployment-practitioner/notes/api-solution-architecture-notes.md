# API Solution Architecture — concise notes

Course status snapshot: PartnerU recorded this module as complete. Re-check the live dashboard if completion status matters.

## Core idea

Architecture starts with the customer workflow and constraints—not with a model, API capability, or fashionable pattern. Produce a clear, bounded, review-ready brief before implementation.

## In plain English

Before anyone writes code, make sure everyone agrees on the job, the people and systems involved, and what “good” looks like. A simple model call may be enough; retrieval, tools, or agents are justified only when the workflow genuinely needs them.

## Recommended flow

1. **Customer problem and outcome** — state the specific workflow problem, desired improvement, users, and business value.
2. **Solution boundary** — separate what is in scope, out of scope, human-owned, and not yet decided.
3. **Customer constraints** — capture vertical context, policy/security/privacy/compliance, existing systems, latency/reliability/fallback, source freshness, throughput, logging/retention, permissions, support ownership, and review/approval expectations.
4. **Integration map** — identify: caller/workflow; systems and data sources; output channel; downstream dependencies; approval or handoff point.
5. **Minimum useful pattern** — choose the simplest pattern that responsibly supports the workflow.
6. **Readiness assumptions** — make governance, evaluation, observability, and production-readiness questions explicit.
7. **Brief and handoff** — summarize decisions, assumptions, risks, and the next validation step.

## Pattern cheat sheet

| Pattern | Use when | Main decisions / cautions |
|---|---|---|
| Simple model call | Request contains all context; generation, summarization, transformation, classification, or reasoning is enough | Prompt/request shape, response handling, basic errors |
| Structured output | A reviewer or downstream system needs predictable fields, status, evidence, or review flags | Schema, validation, malformed-output handling |
| Retrieval-grounded | Approved, current, permission-aware internal sources are needed at runtime | Source ownership, permissions, freshness, retrieval failure |
| Tool/action | Live status, calculations, record creation/update, or another system action is required | Tool contract, access boundary, approval gate, audit event |
| Agentic workflow | Multi-step coordination across tools/systems, state, approvals, escalation, and monitoring are genuinely required | State, sequencing, monitoring, rollback/handoff; avoid premature use |
| Realtime/multimodal | Voice, audio, image, low-latency interaction, or accessibility needs drive the workflow | Latency, consent, media quality/privacy, fallback, retention |
| Hybrid | One pattern alone is insufficient and each added capability has a clear reason | Coordination and compounded failure modes |

**Rule:** add complexity only when the workflow requires it and the added value justifies the extra validation and operational risk.

## Pattern-rationale template

> We recommend **[pattern]** because **[workflow need]**. This enables **[specific capability]**. It does not solve **[limitation/open issue]**. Before build, validate **[next question]**.

## Architecture decision points

- What is the simplest viable pattern?
- Where does model interaction occur, and where does business context enter?
- Is approved runtime retrieval required?
- Are tools/actions needed, and where are their boundaries?
- Where must a human review or approve?
- What must be observable after release?
- Which sources, permissions, schema, retention, compliance, and production assumptions could change the design?

## Readiness checklist

- **Governance:** what data/systems can be accessed, who owns them, who approves actions, and who reviews outputs?
- **Evaluation:** expected behavior, acceptable/unacceptable outputs, missing/conflicting-context behavior, and escalation triggers.
- **Observability:** request/output status, actor, context/source availability, retrieval/tool status, review flags, errors, latency, feedback, and escalations.
- **Production readiness:** review owner, fallback for missing context or dependency failure, logging rules, support owner, and evidence required before broader exposure.

## Brief template (decision-ready)

1. Customer problem and business outcome
2. Workflow moment and actor
3. Vertical/customer constraints
4. Solution boundary (in scope / out of scope / not yet decided)
5. Integration needs (caller, inputs, sources, output channel, review point)
6. Application pattern and rationale
7. Architecture decision points
8. Context/data assumptions
9. Model/capability requirements for later handoff (no premature model selection)
10. Tool/action assumptions
11. Evaluation, governance, observability, and production-readiness needs
12. Open risks, validation questions, and next technical validation step

## Worked example: financial-services pre-call briefing

- **Problem/outcome:** Relationship managers spend too long gathering CRM notes, support history, internal research, and prior meeting summaries; reduce preparation time and improve consistency.
- **Workflow:** Account workspace calls the API when a relationship manager opens an account before a meeting.
- **First version:** Generate a structured internal briefing from approved account context and return it for relationship-manager review.
- **Out of scope:** Investment recommendations, customer-facing messages, CRM updates, task creation, or any system-changing action without approval.
- **Pattern:** Structured output if the workspace supplies approved context directly; retrieval remains conditional on source approval, ownership, permissions, and freshness.
- **Request sketch:** account ID (required), user ID/role (required), meeting ID (optional), approved context (optional if supplied by the workspace).
- **Response sketch:** status (`draft_ready`, `needs_review`, `cannot_generate`), briefing fields, source notes, and review flags for missing/conflicting context, recommendation-like language, or unclear permission boundaries.
- **Next validation:** confirm approved sources, access boundaries, required response fields, review ownership, logging/retention, and the next request/response contract.

## One-line takeaway

Choose the fit-for-purpose API architecture that makes the workflow clear, bounded, explainable, reviewable, and ready for technical validation.
