# FastAPI Framework Guide

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

## Key Features
- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- **Fast to code**: Increase the speed to develop features by about 200% to 300%.
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors.
- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Setup
Install it using pip:
`pip install fastapi uvicorn`

Run the server:
`uvicorn main:app --reload`
