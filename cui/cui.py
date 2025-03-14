import os
import time
import sys
import pandas as pd
import scripts.data_handler as data_handler
import scripts.lecture_processor as lecture_processor
from tabulate import tabulate

# ANSI color codes
RESET = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    clear_screen()
    print(f"{BLUE}============================{RESET}")
    print(f"{GREEN}      LearnBot CLI v1.0      {RESET}")
    print(f"{BLUE}============================{RESET}\n")

def main_menu():
    while True:
        print_banner()
        print(f"{YELLOW}1.{RESET} Generate Study Schedule")
        print(f"{YELLOW}2.{RESET} View Existing Schedule")
        print(f"{YELLOW}3.{RESET} Exit\n")
        
        choice = input(f"{GREEN}Enter your choice: {RESET}")
        
        if choice == "1":
            generate_schedule()
        elif choice == "2":
            view_schedule()
        elif choice == "3":
            print(f"{RED}Exiting LearnBot...{RESET}\n")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}\n")
            time.sleep(1)

def generate_schedule():
    print(f"{BLUE}\nGenerating your study schedule...{RESET}\n")
    time.sleep(1)
    
    routine = data_handler.load_routine()
    lectures = lecture_processor.load_lectures()
    schedule = lecture_processor.assign_lectures(routine, lectures)
    lecture_processor.save_lectures(schedule)
    
    print(f"{GREEN}Schedule successfully updated in data/lectures.csv{RESET}\n")
    input("Press Enter to return to the main menu...")

def view_schedule():
    print(f"{BLUE}\nYour Scheduled Lectures:{RESET}\n")
    
    try:
        schedule = pd.read_csv("data/lectures.csv")

        # Ensure the DataFrame isn't empty
        if schedule.empty:
            print(f"{RED}No lectures scheduled! Please generate one first.{RESET}\n")
        else:
            print(tabulate(schedule, headers=schedule.columns, tablefmt="fancy_grid", showindex=False))
    
    except FileNotFoundError:
        print(f"{RED}No schedule found! Please generate one first.{RESET}\n")
    except pd.errors.EmptyDataError:
        print(f"{RED}The schedule file is empty! Please generate a schedule first.{RESET}\n")
    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}\n")
    
    input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()