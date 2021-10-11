# try-python
This is my TUTORIAL project for python. 

![try-python - Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/devlights/try-python/badge)](https://www.codefactor.io/repository/github/devlights/try-python)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/devlights/try-python) 

# Requirements
- Python 3.9 or higher

```sh
$ python3
Python 3.10.0 (default, Oct  8 2021, 04:49:46) [GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

# Make Environment
```sh
$ cd try-python
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -U -r requirements-dev.txt
```

# Unit Test
```sh
$ cd try-python
$ source .venv/bin/activate
$ pytest
```

# Launch

```sh
$ cd try-python
$ source .venv/bin/activate
$ python -m trypython
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
