# webook-fastapi
REST backend solution in FastAPI for WeBook project

### Quick setup

1 - Install Python 3.9 (https://www.python.org/downloads/release/python-397/)

2 - Install Poetry (Poetry is a tool for dependency management and packaging in Python)

a - <a name="step-1">Reccomended installation (osx/linux/bashonwindows):</a>
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

b - <a name="step-1">Reccomended installation (windows powershell install instructions):</a>
```bash
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

3 - Create virtual environment

```bash
poetry env use /full/path/to/python
```

or (if python is in default path)

```bash
 poetry env use python
```
