from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

OUTPUT = "cyber/output/Northstar_Financial_Customer_Security_Recommendation.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=LETTER,
    rightMargin=0.7 * inch,
    leftMargin=0.7 * inch,
    topMargin=0.6 * inch,
    bottomMargin=0.55 * inch,
)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER,
    fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#12304A"),
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], alignment=TA_CENTER,
    fontName="Helvetica", fontSize=9, leading=12, textColor=colors.HexColor("#52616B"),
    spaceAfter=14,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=10.5, leading=13, textColor=colors.HexColor("#0C5A72"), spaceBefore=5, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="BodyCompact", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.4, leading=12.6, textColor=colors.HexColor("#1F2933"), spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica-Oblique",
    fontSize=9.2, leading=12.2, textColor=colors.HexColor("#1F2933"),
))

story = []
story.append(Paragraph("Northstar Financial\nCustomer Security Recommendation", styles["TitleCenter"]))
story.append(Paragraph("Prepared for the planned customer-portal release", styles["Subtitle"]))

story.append(Paragraph("Customer situation", styles["Section"]))
story.append(Paragraph(
    "Northstar must make a release decision in three days about an authorization-related pull request in the customer-owned <font name='Courier'>customer-account-service</font>. AppSec has 62 open findings and capacity for one focused review; the engineering director needs evidence that developers can act on. The immediate bottleneck is reviewer confidence for this sensitive change, not estate-wide coverage.",
    styles["BodyCompact"],
))

story.append(Paragraph("Recommended first step", styles["Section"]))
story.append(Paragraph(
    "Run a bounded Codex Security review of the pull request and directly related authorization files and tests. This is the most responsible starting point because it is owned, time-sensitive, read-only, and tied to a named human review path. Reviewing every repository or promising automatic fixes would increase scope before Northstar has a usable decision loop.",
    styles["BodyCompact"],
))

story.append(Paragraph("Scope, reviewers, and evidence position", styles["Section"]))
scope_data = [
    [Paragraph("In scope", styles["BodyCompact"]), Paragraph("The authorized pull request, directly related authorization files, and directly related tests.", styles["BodyCompact"])],
    [Paragraph("Out of scope", styles["BodyCompact"]), Paragraph("Other repositories, production testing, exploit reproduction, third-party systems, automatic remediation or merge, and an automated release decision.", styles["BodyCompact"])],
    [Paragraph("Accountable reviewers", styles["BodyCompact"]), Paragraph("AppSec lead and engineering owner; the CISO remains the governance and risk decision owner.", styles["BodyCompact"])],
    [Paragraph("Evidence position", styles["BodyCompact"]), Paragraph("Source facts show that one account-update path no longer calls the prior role-checking helper. Existing tests show authenticated updates, but do not show whether one user can update another customer's account. Classify this as a candidate authorization concern requiring review, not a validated vulnerability. Runtime proof and exploitability remain unproven.", styles["BodyCompact"])],
]
tbl = Table(scope_data, colWidths=[1.25 * inch, 5.85 * inch], hAlign="LEFT")
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF4F7")),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#9DBCC6")),
    ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#C9DDE2")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
story.append(tbl)

story.append(Paragraph("Success measures and guardrails", styles["Section"]))
story.append(Paragraph(
    "Success means AppSec and engineering can accept, suppress, remediate, or request more evidence using a concise record that states source facts, proof gaps, disposition, and owner. Preserve read-only operation, human review, customer-approved logging, and no automatic release decision. Escalate any request for production testing, exploit-heavy validation, broader access, or advanced cyber SME support before proceeding.",
    styles["BodyCompact"],
))

story.append(Paragraph("Next action and owner", styles["Section"]))
story.append(Paragraph(
    "Northstar's AppSec lead and engineering owner should confirm the scope, review the changed path, determine whether authorization is enforced elsewhere, and decide whether additional tests or remediation are needed before release. The partner should facilitate the evidence-led review and record the decision in Northstar's approved system of record. This enables a defensible release decision without claiming guaranteed security.",
    styles["BodyCompact"],
))

doc.build(story)
print(OUTPUT)
