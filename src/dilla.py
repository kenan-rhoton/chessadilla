import chess
import chess.uci
import shutil

engine = chess.uci.popen_engine(shutil.which("stockfish"))
engine.uci()
board = chess.Board()
info_handler = chess.uci.InfoHandler()
engine.info_handlers.append(info_handler)
engine.position(board)
engine.go(depth=10)

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

def score_pos():
    print(info_handler.info["score"][1])


actions = { ".p": print_pos, ".e": eval_pos, ".u": go_back, ".m": move_list, ".s": score_pos }

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


