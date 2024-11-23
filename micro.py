import time
from datetime import datetime, timedelta

def countdown_clock():
    """Countdown Clock: User inputs target time in hours, minutes, and seconds."""
    print("\nSet your countdown clock:")
    try:
        hours = int(input("Enter target hours (0-23): "))
        minutes = int(input("Enter target minutes (0-59): "))
        seconds = int(input("Enter target seconds (0-59): "))
        
        now = datetime.now()
        target_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        
        if target_time <= now:
            target_time += timedelta(days=1)  # Set for the next day if time is earlier
        
        print(f"Countdown clock set for {target_time.strftime('%H:%M:%S')}.")
        while datetime.now() < target_time:
            remaining = target_time - datetime.now()
            hrs, rem = divmod(remaining.seconds, 3600)
            mins, secs = divmod(rem, 60)
            print(f"Time left: {hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
        print("\nTime's up!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def countdown_timer():
    """Countdown Timer: User inputs hours, minutes, and seconds."""
    print("\nSet your countdown timer:")
    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        print("Countdown timer started!")
        
        while total_seconds:
            hrs, rem = divmod(total_seconds, 3600)
            mins, secs = divmod(rem, 60)
            print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            total_seconds -= 1
        print("\nTime's up!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def main():
    """Menu for Countdown Clock and Timer."""
    while True:
        print("\nChoose an option:")
        print("1. Countdown Clock (to a specific time)")
        print("2. Countdown Timer (for a duration)")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            countdown_clock()
        elif choice == "2":
            countdown_timer()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
