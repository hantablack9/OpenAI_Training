# Realtime, Voice, and Multimodal API Experiences — concise notes

## Core principle

Start with the user moment and choose the simplest modality that safely solves it. Realtime, voice, image, or multimodal interaction is justified by workflow need, user context, risk, accessibility, consent, and readiness evidence—not novelty.

## Choose the modality

- **Realtime interaction:** low-latency back-and-forth; design turn-taking, interruptions, tool delays, correction, fallback, and monitoring.
- **Speech-to-text:** validate audio quality, languages/accents, domain terms, correction, low confidence, consent, retention, review, and deletion.
- **Text-to-speech:** provide pause/replay/slow/switch-to-text controls, readable text for important details, and AI-generated voice disclosure.
- **Voice patterns:** voice-to-action needs confirmation before sensitive or irreversible actions; systems-to-voice provides timely spoken context; voice-to-voice preserves spoken continuity.
- **Image input:** treat images as evidence; validate quality, permission, blur/privacy, clarification, and human review. Do not make high-impact decisions from image evidence alone.
- **Image output:** validate whether an image is needed, plus rights, brand/legal, safety, accessibility, and human review; provide alternatives.
- **Multimodal:** define each modality’s purpose, primary/supporting channel, switch point, confirmation point, fallback, and review path.

For live audio, select the connection path from the workflow: WebRTC for browser/mobile direct audio, WebSocket when a server handles raw audio, or SIP for telephony. These capabilities and model support can change, so verify current documentation immediately before implementation.

## Realtime architecture

- **Speech-to-speech Realtime:** direct live audio, natural turn-taking, interruptions, and realtime tools.
- **Chained pipeline:** STT → text agent → TTS; preferable when visible intermediate text, durable transcripts, deterministic checks, or approval steps matter.

## Interaction flow

1. Start with clear modality, AI-voice, recording, and consent disclosure.
2. Capture input/context and show what is being listened to, recorded, or processed.
3. Clarify low-confidence speech, unclear images, or missing context before proceeding.
4. Respond with progress and make important details reviewable in text.
5. Require explicit confirmation before consequential actions (booking, billing, record changes, policy exceptions).
6. Provide pause, stop, correct, repeat, slow-down, and channel-switch controls.
7. On failure, use a deterministic fallback: retry/replace media, switch to text, request human review, or hand off.

## Safety, privacy, accessibility, and readiness

- Define allowed actions, hard boundaries, and review/escalation points before guidance, record updates, or actions.
- For audio/images/transcripts, document purpose, access, storage, retention, deletion, user correction/replacement, derived artifacts, logging restrictions, and prohibited capture/reuse.
- Provide captions/transcripts, readable text alternatives, image descriptions, non-visual alternatives, pause/repeat/slow controls, and another approved channel.
- Monitor latency, turn-taking, interruptions, audio/image quality, transcription/interpretation errors, tool/retrieval delays, fallback and handoff rates, corrections, consent/privacy flags, accessibility blockers, safety triggers, and reviewer/user feedback.

## Blueprint handoff template

1. **User moment:** user, goal, context, input, output, urgency, and why text-only is insufficient (if applicable).
2. **Modality fit:** selected pattern, Realtime vs chained architecture, connection method, supporting modality, fallback, and rejected alternatives.
3. **Flow:** input → context → clarification → response → confirmation → tool/system action → fallback/escalation.
4. **Controls:** safety boundary, disclosure/consent, human review, accessibility, media handling, sensitive-data limits.
5. **Verification/monitoring:** pre-release tests and modality-specific signals.
6. **Recommendation:** safest next step, rationale, top blocker/condition, owner, and evidence that would change the recommendation.

