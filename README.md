# API_flask
An hello world project to put hands up on API programming

## Prerequisites

Ensure you have the following installed:
- Python 3.6+ (check with `python --version` or `python3 --version`)
- `pip` (Python package manager, check with `pip --version`)

---

## Setting up a Virtual Environment

### macOS / Linux

1. Open your terminal.
2. Navigate to your project directory:
3. Create the virtual env
```bash
python3 -m venv venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
### Windows
1. Open your terminal.
2. Navigate to your project directory:
3. Create the virtual env
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
venv\Scripts\activate
```

## Installing Requirements
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

## Run 
Run the Flask app:
```bash
python3 hello_api.py
```

# 🐍 Flask Hello World API (Docker)

Questa è una semplice API Flask che risponde con un saluto personalizzato.

---

## 🚀 Avvio con Docker

Costruisci l'immagine:

```bash
docker build -t flask-hello .
```
```bash
docker run -d -p 5000:5000 flask-hello
```


