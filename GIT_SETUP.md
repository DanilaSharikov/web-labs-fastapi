# Работа с Git и сдача лабораторных

Локально подготовлены две ветки:
- `lab-01-basic-api` — лабораторная №1, коммит `717ec5f`.
- `lab-02-database` — лабораторная №2, коммит `ace8c29`.

Текущая ветка: `lab-02-database`. База кода второй лабораторной продолжает первую.

## После распаковки

```bash
git branch
git log --all --oneline --decorate
git switch lab-01-basic-api
git switch lab-02-database
```

## Публикация в GitHub

Создайте **пустой** репозиторий `web-labs-fastapi` на GitHub, затем выполните:

```bash
git remote add origin https://github.com/ВАШ_ЛОГИН/web-labs-fastapi.git
git push -u origin lab-01-basic-api
git push -u origin lab-02-database
```

При необходимости установите ветку `lab-02-database` основной в настройках GitHub.

Ссылка на GitHub появляется только после публикации; локальный архив не является опубликованным репозиторием.

Для запуска соответствующей лабораторной: `git switch <имя-ветки>`, `pip install -r requirements.txt`, `uvicorn app.main:app --reload`. Для ЛР2 скопируйте `.env.example` в `.env`.
