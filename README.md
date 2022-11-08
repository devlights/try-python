# try-python
This is my TUTORIAL project for python. 

![try-python - Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/devlights/try-python/badge)](https://www.codefactor.io/repository/github/devlights/try-python)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/devlights/try-python) 

# Requirements
- Python 3.10 or higher
- [Poetry](https://python-poetry.org/)
  - Dependency management
- [Task](https://taskfile.dev/#/)
  - Task runner

# Python version

```sh
$ poetry run python -V
Python 3.10.7

$ poetry env info

Virtualenv
Python:         3.10.7
Implementation: CPython
Path:           /workspace/.pyenv_mirror/poetry/virtualenvs/try-python-M1FUJLyv-py3.10
Executable:     /workspace/.pyenv_mirror/poetry/virtualenvs/try-python-M1FUJLyv-py3.10/bin/python
Valid:          True

System
Platform:   linux
OS:         posix
Python:     3.10.7
Path:       /home/gitpod/.pyenv/versions/3.10.7
Executable: /home/gitpod/.pyenv/versions/3.10.7/bin/python3.10
```

# Make Environment
```sh
$ poetry install
$ poetry lock
```

# REPL

```sh
$ task repl
task: [repl] poetry run python
Python 3.10.7 (main, Nov  8 2022, 08:35:33) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.system("which python")
/workspace/.pyenv_mirror/poetry/virtualenvs/try-python-M1FUJLyv-py3.10/bin/python
0
```

# Launch

```sh
$ task run
```

# Unit Test

```sh
$ task test
```

# Format

```sh
$ task fmt
```

# Lint

```sh
$ task lint
```

# Mypy

```sh
$ task mypy
```

# VSCode settings (Example)

## settings.json

```json
{
    "python.defaultInterpreterPath": "python",
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "python.linting.pydocstyleEnabled": true,
    "python.terminal.launchArgs": [
        "-B",
        "-c",
        "\"import IPython; IPython.start_ipython()\""
    ]
}
```

## launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "try-python",
            "type": "python",
            "request": "launch",
            "module": "trypython",
            "pythonArgs": [
                "-X", "dev",
                "-X", "tracemalloc=10"
            ],
            "env": {
                "PYTHONDONTWRITEBYTECODE": "1"
            }
        }
    ]
}
```

# Misc

- [try-python-extlib](https://github.com/devlights/try-python-extlib)
  - 姉妹プロジェクト. 外部ライブラリのサンプルなどがあります。
