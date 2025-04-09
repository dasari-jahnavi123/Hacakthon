from score_calculator import average_score

def test_average_score():
    assert average_score([10, 20, 30]) == 20
    assert average_score([]) == 0
