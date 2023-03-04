# flow.md

```mermaid
---
Title: wydle.py
---
flowchart LR
    A[python3 wyrdle.py] --> B(User Guess)
    B --> C{Check Guess}
    C --> |Wrong Guess| F{Counter < 6} 
    F --> |Guess Count <= 5| B
    F --> |Guess Count > 5| F[End and display word]
    C --> |Correct Guess| D[Break and display word]
```
