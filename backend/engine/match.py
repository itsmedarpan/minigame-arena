WINS_NEEDED = 2

class Match:
    def __init__(self, player_a, player_b):
        self.players = {player_a, player_b}
        self.scores = {player_a: 0, player_b: 0}
        self.status = "in_progress"
        self.winner = None
        self.current_game = None
        self.rounds = []

    def start_next_round(self, game_id):
        if self.status == "finished":
            raise ValueError("Match is already finished")
        if self.current_game is not None:
            raise ValueError("a round is already in progress")
        self.current_game = game_id

    def record_round_result(self, winner):
        if self.current_game is None:
            raise ValueError("no round is in progress")
        if winner is not None and winner not in self.scores:
            raise ValueError("unknown player")

        self.rounds.append({
            "number": len(self.rounds) + 1,
            "game": self.current_game,
            "winner":winner,
        })

        self.current_game = None

        if winner is None:
            return

        self.scores[winner] += 1
        if self.scores[winner] == WINS_NEEDED:
            self.status = "finished"
            self.winner = winner


    def is_finished(self):
        return self.status == "finished"
