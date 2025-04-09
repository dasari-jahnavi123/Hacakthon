from feedback_summary import feedback_summary

def test_feedback_summary():
    feedbacks = ['Good', 'Excellent']
    result = feedback_summary(feedbacks)
    assert "Total Feedbacks: 2" in result
    assert "- Good" in result
    assert "- Excellent" in result
