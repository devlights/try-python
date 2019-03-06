# try-python
This is my TUTORIAL project for python. (python 3.7) 

# Caution
I'm japanese. so some script include Japanese comments. :wink:

# Requirements
- Python 3.7 or higher

# Requirements (Optional)
- JetBrains PyCharm
- VisualStudio Code

# Make Environment
```sh
$ cd try-python
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements-dev.txt
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
$ python -m trypython.xxx.xxx
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
