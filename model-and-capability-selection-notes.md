# Model and Capability Selection for API Solutions — concise notes

## Core principle

Model selection is a workflow-and-evidence decision, not a prestige ranking. Start with the job the API must do, then select the least complex capability that meets predefined quality, safety, latency, reliability, and economic thresholds.

## 1) Define the workflow

- Classify the primary task: generate, summarize, classify, extract, reason, transform, retrieve, act through a tool, or support live/multimodal interaction.
- Specify input/output modality and the primary output.
- Record technical requirements: reasoning depth, context/retrieval needs, output schema, latency, throughput, reliability, interface behavior, and review/escalation rules.
- Record risk requirements: sensitive data, human review, safety boundary, quality threshold, permissions, governance, and observability signals.

## 2) Build a current shortlist

- Use current official model/catalog and comparison guidance; do not rely on memory or old examples.
- Record exact model IDs, official source links, date checked, capabilities, limits, availability, and pricing assumptions.
- Filter on must-haves first (modality, interface, context, output behavior, operational fit), then compare preferences.
- Test the same representative cases against each candidate. Compare task quality, schema validity, review triggers, latency, throughput, and cost per successful task.

## 3) Avoid selection shortcuts

Do not choose the newest/flagship model, lowest nominal token price, or a model from an old code sample without workflow evidence. Total task cost includes input/output, retrieval or tool calls, retries, failures, reviewer correction, and rework. A higher-capability model is justified only when it materially improves successful task completion enough to offset added cost, latency, or operating burden.

Decision positions: retain; retain with conditions; remove; or defer. Name a provisional lead and the questions that could change the decision.

## 4) Stress-test the recommendation

- Cost/scale: volume, burstiness, input/output length, growth, retries, review rate, and peak throughput.
- Latency/reliability: synchronous vs. async/streaming behavior, timeouts, retries, fallbacks, valid structured output, and failure states.
- Safety/validation: representative, edge, known-failure, high-risk, ambiguous, seasonal, and adversarial cases; human review where decisions are sensitive or require approval.
- Product facts: revalidate current model/API support, structured-output behavior, modalities, tools/retrieval, limits, pricing, availability, and SDK behavior against official documentation.
- Observability signals: latency, timeout rate, output validity, retry rate, review-trigger volume, fallback use, and failure categories.

## Model & Capability Selection Rationale template

1. Workflow task and business/customer outcome
2. Input/output modality and required capabilities
3. Contract/interface requirements (fields, state, streaming/async, errors, retries, idempotency)
4. Candidate capability patterns and dated model shortlist
5. Recommended pattern/candidate and evidence against thresholds
6. Rejected alternatives and why they are not the right first choice
7. Cost, latency, scale, reliability, safety, and review tradeoffs
8. Risks, assumptions, validation questions, and next review area
9. Exact product facts to revalidate before build

## Handoff checklist

- Use exact tested IDs and representative cases.
- Separate durable decision logic from volatile product facts.
- State what would change the recommendation (quality failure, peak-latency failure, new retrieval/tool need, sensitive-data review, or changed pricing/availability).
- Hand off deeper review to the right owner: contract/interface, security/data handling, retrieval, tool/action design, evals/guardrails, observability, or production readiness.
