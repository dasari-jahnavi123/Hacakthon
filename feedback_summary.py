def feedback_summary(feedback_list):
    summary = f"Total Feedbacks: {len(feedback_list)}\n"
    summary += "Feedback Entries:\n"
    for fb in feedback_list:
        summary += f"- {fb}\n"
    return summary
