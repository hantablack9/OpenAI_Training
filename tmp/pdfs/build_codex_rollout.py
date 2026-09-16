from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUT = "/Users/hanishpaturi/Documents/ChatGPT/OpenAI/output/pdf/codex-enterprise-rollout-design.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleSmall", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=colors.HexColor("#102A43"), spaceAfter=3))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#486581"), spaceAfter=7))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=colors.HexColor("#0B7285"), spaceBefore=4, spaceAfter=3))
styles.add(ParagraphStyle(name="BodyTiny", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.1, leading=8.3, textColor=colors.HexColor("#243B53"), spaceAfter=1))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=colors.HexColor("#102A43"), spaceAfter=0))
styles.add(ParagraphStyle(name="Label", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.4, leading=8.5, textColor=colors.HexColor("#0B7285"), spaceAfter=0))

def p(text, style="BodyTiny"):
    return Paragraph(text, styles[style])

doc = SimpleDocTemplate(OUT, pagesize=letter, rightMargin=0.42 * inch, leftMargin=0.42 * inch, topMargin=0.34 * inch, bottomMargin=0.3 * inch)
story = []
story.append(p("Codex Enterprise Rollout Design", "TitleSmall"))
story.append(p("Linton Labs | Legacy billing platform first | Partner-ready recommendation", "Subtitle"))

callout = Table([[p("Recommendation: establish one governed default for the billing pilot, prove it with reviewable evidence, then expand one bounded slice at a time.", "Callout")]], colWidths=[7.56 * inch])
callout.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E6FFFA")), ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#0B7285")), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story.append(callout)
story.append(Spacer(1, 4))

left = [
    p("Explicit rollout decisions", "Section"),
    p("<b>1. Surface strategy.</b> Billing engineers default to the Codex IDE extension for day-to-day edits; platform and SRE use the Codex app for reviews and runbooks; CLI is for scripted, reproducible tasks. Use cloud tasks only for explicitly approved, non-sensitive work. Use worktrees for parallel or risky changes; keep single-file fixes in the current branch."),
    p("<b>2. Model strategy.</b> Use the current approved general model by default; use the latest approved API-key workflow model for automation. Escalate reasoning only for high-impact design or debugging. Spark is limited to low-latency, low-risk loops with tighter scope and explicit validation."),
    p("<b>3. Context continuity.</b> Checkpoint at task boundaries, before compaction, and before switching surfaces. Preserve decisions, file scope, commands, tests, and open risks in the task record. Resume from the last checkpoint rather than guessing."),
    p("<b>4. Governance bundle.</b> Ship a versioned config.toml, repo AGENTS.md, and .rules allowlist. AGENTS.md defines verification commands, review guidance, and the done definition; rules block risky commands and require human approval for release-affecting actions."),
]
right = [
    p("Safety and operating controls", "Section"),
    p("<b>5. Cloud and secrets.</b> Cloud environments are off by default for billing work. Setup scripts are pinned and cached; secrets stay in the approved secret store and are never written to prompts, logs, or repositories. Internet access is disabled unless an allowlisted dependency is approved."),
    p("<b>6. Review and integrations.</b> Start GitHub review manually with @codex review; enable automatic reviews only after evidence quality and reviewer burden meet the pilot scorecard. Slack and Linear may receive summaries and bounded follow-ups, never merge, release, or permission decisions."),
    p("<b>7. Admin and monitoring.</b> Enable local and cloud surfaces through RBAC groups. Track analytics for adoption and workflow health; track compliance logs for approvals, sandbox mode, environment, access, and review disposition. The support runbook begins with approvals, sandbox, environment selection, and entitlements."),
    p("<b>Windows posture.</b> Prefer native Windows sandbox mode unelevated. Use elevated only when prerequisites are documented and approved; use WSL semantics when the repo requires Linux tooling. If elevated setup is blocked, fall back to the approved unelevated path and record the limitation."),
]
cols = Table([[left, right]], colWidths=[3.72 * inch, 3.72 * inch], hAlign="LEFT")
cols.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("LINEAFTER", (0, 0), (0, 0), 0.35, colors.HexColor("#BCCCDC"))]))
story.append(cols)
story.append(Spacer(1, 2))

guardrails = Table([[p("Guardrails", "Label"), p("<b>Scope:</b> billing repo and approved adjacent files only; no production testing, release, merge, or permission changes. <b>Evidence:</b> every run records scope, model, surface, commands, tests, approvals, and reviewer disposition. <b>Human gates:</b> humans accept findings, approve patches, merge, release, and expand scope.")]], colWidths=[0.78 * inch, 6.78 * inch])
guardrails.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F4F8")), ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#BCCCDC")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story.append(guardrails)
story.append(Spacer(1, 3))

recovery = Table([[p("Recovery patterns", "Section"), p("<b>Long-running task:</b> checkpoint at each milestone; if context is compacted, reload the checkpoint and confirm scope, decisions, tests, and open risks before continuing. <b>Failure or drift:</b> stop, capture the last known-good state, revert or isolate the change, switch to a safer surface if needed, rerun focused verification, and request reviewer disposition before resuming.")]], colWidths=[1.25 * inch, 6.31 * inch])
recovery.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF7ED")), ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#F6AD55")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story.append(recovery)
story.append(Spacer(1, 3))
story.append(p("Pilot exit criteria: reviewers can reproduce the workflow, approve or reject evidence, and recover from interruption; adoption and compliance signals are visible; no release or access decision is delegated. Expand to one adjacent repo or team only after the billing pilot meets these criteria."))

def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D9E2EC"))
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 0.24 * inch, letter[0] - doc.rightMargin, 0.24 * inch)
    canvas.setFont("Helvetica", 6.5)
    canvas.setFillColor(colors.HexColor("#829AB1"))
    canvas.drawString(doc.leftMargin, 0.12 * inch, "Linton Labs rollout review | Safe by default, easy to adopt, auditable, recoverable")
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.12 * inch, "Codex Enterprise Rollout Design")
    canvas.restoreState()

doc.build(story, onFirstPage=draw_page)
print(OUT)
