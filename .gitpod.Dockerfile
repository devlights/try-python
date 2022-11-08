FROM gitpod/workspace-full:latest

USER gitpod

RUN pyenv install 3.10.7
RUN pyenv global 3.10.7
RUN python3 -m pip install poetry
RUN poetry install
