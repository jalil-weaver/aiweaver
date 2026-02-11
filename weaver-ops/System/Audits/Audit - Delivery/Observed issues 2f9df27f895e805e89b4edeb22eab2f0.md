# Observed issues

## Structural problems

- Delivery readiness is assumed instead of explicitly validated
- Delivery start is not gated by confirmed execution capacity
- Delivery timelines can be communicated before capacity is secured
- No formal system condition defines when Delivery can legitimately start
- Capacity uncertainty is managed informally instead of structurally
- Staffing availability is treated as an execution detail instead of a start gate
- No explicit rule separates commercial continuation from operational readiness

---

## Symptoms

- Delivery timelines announced while staffing is still uncertain
- Hidden waiting time between Framing closure and real execution start
- Client perceives delays without understanding the blocking factor
- PM or Sales absorbs pressure caused by missing capacity
- Delivery kickoff prepared while team composition is still evolving
- External developers onboard mid-flight, increasing ramp-up cost
- Negotiation with developers happens in parallel with planning
- Execution starts with partial teams or assumptions
- Deadlines slip due to late capacity confirmation
- Delivery progress is discussed while nothing is actually buildable

---

## SPOF

- Founder or senior profiles arbitrating delivery feasibility manually
- Implicit promises made before execution capacity is secured
- Ad hoc negotiation with external developers
- Delivery start depending on informal confirmation of availability
- No system-level mechanism to block Delivery when capacity is missing

---

## Boundaries

### Delivery start (current state)

- *Delivery is considered started once development is agreed after Framing.*
- *Operational readiness is assumed, not explicitly validated.*
- *Execution may be prepared while staffing is still pending.*

---

### Delivery end (current state)

- *Delivery is considered finished when features are mostly implemented.*
- *Acceptance is implicit or negotiated informally with the client.*
- *No formal Delivery closure separating Delivery from Evolution or Maintenance.*

---

## Core insight

Delivery issues are not caused by execution quality.

They are caused by a **missing system-level gate between commercial decision and operational reality**.

The system currently allows Delivery to start **before it is actually possible to execute**.