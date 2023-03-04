# flow.md

```mermaid
---
Title: wydle.py
---
flowchart LR
    A[python3 wyrdle.py] --> B{User Guess}
    B --> C(Check Guess) --> D
    D --> E|Wrong Guess| --> B
    D --> F|Correct Guess| --> G[Break & display word]
```
