import os
from typing import Iterable

from git import Repo


def create_commit(message: str, files: Iterable[str]):
    repo = Repo(os.getcwd())
    repo.index.add([os.path.abspath(filename) for filename in files])
    repo.index.commit(message)
