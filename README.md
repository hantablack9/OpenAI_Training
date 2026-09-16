# OpenAI Training

Personal notes and lab exercises from OpenAI practitioner/solutions training tracks — API architecture and deployment, ChatGPT, Codex, cybersecurity, and consultative solutions.

Content is organized **topically first** (by subject area), then **functionally** (`notes/` for write-ups, `scripts/` for lab build scripts, `output/` for generated deliverables).

## Layout

```
.
├── api/            # API solution architecture, deployment, security, and ops
│   └── notes/
├── chatgpt/        # ChatGPT solutions and deployment
│   └── notes/
├── codex/          # Codex solutions and deployment
│   ├── notes/
│   ├── scripts/    # lab PDF generator
│   └── output/     # generated lab deliverable
├── cyber/          # Cybersecurity solutions and deployment
│   ├── notes/
│   ├── scripts/    # lab PDF generator
│   └── output/     # generated lab deliverable
├── general/        # cross-cutting technical and consultative notes
│   └── notes/
└── tmp/            # scratch copies and preview renders from drafting the labs
```

## API

Concise notes on API solution architecture, deployment, security, and production readiness.

- [api-solution-architecture-notes.md](api/notes/api-solution-architecture-notes.md)
- [api-contracts-and-core-interfaces-notes.md](api/notes/api-contracts-and-core-interfaces-notes.md)
- [context-data-retrieval-grounded-api-notes.md](api/notes/context-data-retrieval-grounded-api-notes.md)
- [model-and-capability-selection-notes.md](api/notes/model-and-capability-selection-notes.md)
- [realtime-voice-multimodal-api-experiences-notes.md](api/notes/realtime-voice-multimodal-api-experiences-notes.md)
- [deep-research-images-distillation-specialized-api-pattern-fit-notes.md](api/notes/deep-research-images-distillation-specialized-api-pattern-fit-notes.md)
- [api-security-data-handling-access-controls-notes.md](api/notes/api-security-data-handling-access-controls-notes.md)
- [devops-observability-production-readiness-notes.md](api/notes/devops-observability-production-readiness-notes.md)
- [api-deployment-practice-application-notes.md](api/notes/api-deployment-practice-application-notes.md)
- [prompt-design-evals-moderation-guardrails-human-review-notes.md](api/notes/prompt-design-evals-moderation-guardrails-human-review-notes.md)

## ChatGPT

- [openai-chatgpt-solutions-practitioner-notes.md](chatgpt/notes/openai-chatgpt-solutions-practitioner-notes.md)
- [openai-chatgpt-deployment-practitioner-notes.md](chatgpt/notes/openai-chatgpt-deployment-practitioner-notes.md)

## Codex

**Notes**
- [openai-codex-solutions-practitioner-notes.md](codex/notes/openai-codex-solutions-practitioner-notes.md)
- [openai-codex-deployment-practitioner-notes.md](codex/notes/openai-codex-deployment-practitioner-notes.md)
- [codex-deployment-practitioner-notes.md](codex/notes/codex-deployment-practitioner-notes.md)

**Lab: Codex Enterprise Rollout Design**
- Script: [`scripts/build_codex_rollout_lab.py`](codex/scripts/build_codex_rollout_lab.py)
- Output: [`output/Codex_Enterprise_Rollout_Design.pdf`](codex/output/Codex_Enterprise_Rollout_Design.pdf)

## Cybersecurity

**Notes**
- [openai-cyber-solutions-practitioner-notes.md](cyber/notes/openai-cyber-solutions-practitioner-notes.md)
- [openai-cyber-practitioner-notes.md](cyber/notes/openai-cyber-practitioner-notes.md)

**Lab: Northstar Financial Customer Security Recommendation**
- Script: [`scripts/build_northstar_lab.py`](cyber/scripts/build_northstar_lab.py)
- Output: [`output/Northstar_Financial_Customer_Security_Recommendation.pdf`](cyber/output/Northstar_Financial_Customer_Security_Recommendation.pdf)

## General / consultative

- [openai-technical-practitioner-notes.md](general/notes/openai-technical-practitioner-notes.md)
- [openai-consultative-solutions-practitioner-notes.md](general/notes/openai-consultative-solutions-practitioner-notes.md)

## Regenerating lab PDFs

Run from the repo root so the scripts' relative output paths resolve correctly:

```bash
pip install reportlab
python codex/scripts/build_codex_rollout_lab.py
python cyber/scripts/build_northstar_lab.py
```
