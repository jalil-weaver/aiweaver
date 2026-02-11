# State guide

A state represents **where the system is allowed to be** inside a workflow.

### **Rules**

- Has explicit entry conditions
- Has explicit exit conditions
- Is irreversible
- Exists to protect execution

### **How to use states**

- States prevent “we’ll see later” situations
- Work cannot progress outside a state
- A workflow moves only when a state is closed

> If movement is unclear, the state is missing or badly defined.
>