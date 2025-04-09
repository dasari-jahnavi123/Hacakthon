from count_feedback import count_feedback

def test_count_feedback():
    feedback_list = ["Alice: Good", "Bob: Average", "Charlie: Excellent"]
    assert count_feedback(feedback_list) == 3
