# ---------------------------------------------------------
# 書籍「独学プログラマー Python言語の基本から仕事のやり方まで」 より写経
# ---------------------------------------------------------
from wargame.card import Card
from wargame.deck import Deck
from wargame.player import Player


# noinspection PyMethodMayBeStatic
class Game:
    def __init__(self):
        self._deck: Deck = Deck()
        self._p1: Player = None
        self._p2: Player = None

    def _wins(self, winner: Player):
        print(f'{winner.name}の勝ち')

    def _draw(self, p1n: str, p1c: Card, p2n: str, p2c: Card):
        print(f'{p1n} は {p1c}, {p2n} は {p2c} を引いた')

    def _winner(self, p1: Player, p2: Player) -> str:
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け'

    def play(self):
        name1 = input('プレーヤー１の名前：')
        name2 = input('プレーヤー２の名前：')

        print('ゲーム開始')

        self._p1 = Player(name=name1)
        self._p2 = Player(name=name2)

        cards = self._deck.cards
        while len(cards) >= 2:
            res = input('q: 終了, それ以外のキーでplay:')
            if res == 'q':
                break

            p1c = self._deck.remove_card()
            p2c = self._deck.remove_card()
            p1n = self._p1.name
            p2n = self._p2.name

            self._draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self._p1.wins += 1
                self._wins(self._p1)
            else:
                self._p2.wins += 1
                self._wins(self._p2)

        win = self._winner(self._p1, self._p2)
        print(f'ゲーム終了 {win} の勝ち')
