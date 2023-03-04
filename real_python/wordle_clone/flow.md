# flow.md

```mermaid
---
Title: wydle.py
---
flowchart LR
    A[python3 wyrdle.py] --> B(User Guess)
    B --> C{Check Guess}
    C --> E|Wrong Guess| --> B
    C --> F|Correct Guess| --> G[Break & display word]
```
