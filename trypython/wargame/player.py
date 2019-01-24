# ---------------------------------------------------------
# 書籍「独学プログラマー Python言語の基本から仕事のやり方まで」 より写経
# ---------------------------------------------------------
import dataclasses

from wargame.card import Card


@dataclasses.dataclass
class Player:
    wins: int = 0
    card: Card = None
    name: str = ""
