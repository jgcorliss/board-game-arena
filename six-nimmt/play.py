class Game:
    def __init__(self, num_players: int, start_cards: list, my_cards: set):
        msg = 'Invalid starting cards'
        assert (isinstance(start_cards, list) and len(start_cards) == 4 and
                all(map(is_valid_card, start_cards))), msg
        msg = 'Invalid collection of cards for your hand'
        assert isinstance(my_cards, set) and all(map(is_valid_card, my_cards)), msg

        self.cards = [[k] for k in start_cards]
        self.num_players = num_players
        self.scores = self.num_players * [66]
        self.deck = set(range(1, 105)) - set(start_cards)
        self.my_cards = my_cards

    def update_scores(self, new_scores) -> None:
        msg = 'Invalid list of new scores'
        assert (isinstance(new_scores, list) and len(new_scores) == self.num_players and
                all(map(is_valid_score, new_scores))), msg
        self.scores = new_scores

    def replace_row(self, card: int, row_num: int) -> None:
        assert is_valid_card(card), 'Invalid card'
        assert is_valid_row_num(row_num), 'Invalid row number'
        self.cards[row_num - 1] = [card]

    def add_cards(self, new_cards: set) -> None:
        msg = 'Invalid collection of new cards'
        assert isinstance(new_cards, set) and all(map(is_valid_card, new_cards)), msg
        self.deck -= new_cards
        new_cards = sorted(new_cards)
        for new_card in new_cards:
            dest_row_num = None
            dest_end_card = None
            for row_num in range(1, 5):
                end_card = self.cards[row_num - 1][-1]
                if (end_card < new_card and
                        (end_card > dest_end_card or dest_end_card is None)):
                    dest_row_num = row_num
                    dest_end_card = end_card
            if dest_row_num is None:
                replace_row = int(input(f"New card {new_card} must replace a current"
                                        f" row. Which row? "))
                self.replace_row(card=new_card, row_num=replace_row)
            elif len(self.cards[dest_row_num]) == 5:
                self.cards[dest_row_num] = [new_card]
            else:
                self.cards[dest_row_num].append(new_card)


def bulls(card: int) -> int:
    if card % 55 == 0:
        return 7
    elif card % 11 == 0:
        return 5
    elif card % 10 == 0:
        return 3
    elif card % 5 == 0:
        return 2
    else:
        return 1


def is_valid_score(score) -> bool:
    return isinstance(score, int) and (score <= 66)


def is_valid_card(card) -> bool:
    return isinstance(card, int) and (1 <= card <= 104)


def is_valid_row_num(row) -> bool:
    return isinstance(row, int) and (1 <= row <= 4)


if __name__ == '__main__':
    pass
