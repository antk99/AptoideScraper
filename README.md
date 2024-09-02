# Aptoide Scraper Project

This project includes a Falcon REST API and a React web application for webscraping and displaying information about Android apps from [Aptoide](https://en.aptoide.com/).

## Installation

Before running the application, ensure you have the following installed:

-   [**Python 3**](https://www.python.org/downloads/)

To verify your installation, run the following from your terminal:

```bash
python3 --version
```

## Instructions

### Backend

To run the backend server, start by initializing a virtual environment and installing the required packages:

```bash
# Run from backend/
python3 -m venv .venv
```

Whenever interacting with the backend, ensure your terminal is using the backend's virtual environment:

* Windows:
```bash
# Run from backend/
.venv\Scripts\activate
```

* Linux/Unix/MacOs
```bash
# Run from backend/
source .venv/bin/activate
```

Your terminal prompt should indicate the virtual environment is active by displaying `.venv`.

Install the required packages from `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
```

#### Server

To run the server, run the following command:

```bash
# Run from backend/
python3 run.py server
```

(or you can use `uvicorn` yourself)

```bash
# Run from backend/src/
python3 -m uvicorn app:app --reload
```

#### Tests

To run the tests, run the following command:

```bash
# Run from backend/
python3 run.py test
```

(or you can use `pytest` yourself)

```bash
# Run from backend/
python3 -m pytest tests
```

#### Type Checker

To type check the Python code, run the following command:

```bash
# Run from backend/
python3 run.py mypy
```

(or you use `mypy` yourself, but make sure to run the `src` and `tests` tests separately)

```bash
# Run from backend/
python3 -m mypy src
python3 -m mypy tests
```

### Frontend

The frontend React application code is provided, but if you're only interested in running it, simply open the `index.html` file from the `frontend/build` directory.

```bash
# Run from frontend/
open build/index.html
```
