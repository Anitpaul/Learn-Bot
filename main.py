import pandas as pd
from datetime import datetime, timedelta
import scripts.data_handler as data_handler
import scripts.lecture_processor as lecture_processor
import sys
from cui.cui import main_menu  # Import the main_menu function from your CUI script

def main():
    print("LearnBot: Processing your study schedule...")

    # Load data using imported modules
    routine = data_handler.load_routine()
    print("Routine loaded:", routine)
    
    lectures = lecture_processor.load_lectures()
    print("Lectures loaded:", lectures)

    # Process and assign lectures
    schedule = lecture_processor.assign_lectures(routine, lectures)
    print("Schedule generated:", schedule)
    
    # Save final schedule
    lecture_processor.save_lectures(schedule)
    print("Lecture schedule updated in data/lectures.csv")

    # Launch the CUI
    main_menu()

if __name__ == "__main__":
    main()
