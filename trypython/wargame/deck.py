# ---------------------------------------------------------
# 書籍「独学プログラマー Python言語の基本から仕事のやり方まで」 より写経
# ---------------------------------------------------------
import random
from typing import List, Optional

from wargame.card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self._make_cards()

    def _make_cards(self):
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def remove_card(self) -> Optional[Card]:
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
