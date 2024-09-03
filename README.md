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

To run the backend server, initialize a virtual environment by running the following from the `backend` directory:

```bash
python3 -m venv .venv
```

Acivate the virtual environment by running the following from the `backend` directory:

-   Windows:

```bash
.venv\Scripts\activate
```

-   Linux/Unix/MacOs:

```bash
source .venv/bin/activate
```

Your terminal prompt should indicate the virtual environment is active by displaying `.venv`.

Install the required packages from `requirements.txt` by running the following from the `backend` directory:

```bash
python3 -m pip install -r requirements.txt
```

#### Server

To run the server, run the following command from the `backend` directory:

```bash
python3 run.py server
```

(or you can use `uvicorn` yourself)

```bash
python3 -m uvicorn app:app --reload
```

#### Tests

To run the tests, run the following command from the `backend` directory:

```bash
python3 run.py test
```

(or you can use `pytest` yourself)

```bash
python3 -m pytest tests
```

#### Type Checker

To type check the Python code, run the following command from the `backend` directory:

```bash
python3 run.py mypy
```

(or you can use `mypy` yourself, but make sure to run the `src` and `tests` tests separately)

```bash
python3 -m mypy src
python3 -m mypy tests
```

### Frontend

The frontend React application code is provided, but if you're only interested in running it, simply open the `frontend/build/index.html` file in your web browser.
