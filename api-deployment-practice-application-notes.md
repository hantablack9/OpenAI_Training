# API Deployment Practice Application — concise notes

## Case and decision rule

Northstar Retail Group wants an internal Employee Policy API for routine HR, travel, benefits, and IT questions over approved company documents. The core pattern—retrieval-grounded text answers with structured output, fallback, and escalation—is plausible. The central rule is: a working staging path is evidence of progress, not proof of deployment readiness.

Always separate:

- **Confirmed evidence:** what the case directly demonstrates.
- **Assumptions:** what may be true but needs confirmation.
- **Open questions:** what must be clarified before release, remediation, or escalation.

## Architecture, contract, and capability fit

- Keep the first release to routine policy self-service; exclude HR decisions, legal advice, record updates, automated ticket creation, benefits changes, and restricted employee-relations topics unless separately approved.
- Verify role and region context rather than trusting caller-provided fields; define behavior when context is missing or unreliable.
- Contract failure states for missing, outdated, region-specific, role-specific, restricted, ambiguous, unsupported, and retrieval-failure cases. Prefer structured reasons such as `missing_source`, `restricted_content`, `clarification_required`, `unsupported_request`, and `escalation_required`.
- Define the meaning and owner of any `confidence_label`; do not treat it as a calibrated model confidence score without evidence.
- Use only the complexity the workflow needs; realtime, voice, image, research-style, action-taking, and specialized optimization were not justified for the first pilot.

## Security, data, and governance blockers

- Map input, retrieved, output, and logged data. Internal-only does not automatically mean low risk.
- Verify authentication, authorization, role/region context, and permission-aware retrieval.
- Use only approved, current, region-appropriate sources. Exclude or permission-gate restricted HR/employee-relations content and route sensitive topics to an approved HR/Legal path.
- For Northstar’s source set: HR Handbook and IT policy are approved/current; Travel policy is US/Canada approved with UK pending; benefits coverage varies by region; employee-relations procedure is restricted.
- Confirm logging masking, retention, access control, and sensitive-content exclusion for questions, user IDs, snippets, answers, errors, and timestamps.
- Name security, privacy, source-owner, release, support, HR Operations, and HR Legal owners.

## Validation, observability, and operations

Current proof: 42 tests, 35 common-question passes, 4 inconsistent ambiguous fallbacks, and 3 restricted/region-specific cases answered when fallback or escalation was expected. Missing coverage includes manager-only differences, restricted content, missing/outdated/conflicting sources, and regional edge cases.

Add expected outcomes for answer, clarify, refuse, fallback, and escalation. Monitor more than health and latency:

- retrieval failures, missing-source rate, source version/freshness;
- fallback and human-escalation rate/reason;
- role/region error patterns and restricted-topic attempts;
- release version, usage, cost/consumption, quotas/rate limits;
- alerts, incident response, rollback/disablement, and support route.

## Final recommendation

**Remediate before release.** Preserve the useful retrieval-grounded design, but do not expose it to pilot users until contract behavior, source ownership, restricted-content handling, role/region verification, logging controls, expanded validation, observability, release approval, and support ownership are remediated with named owners.

The recommendation could change to “proceed with conditions” once those controls and evidence support a limited pilot. Escalate if privacy, logging, restricted-source, regional-policy, or governance questions exceed the working team’s authority.

## Practitioner exam reminders

- Start architecture with the customer problem, workflow, outcome, boundaries, and constraints.
- Choose interfaces, models, tools, and agentic complexity from workflow needs—not defaults or novelty.
- Treat authentication, authorization, data minimization, retrieval permissions, evals, human review, observability, rollback, escalation, and ownership as release concerns.
- Use the simplest pattern that completes the approved workflow safely and reliably; specialized or multimodal patterns require fit evidence and validation.
- When access controls, eval evidence, incident ownership, or other release blockers are unresolved, recommend remediation before release with named owners and evidence requirements.

## Handoff template

State the customer situation, recommendation option, confirmed/assumed/unknown evidence, readiness gaps, scope and exclusions, owners and next action, and the evidence that would change the decision.
