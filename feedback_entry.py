def collect_feedback():
    feedback_list = []
    while True:
        feedback = input("Enter student feedback (or type 'done' to finish): ")
        if feedback.lower() == 'done':
            break
        feedback_list.append(feedback)
    return feedback_list
