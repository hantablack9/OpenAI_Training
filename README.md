# OpenAI Practitioner Notes

Interview-ready notes from the OpenAI PartnerU learning tracks. The repository is organized **by course first**. Topic notes sit inside each course folder so you can read the course guide before diving into a specific module.

## How to use the notes

1. Open the course `README.md` for the plain-English story, mental model, interview prompts, and fact-check notes.
2. Use the linked module notes for deeper checklists, worked examples, and handoff templates.
3. Treat product names, model IDs, availability, pricing, limits, retention, and access programs as time-sensitive. Re-check the linked official documentation immediately before implementation or a customer commitment.

## Required practitioner tracks

| Course | Course guide | Module notes |
|---|---|---|
| OpenAI Technical Practitioner | [course guide](courses/openai-technical-practitioner/README.md) | [notes](courses/openai-technical-practitioner/notes/openai-technical-practitioner-notes.md) |
| API Deployment Practitioner | [course guide](courses/api-deployment-practitioner/README.md) | [10 module notes](courses/api-deployment-practitioner/README.md#module-notes) |
| Codex Deployment Practitioner | [course guide](courses/codex-deployment-practitioner/README.md) | [notes](courses/codex-deployment-practitioner/README.md#module-notes) |
| OpenAI Cyber Practitioner (listed in PartnerU as **OpenAI Cyber Deployment Practitioner**) | [course guide](courses/cyber-deployment-practitioner/README.md) | [notes](courses/cyber-deployment-practitioner/README.md#module-notes) |

## Additional completed tracks

- [ChatGPT Solutions Practitioner](courses/chatgpt-solutions-practitioner/README.md)
- [ChatGPT Deployment Practitioner](courses/chatgpt-deployment-practitioner/README.md)
- [Codex Solutions Practitioner](courses/codex-solutions-practitioner/README.md)
- [OpenAI Cyber Solutions Practitioner](courses/cyber-solutions-practitioner/README.md)
- [Consultative Solutions Practitioner](courses/consultative-solutions-practitioner/README.md)

## Fact-check baseline

The current-product checks were refreshed on **2026-09-16** against official OpenAI documentation:

- The Responses API supports model responses, tools, structured output, and conversation/state options; `json_schema` Structured Outputs are distinct from older JSON mode. See the [Responses API reference](https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses) and [create a response](https://developers.openai.com/api/reference/cli/resources/responses/methods/create).
- API data handling is endpoint- and feature-specific. API data is not used for training by default; abuse-monitoring retention and application-state retention are different concepts, and Zero Data Retention/Modified Abuse Monitoring require eligibility and approval. See [Your data](https://developers.openai.com/api/docs/guides/your-data).
- API troubleshooting should retain request IDs and rate-limit headers without logging sensitive customer content. See the [API overview](https://developers.openai.com/api/reference/overview).
- Current model names, capabilities, pricing, limits, and availability are volatile. Use the [model guidance](https://developers.openai.com/api/docs/guides/latest-model) and dated model pages rather than copying old course examples.
- The current model catalog lists OpenAI Daybreak cyber models, including GPT-5.6 Cyber, Daybreak Red, and Daybreak Blue. Treat that as a dated catalog fact—not a promise of access or eligibility—and verify the approved route before making a customer commitment. See the [models catalog](https://developers.openai.com/api/docs/models).
- Codex use cases include code review/security workflows and long-running or reusable engineering tasks, but the course notes describe operating patterns and guardrails; they are not guarantees of account access or product behavior. See [Codex use cases](https://developers.openai.com/codex/use-cases).

## Labs and artifacts

- [Codex rollout lab script](codex/scripts/build_codex_rollout_lab.py)
- [Codex rollout PDF](codex/output/Codex_Enterprise_Rollout_Design.pdf)
- [Northstar security lab script](cyber/scripts/build_northstar_lab.py)
- [Northstar security PDF](cyber/output/Northstar_Financial_Customer_Security_Recommendation.pdf)
