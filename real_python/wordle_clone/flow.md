# flow.md

```mermaid
---
Title: wydle.py
---
flowchart LR
    A[python3 wyrdle.py] --> B(User Guess)
    B --> C{Check Guess}
    C --> |Wrong Guess| --> B
    C --> |Correct Guess| --> G[Break & display word]
```
