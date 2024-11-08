# QR Code Generator

QR Code Generator microservice implemented on FastAPI.

## Instructions

To start this app:

- Installing Dependencies

```
poetry install
```

- Activating the virtual environment:

```
poetry shell
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
