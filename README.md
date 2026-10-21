# Лабораторная работа №1

Python 3.11+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs

Данные хранятся только в оперативной памяти и исчезают после перезапуска.
