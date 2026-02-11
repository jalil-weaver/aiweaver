# Workflow - Framing change

## **Purpose**

Transform a requested product change into a clear, bounded, and estimable change scope, without rewriting existing documentation.

---

## **Entry Conditions**

- Existing product already delivered or under maintenance
- [Change Specification](../Related%20documents/Change%20Specification%202fedf27f895e80d3a75cee312b5e72cb.md) available
- [Product Roadmap](../Related%20documents/Product%20Roadmap%20301df27f895e8021a83ccc7f2ead5334.md) if existing
- [Product documentation](../Related%20documents/Product%20Documentation%202fddf27f895e80bba212d437b6395575.md) available
- Access to existing product documentation and design

---

## **Exit Conditions**

- [Product documentation](../Related%20documents/Product%20Documentation%202fddf27f895e80bba212d437b6395575.md) updated (if needed)
- [Technical documentation](../Related%20documents/Technical%20Documentation%202fddf27f895e80a2b30dfb468cf8729b.md) updated (if needed)
- Updated [design](../Related%20documents/Design%202fddf27f895e8090a5c8e6a8a0fdbe95.md) produced if required
- Change ready for Development Estimation (change mode)

---

## **States**

---

[**State 0 - Change Qualification & Lock**](Workflow%20-%20Framing%20change/State%200%20-%20Change%20Qualification%20&%20Lock%202fedf27f895e80d0a741e4cc5a2b0c18.md)

Clarify and validate the change request before any framing work starts.

---

[**State 1 - Change Scope Definition**](Workflow%20-%20Framing%20change/State%201%20-%20Change%20Scope%20Definition%202fedf27f895e801da2dadb6d7b1e6d76.md)

Define precisely what is added, modified, or removed, as a strict delta from the existing product.

---

[**State 2 - Technical Decision Gate**](Workflow%20-%20Framing%20change/State%202%20-%20Technical%20Decision%20Gate%202fedf27f895e802ab84af73b1ec8922e.md)

Produce updated design elements only if the change impacts UX or UI.

---

[**State 3 - Change Lock & Handover**](Workflow%20-%20Framing%20change/State%203%20-%20Change%20Lock%20&%20Handover%202fedf27f895e80a0a608ed6437d796e7.md)

Validate and freeze the change scope for estimation and delivery.

---

## **Invariants**

- Existing documentation is never rewritten
- Change scope is always expressed as a delta
- No estimation or pricing happens in this workflow
- One change request produces one Change Specification
- States are irreversible