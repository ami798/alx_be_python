# daily_reminder.py

# Prompt for task
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ")

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ")

# Process using match-case (Python 3.10+)
match priority.lower():
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Use if statement to adjust message if task is time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    if priority.lower() == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the customized reminder
print(message)
