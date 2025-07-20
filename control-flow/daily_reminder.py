def provide_reminder(task, priority, time_bound):
    """
    Prints a customized reminder based on user input.

    Parameters:
    - task (str): The name of the task
    - priority (str): Task priority level (High, Medium, Low)
    - time_bound (str): 'yes' if task is time-sensitive, otherwise 'no'
    """
    urgent_message = "This task requires immediate attention!" if time_bound.lower() == 'yes' else "This task can be done later."

    match priority.lower():
        case 'high':
            print(f"Reminder: High priority task '{task}'. {urgent_message}")
        case 'medium':
            print(f"Reminder: Medium priority task '{task}'. {urgent_message}")
        case 'low':
            print(f"Reminder: Low priority task '{task}'. {urgent_message}")
        case _:
            print(f"Reminder: Task '{task}' with unknown priority. {urgent_message}")


# --- User prompts ---
task = input("Enter your task: ")
time_bound = input("Is the task time-bound? (yes/no): ")
priority = input("Enter priority level (High, Medium, Low): ")

# Call the function
provide_reminder(task, priority, time_bound)
