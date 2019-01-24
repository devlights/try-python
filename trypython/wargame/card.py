# ---------------------------------------------------------
# 書籍「独学プログラマー Python言語の基本から仕事のやり方まで」 より写経
# ---------------------------------------------------------


class Card:
    suits = ('spades', 'hearts', 'diamonds', 'clubs',)
    values = (None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',)

    def __init__(self, value: int, suit: int):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit == other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return f'{self.values[self.value]} of {self.suits[self.suit]}'
