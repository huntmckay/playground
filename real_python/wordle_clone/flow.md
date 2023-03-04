# flow.md

```mermaid
---
Title: wydle.py
---
flowchart LR
    A[python3 wyrdle.py] --> B{User Guess}
    B --> C(Wrong Guess +1 counter) --> B
    C --> F|Guess Counter| --> G[End & display word]
    B --> D(Correct Guess) --> E[Break & display word]
```
