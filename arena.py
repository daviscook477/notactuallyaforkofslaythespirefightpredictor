import logging

from tqdm import tqdm

log = logging.getLogger(__name__)


class Arena():
    """
    An Arena class where an agent plays
    """

    def __init__(self, player, game, display=None):
        """
        Input:
            player: function that takes board as input, return action
            game: Game object
            display: a function that takes board as input and prints it (e.g.
                     display in othello/OthelloGame). Is necessary for verbose
                     mode.
        see othello/OthelloPlayers.py for an example. See pit.py for pitting
        human players/other baselines with each other.
        """
        self.player = player
        self.game = game
        self.display = display

    def playGame(self, verbose=False):
        """
        Executes one episode of a game.
        Returns:
            winner: (1 if won, -1 if lost)
        """
        board = self.game.getInitBoard()
        it = 0
        while self.game.getGameEnded(board) == 0:
            it += 1
            if verbose:
                assert self.display
                print("Turn ", str(it))
                self.display(board)
            action = self.player(board)

            valids = self.game.getValidMoves(board)

            if valids[action] == 0:
                log.error(f'Action {action} is not valid!')
                log.debug(f'valids = {valids}')
                assert valids[action] > 0
            board = self.game.getNextState(board, action)
        if verbose:
            assert self.display
            print("Game over: Turn ", str(it), "Result ", str(self.game.getGameEnded(board)))
            self.display(board)
        return self.game.getGameEnded(board)

    def playGames(self, num, verbose=False):
        """
        Plays num games
        Returns:
            won: games won
            lost: games lost
        """

        won = 0
        lost = 0
        for _ in tqdm(range(num), desc="Arena.playGames (1)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == 1:
                won += 1
            elif gameResult == -1:
                lost += 1
            else:
                log.error(f'Game result {gameResult} is not valid! Must be either a win or lose!')

        return won, lost