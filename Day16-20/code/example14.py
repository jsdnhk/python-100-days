"""
面向對象
枚舉 - 一個變量的值只有有限個選擇，最適合的類型就是枚舉
通過枚舉我們可以定義符號常量，符號常量優於字面常量
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """花色（枚舉）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """撲克"""
    
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """發牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """是否有更多的牌"""
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """主函數"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('東邪'), Player('西毒'), 
        Player('南帝'), Player('北丐')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()
