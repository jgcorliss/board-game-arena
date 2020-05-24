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
