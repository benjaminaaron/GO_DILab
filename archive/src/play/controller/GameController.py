import threading

from Game import InvalidMove_Error


class GameController(threading.Thread):

    def __init__(self, game, view, player1, player2):
        threading.Thread.__init__(self)
        self.game = game
        self.view = view
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def next_turn(self):
        # swap player1 and player2
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def run(self):
        self.game.start()

        while self.game.is_running:
            self.view.show_player_turn_start(self.current_player.name)
            # loop until a move is valid
            # (can lead to inf-loops when bots fail to produce valid moves)
            while True:
                try:
                    move = self.current_player.get_move()
                    if move is not None:
                        self.game.play(move, self.current_player.color)
                        break
                except InvalidMove_Error as e:
                    self.view.show_error(' '.join(e.args))
            self.view.show_player_turn_end(self.current_player.name)
            self.next_turn()

        # TODO
        # relieve the Game-class from the task to print end-of-game
        # things, view must do this: self.view.show_game_ended()
