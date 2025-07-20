def provide_reminder(task_name, priority, time_sensitive):
    """
    Prints a customized reminder based on task details.

    Parameters:
    - task_name (str): The name of the task.
    - priority (str): The priority level (e.g., 'High', 'Medium', 'Low').
    - time_sensitive (bool): Whether the task requires immediate attention.
    """
    if time_sensitive:
        urgency = "This task requires immediate attention!"
    else:
        urgency = "This task can be scheduled later."

    print(f"Reminder: You need to complete '{task_name}'. Priority: {priority}. {urgency}")


# Example usage
provide_reminder("Submit assignment", "High", True)
