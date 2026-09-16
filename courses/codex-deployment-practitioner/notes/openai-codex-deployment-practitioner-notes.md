# Codex Deployment Practitioner — concise notes

- Design the rollout around safe defaults, low-friction adoption, auditability, and recovery for long-running tasks or failures.
- Surface strategy: choose Codex app, IDE extension, CLI, or cloud by team/workflow; make worktree use explicit; define when cloud tasks are required or forbidden; document Windows sandbox posture and WSL/elevated fallbacks.
- Model strategy: set a default model, select the current API-key workflow model only after checking the live model catalog, escalate reasoning only when needed, and use any ultra-low-latency model or mode only for tightly scoped work with explicit verification. “Spark” is course-era terminology; do not assume a current model or alias from this note.
- Context continuity: define checkpoint cadence, compaction policy, preserved decisions, and recovery patterns for failed attempts, drift, surface changes, or restarted threads.
- Governance bundle: maintain `config.toml` defaults, project `AGENTS.md` instructions and done criteria, allowlisted `.rules`, and reusable skills for secure review, CI fixes, and release notes.
- Cloud policy: document setup scripts/caching, keep secrets separate from environment variables, and default agent internet access off with narrow allowlists when justified.
- Integrations: define manual vs automatic GitHub review and safe delegation boundaries for Slack/Linear.
- Admin/monitoring: specify local/cloud enablement and RBAC, analytics vs compliance signals, support runbooks for approvals/sandbox/environment/access, and Windows sign-in/entitlement checks.
- Partner-ready rollout one-pager should state surface/model strategy, context continuity, governance, cloud policy, integrations, admin/monitoring, defaults, guardrails, and recovery patterns for the billing-platform starting point.
- **Course state snapshot:** At the last recorded check, the Advanced Codex Lab — Enterprise Rollout Design deliverable was submitted and PartnerU showed **Awaiting review** and “You’re all done.” Final completion credit depended on manual review. Re-check the dashboard before using this as current status.
