# Workflow - Development estimation

## **Purpose**

Produce reliable and executable development scenarios, including infrastructure impact when required, from validated inputs, without assumptions.

---

## **Entry Conditions**

At least **one** of the following input sets is available and validated:

### **Option A - Full Product Scope**

- [Product documentation](../Related%20documents/Product%20Documentation%202fddf27f895e80bba212d437b6395575.md) available
- [Delivery scenario](../Related%20documents/Delivery%20Scenario%202fddf27f895e80fdaea1c975aa3cadfc.md) or [Product Roadmap](../Related%20documents/Product%20Roadmap%20301df27f895e8021a83ccc7f2ead5334.md) available
- [Design](../Related%20documents/Design%202fddf27f895e8090a5c8e6a8a0fdbe95.md) available and validated

### **Option B - Product Change**

- Change specification
- Design updated (if impacted)

### **Option C - Infrastructure Change**

- Infrastructure Change Brief

---

## **Exit Conditions**

- At least one delivery scenario produced
    
    **or**
    
- At least delivery team produced
    
    or
    
- Estimation blocked with missing inputs explicitly documented

---

## **States**

---

[**State 0 - Estimation Readiness Check**](Workflow%20-%20Development%20estimation/State%200%20-%20Estimation%20Readiness%20Check%202fedf27f895e80f3af55f6ff5fdfd31b.md)

Verify that provided inputs are sufficient to start estimation.

---

[**State 1 - Scenario Construction**](Workflow%20-%20Development%20estimation/State%201%20-%20Scenario%20Construction%202fedf27f895e806f8085ce7468c4c170.md)

Build one or more executable development scenarios, including infrastructure requirements.

---

[**State 2 - Estimation Consolidation**](Workflow%20-%20Development%20estimation/State%202%20-%20Estimation%20Consolidation%202fedf27f895e80e4b19ae28439120b72.md)

Finalize scenarios and make them usable for pricing by Sales.

---

## **Invariants**

- Estimation never starts without sufficient inputs
- No assumption is allowed
- Estimation never produces pricing
- Infrastructure and IA are always included when relevant
- States are irreversible