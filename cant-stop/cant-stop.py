

class GamePosition:
    cols = set(range(2, 13))
    col_height = {col: 13 - 2*abs(col - 7) for col in cols}

    def __init__(self, position: dict, temp_position: dict):
        self.open_cols = GamePosition.cols

    def close_col(self, col: int):
        self.open_cols.discard(col)
