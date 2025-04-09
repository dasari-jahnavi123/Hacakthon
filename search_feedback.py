def search_feedback(feedback_list, student_name):
    return [feedback for feedback in feedback_list if student_name.lower() in feedback.lower()]
