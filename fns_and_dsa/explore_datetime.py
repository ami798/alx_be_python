from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date(days_to_add: int):
    now = datetime.now()
    future = now + timedelta(days=days_to_add)
    future_date = future.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return
    calculate_future_date(days)

if __name__ == "__main__":
    main()
