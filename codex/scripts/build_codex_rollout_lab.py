from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

OUTPUT = "codex/output/Codex_Enterprise_Rollout_Design.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=LETTER,
    rightMargin=0.62 * inch,
    leftMargin=0.62 * inch,
    topMargin=0.48 * inch,
    bottomMargin=0.45 * inch,
)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER,
    fontName="Helvetica-Bold", fontSize=15.5, leading=18, textColor=colors.HexColor("#12304A"),
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], alignment=TA_CENTER,
    fontName="Helvetica", fontSize=8.8, leading=11, textColor=colors.HexColor("#52616B"),
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=9.8, leading=12, textColor=colors.HexColor("#0C5A72"), spaceBefore=4, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="BodyCompact", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.25, leading=10.4, textColor=colors.HexColor("#1F2933"), spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.7, leading=9.5, textColor=colors.HexColor("#1F2933"), spaceAfter=1,
))

story = []
story.append(Paragraph("Codex Enterprise Rollout Design", styles["TitleCenter"]))
story.append(Paragraph("Linton Labs | governed expansion from a billing-platform pilot", styles["Subtitle"]))

story.append(Paragraph("Recommendation", styles["Section"]))
story.append(Paragraph(
    "Adopt a staged rollout beginning with the legacy billing repository and two named engineering teams. Start with low-friction local surfaces, enforce review and workspace isolation, and expand only when evidence shows safe adoption, reliable verification, and support readiness. Codex accelerates implementation; humans retain ownership of approvals, merges, releases, and production risk.",
    styles["BodyCompact"],
))

story.append(Paragraph("Explicit decisions", styles["Section"]))
decisions = [
    [Paragraph("Decision", styles["Small"]), Paragraph("Default for phase 1", styles["Small"])],
    [Paragraph("Surface strategy", styles["Small"]), Paragraph("IDE extension for day-to-day edits; Codex app for review/orchestration; CLI for reproducible scripted work. Worktrees are mandatory for parallel or risky changes; cloud tasks are forbidden for proprietary billing code until policy approval.", styles["Small"])],
    [Paragraph("Model strategy", styles["Small"]), Paragraph("Use the configured general model for most work; use an API-key workflow only with approved credentials and data controls. Escalate reasoning for architecture/debugging; use Spark only for narrow, low-latency loops with tighter verification.", styles["Small"])],
    [Paragraph("Context continuity", styles["Small"]), Paragraph("Checkpoint at task boundaries, before compaction, and after failed attempts. Preserve decisions, changed files, tests, and proof gaps in the task record; recover by restarting from the last verified checkpoint.", styles["Small"])],
    [Paragraph("Governance bundle", styles["Small"]), Paragraph("Standardize <font name='Courier'>config.toml</font>, <font name='Courier'>AGENTS.md</font>, and allowlisted <font name='Courier'>.rules</font>; require verification commands, review guidance, a definition of done, and a secure-PR skill for billing work.", styles["Small"])],
    [Paragraph("Cloud policy", styles["Small"]), Paragraph("Cache approved dependencies through setup scripts; keep secrets out of prompts and repositories; use environment variables or the approved secret store; internet access is off by default and allowlisted per task.", styles["Small"])],
    [Paragraph("Integrations and admin", styles["Small"]), Paragraph("Begin with manual <font name='Courier'>@codex review</font>; delegate Slack/Linear drafting only, never approvals or production actions. Enable local/cloud access through RBAC groups and track analytics separately from compliance logs.", styles["Small"])],
]
tbl = Table(decisions, colWidths=[1.28 * inch, 5.93 * inch], hAlign="LEFT")
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCEFF3")),
    ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#EEF7F8")),
    ("BOX", (0, 0), (-1, -1), 0.45, colors.HexColor("#9DBCC6")),
    ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.HexColor("#C9DDE2")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
]))
story.append(tbl)

story.append(Paragraph("Guardrails and recovery", styles["Section"]))
story.append(Paragraph(
    "Guardrails: sandboxed execution with least privilege; no secrets in prompts or generated code; internet off by default; mandatory human review, tests, and customer-owned merge/release decisions; log task identity, approvals, tool use, and artifacts. Escalate production access, destructive actions, unsupported integrations, or a request to bypass review.",
    styles["BodyCompact"],
))
story.append(Paragraph(
    "Recovery patterns: (1) If a long-running task drifts or fails, stop, capture the last verified checkpoint, revert unverified changes, and resume with a smaller scoped task. (2) If a surface, model, or cloud environment is unavailable, switch to the approved local fallback, preserve the decision record, rerun validation, and notify the named support owner.",
    styles["BodyCompact"],
))

story.append(Paragraph("Rollout gates and monitoring", styles["Section"]))
story.append(Paragraph(
    "Gate 1: one billing repo, two teams, named reviewers, and baseline metrics. Gate 2: expand to adjacent repos only after verification pass rate, review burden, rollback readiness, and policy adherence are acceptable. Gate 3: consider CI/CD or cloud expansion after repeated evidence, RBAC coverage, support runbook validation, and audit-log completeness. Monitor adoption, verification outcomes, exception/approval rates, secret and internet-policy violations, support tickets, and time to recover.",
    styles["BodyCompact"],
))

doc.build(story)
print(OUTPUT)
