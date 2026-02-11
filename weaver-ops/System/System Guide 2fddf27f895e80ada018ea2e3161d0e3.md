# System Guide

This system provides a **clear structure for operations**.

Its purpose is to:

- organize work explicitly
- reduce ambiguity
- create stable working conditions
- allow consistent execution over time

It defines a **shared operational language** used by everyone involved in delivery.

---

## **Core Structure**

The system is composed of six elements.

Each one has a specific role and must be used for that purpose only.

### **Workflow (offers)**

Represents **what we deliver**.

A workflow structures an offer from start to finish and defines the global logic of execution.

[Workflow guide](System%20Guide/Workflow%20guide%202fddf27f895e802d9b28ccdaa4ed1cf6.md)

---

### **State**

Represents **where we are allowed to be** inside a workflow.

A state protects execution by defining when work can move forward and when it must stop.

[State guide](System%20Guide/State%20guide%202fddf27f895e80cfb7dcc76a56de791c.md)

---

### **Action**

Represents **how work progresses**.

An action is a single execution step that produces a visible result and moves the system forward.

[Action guide](System%20Guide/Action%20guide%202fddf27f895e80b78433dd6b9800c39f.md)

---

### **Work**

Represents a **bounded execution unit**.

A work exists to **produce outputs** that can be used by workflows.

[Work guide](System%20Guide/Work%20guide%202fddf27f895e80a0bca1f27609a6fd89.md)

---

### **Daily Ops**

Represents **continuous operational activity**.

Daily operations keep the system running over time and support execution without belonging to a specific delivery flow.

[Daily ops guide](System%20Guide/Daily%20ops%20guide%202fddf27f895e8067a167c559157cd01e.md)

---

### **Related Documents**

Represents **shared sources of truth**.

Related documents make work explicit and reusable across the system. They can be inputs, outputs, or references.

[Related documents guide](System%20Guide/Related%20documents%20guide%202fddf27f895e80a398f1fc9acf01be1c.md)

---

## **Responsibility Rules (RACI)**

Responsibilities are defined **only where execution happens**.

### **Where RACI is required**

**Action**

- R (Responsible): mandatory
- A (Accountable): mandatory
- C / I: optional

An action without a clear R and A is invalid.

**Work**

- R (Responsible): mandatory
- A: optional

A work must always have one clear owner.

---

## **How the system is used**

1. **Start from a Workflow**
    
    Work is always organized inside a workflow. A workflow defines the beginning and the end of what is delivered.
    
2. **Move through States**
    
    Each workflow progresses through states. Entry and exit conditions determine when the system can move forward.
    
3. **Execute Actions**
    
    Inside each state, actions are executed to produce concrete results. If an action fails, the state cannot be closed.
    
4. **Run Works when needed**
    
    Some actions trigger works. Works execute specific efforts without taking decisions and return measurable results.
    
5. **Rely on Daily Operations**
    
    Daily operations support execution continuously. They are not part of workflows but interact with them when necessary.
    
6. **Use Related Documents as references**
    
    Documents are used wherever needed. They are never owned by a single workflow and always live in a shared library.
    

---

## **How to improve or change the system**

Anyone modifying the system must follow these rules:

- Do not add a new concept unless absolutely necessary
- Change structure only if execution is unclear or unsafe
- Prefer simplifying before adding
- Never mix the roles of two elements
- If something feels ambiguous, make it explicit

The system is meant to **evolve**, but always through **clear rules and explicit changes**.

---

## **Key principle**

> The system exists to make execution clear.
> 

> If clarity is lost, the system must be adjusted.
> 

[Templates](System%20Guide/Templates%202fddf27f895e80928a08c9730b72195d.md)