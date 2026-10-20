import pytest
from engine.match import Match


def new_match():
    return Match("alice", "bob")

def play(match, winner, game="tictactoe"):
    match.start_next_round(game)
    match.record_round_result(winner)



def test_new_match_starts_at_zero():
    m = new_match()
    assert m.scores == {"alice": 0, "bob":0}
    assert m.status == "in_progress"


def test_round_win_adds_a_point():
    m = new_match()
    play(m, "alice")
    assert m.scores["alice"] == 1
    assert m.scores["bob"] == 0
    assert not m.is_finished()

def test_draw_changes():
    m = new_match()
    play(m, None)
    assert m.scores == {"alice": 0, "bob": 0}
    m.start_next_round("rps")

def test_two_wins_finishes_match():
    m = new_match()
    play(m, "alice")
    play(m, "alice")
    assert m.is_finished()
    assert m.winner == "alice"
    assert m.scores["alice"] == 2


def test_match_can_end_two_to_one():
    m = new_match()
    play(m, "alice")
    play(m, "bob")
    play(m, "alice")
    assert m.winner == "alice"
    assert m.scores == {"alice": 2, "bob": 1}


def test_cannot_start_round_after_match_finished():
    m = new_match()
    play(m, "alice")
    play(m, "alice")
    with pytest.raises(ValueError):
        m.start_next_round("tictactoe")


def test_cannot_record_result_without_active_round():
    m = new_match()
    with pytest.raises(ValueError):
        m.record_round_result("alice")

    
