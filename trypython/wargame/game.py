# ---------------------------------------------------------
# 書籍「独学プログラマー Python言語の基本から仕事のやり方まで」 より写経
#
# すこし改変
# ---------------------------------------------------------
from trypython.wargame.deck import Deck
from trypython.wargame.player import Player


class Game:
    def __init__(self):
        self._deck: Deck = Deck()
        self._p1: Player = None
        self._p2: Player = None

    @staticmethod
    def _wins(p1: Player, p2: Player) -> Player:
        if p1.card > p2.card:
            p1.wins += 1
            return p1
        else:
            p2.wins += 1
            return p2

    @staticmethod
    def _draw(deck: Deck, p1: Player, p2: Player):
        p1.card = deck.take()
        p2.card = deck.take()
        print(f'{p1.name} は {p1.card}, {p2.name} は {p2.card} を引いた')

    @staticmethod
    def _winner(p1: Player, p2: Player):
        wins_status = f'{p1.name}[{p1.wins}] {p2.name}[{p2.wins}]'
        if p1.wins > p2.wins:
            print(f'ゲーム終了 {p1.name} の勝ち {wins_status}')
        elif p1.wins < p2.wins:
            print(f'ゲーム終了 {p2.name} の勝ち {wins_status}')
        else:
            print(f'引き分け {wins_status}')

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
            self._draw(self._deck, self._p1, self._p2)
            winner = self._wins(self._p1, self._p2)
            print(f'{winner.name}の勝ち')

        self._winner(self._p1, self._p2)
