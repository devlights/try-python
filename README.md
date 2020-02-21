# try-python
This is my TUTORIAL project for python. 

![try-python - Python Version](https://img.shields.io/badge/python-3.8-blue.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8b8bf44a6dbe40b5aa29e045a8494638)](https://www.codacy.com/manual/devlights/try-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=devlights/try-python&amp;utm_campaign=Badge_Grade)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/devlights/try-python) 

# Caution
I'm japanese. so some script include Japanese comments. :wink:

# Requirements
- Python 3.7 or higher (I'm using Python 3.8)

# Requirements (Optional)
- JetBrains PyCharm
- VisualStudio Code

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

# Run Examples
Each python scripts can be run individually.
- Launch from PyCharm

or

```sh
$ cd try-python
$ source .venv/bin/activate
$ python -m trypython
```

# VSCode settings (Example)

## settings.json

```json
{
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "python.pythonPath": "/path/to/python",
    "python.terminal.launchArgs": [
        "-B",
        "-c",
        "\"import IPython; IPython.start_ipython()\""
    ],
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "python.unitTest.pyTestEnabled": true,
    "python.linting.pydocstyleEnabled": false
}
```

## launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File (Integrated Terminal)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "pythonPath": "${config:python.pythonPath}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}",
                "PYTHONDONTWRITEBYTECODE": "1"
            }
        }
    ]
}
```

:smiley:
