# try-python
This is my TUTORIAL project for python. 

![try-python - Python Version](https://img.shields.io/badge/python-3.14-blue.svg)

# Requirements
- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv)
  - Dependency management
- [Task](https://taskfile.dev/#/)
  - Task runner

# Python version

```sh
$ uv run python -V
Python 3.14.2
```

# Make Environment
```sh
$ uv sync
```

# REPL

```sh
$ task repl
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

# Type-Check

```sh
$ task typecheck
```

# Misc

- [try-python-extlib](https://github.com/devlights/try-python-extlib)
  - 姉妹プロジェクト. 外部ライブラリのサンプルなどがあります。
