from feedback_entry import collect_feedback

def test_collect_feedback(monkeypatch):
    inputs = iter(['Good', 'Excellent', 'done'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert collect_feedback() == ['Good', 'Excellent']
