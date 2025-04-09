from search_feedback import search_feedback

def test_search_feedback():
    feedback_list = ["Alice: Good", "Bob: Average", "Alice: Excellent"]
    result = search_feedback(feedback_list, "Alice")
    assert result == ["Alice: Good", "Alice: Excellent"]
