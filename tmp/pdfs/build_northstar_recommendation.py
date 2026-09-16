from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


out = "output/pdf/northstar-financial-customer-security-recommendation.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCentered",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=16,
    leading=20,
    spaceAfter=14,
))
styles.add(ParagraphStyle(
    name="Section",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=10.5,
    leading=13,
    spaceBefore=7,
    spaceAfter=3,
    textColor="#17365D",
))
styles.add(ParagraphStyle(
    name="BodyCompact",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=13.2,
    spaceAfter=5,
))

doc = SimpleDocTemplate(
    out,
    pagesize=letter,
    rightMargin=0.72 * inch,
    leftMargin=0.72 * inch,
    topMargin=0.65 * inch,
    bottomMargin=0.65 * inch,
    title="Northstar Financial Customer Security Recommendation",
    author="OpenAI PartnerU course submission",
)

story = [
    Paragraph("Customer Security Recommendation", styles["TitleCentered"]),
    Paragraph("Northstar Financial | Pre-release decision for customer-account-service", styles["BodyCompact"]),
    Paragraph("Customer situation", styles["Section"]),
    Paragraph(
        "Northstar must decide whether an authorization-related pull request can move toward release in three days. The workflow is stuck between a broad request to clear 62 AppSec findings and the need for one focused, reviewable decision. The AppSec lead can review one security output this week, while engineering needs useful evidence and a clear owner for the release decision.",
        styles["BodyCompact"],
    ),
    Paragraph("Recommended first step", styles["Section"]),
    Paragraph(
        "Run a bounded, read-only Codex Security review of the authorized pull request, its directly related authorization files, and directly related tests. This is more appropriate than reviewing every repository because it addresses the immediate customer-owned decision, has named reviewers, and can produce evidence within the available review capacity. The review should examine the diff and test context, without production testing, exploit reproduction, or automatic remediation.",
        styles["BodyCompact"],
    ),
    Paragraph("Scope, reviewers, and evidence position", styles["Section"]),
    Paragraph(
        "In scope are the pull request, related source context, and related tests. Other repositories, third-party systems, production environments, automatic merge or release decisions, and automatic fixes are out of scope. The AppSec lead and engineering director (with the pull request owner) remain accountable for review and disposition. Direct evidence shows that a role-checking helper is no longer called in one account-update path and that supplied tests cover authenticated self-update. A reasonable inference is that the changed path needs AppSec review. Classify the output as a candidate finding, not a validated vulnerability. It remains unproven whether one customer can update another customer's account because no runtime validation or exploit reproduction was performed.",
        styles["BodyCompact"],
    ),
    Paragraph("Success measures, guardrails, and next action", styles["Section"]),
    Paragraph(
        "Success means a concise evidence record, an explicit AppSec and engineering disposition, documented proof gaps, and a named owner for any follow-up. Preserve human review and the approved read-only boundary; do not promise broad access, guaranteed discovery, remediation, or a security outcome. Before release, the AppSec lead should coordinate the review and record the decision in Northstar's system of record. Engineering then acts on any accepted remediation path. This record enables a release decision and determines whether a separate, bounded follow-up evaluation is justified.",
        styles["BodyCompact"],
    ),
]


def add_page_number(canvas, doc_obj):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColorRGB(0.35, 0.35, 0.35)
    canvas.drawRightString(7.75 * inch, 0.38 * inch, f"Page {doc_obj.page}")
    canvas.restoreState()


doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(out)
