FROM gitpod/workspace-full:latest

USER gitpod

RUN pyenv install 3.10.7 \
    && pyenv global 3.10.7 \
    && python3 -m pip install poetry \
    && poetry install