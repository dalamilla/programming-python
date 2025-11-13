# QR Code Generator

QR Code Generator microservice implemented on FastAPI.

## Instructions

To start this app:

- Installing Dependencies

```
uv sync
```

- Activating the virtual environment:

```
source .venv/bin/activate
```

- Running FastApi Application:

```
uvicorn main:app --reload
```

- Run FastApi Test Application:

```
pytest
```

## Basic Features

- Receive a query param "data" with the information to codify.
- Return a QR Code with PNG format.
