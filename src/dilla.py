import chess
import chess.uci

engine = chess.uci.popen_engine("/usr/local/bin/stockfish")
engine.uci()
board = chess.Board()

command = ""

def print_pos():
    print(board)

def eval_pos(args = 10):
    engine.position(board)
    res = engine.go(depth = args)
    print(board.san(res[0]))

def go_back():
    board.pop()

def move_list():
    board2 = chess.Board()
    print(board2.variation_san(board.move_stack))

actions = { ".p": print_pos, ".e": eval_pos, ".u": go_back, ".m": move_list }

while command != ".q":
    try:
        command = input("> ")
    except EOFError:
        break
    c = command.split(" ",1)
    if c[0] in actions:
        if len(c) > 1:
            actions[c[0]](c[1])
        else:
            actions[c[0]]()
    else:
        try:
            board.parse_san(c[0])
            board.push_san(c[0])
        except ValueError:
            pass


