from src.model.Game import InvalidMove_Error
from src.utils.Move import Move


def call_method_on_each(arr, method, *args):  # via stackoverflow.com/a/2682075/2474159
    for obj in arr:
        getattr(obj, method)(*args)


def str2move(loc: str, board_size) -> Move:
    if not str:
        return Move(is_pass=True)
    col = _chr2ord(loc[0], board_size)
    row = _chr2ord(loc[1], board_size)
    return Move(col, row)


def _chr2ord(c: str, board_size) -> int:
    idx = ord(c) - ord('a')
    if idx < 0 or idx >= board_size:
        raise InvalidMove_Error(
            c + '=' + str(idx) +
            ' is an invalid row/column index, board size is ' +
            str(board_size))
    return idx
