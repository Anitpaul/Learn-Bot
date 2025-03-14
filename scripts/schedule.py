import pandas as pd
from datetime import datetime, timedelta
from scripts.lecture_processor import load_lectures, save_lectures
from scripts.data_handler import load_routine

# Assign lectures to study sessions
def assign_lectures(routine, lectures):
    study_blocks = routine[routine["Activity"].str.contains("Study")].copy()
    study_blocks["End Time"] = pd.to_datetime(study_blocks["Start Time"], format="%H:%M") + pd.to_timedelta(study_blocks["Duration (min)"], unit='m')
    
    schedule = []
    lecture_index = 0
    
    for _, block in study_blocks.iterrows():
        start_time = pd.to_datetime(block["Start Time"], format="%H:%M")
        end_time = pd.to_datetime(block["End Time"], format="%H:%M")
        
        while lecture_index < len(lectures) and start_time < end_time:
            duration = timedelta(minutes=lectures.iloc[lecture_index]["Duration (min)"])
            if start_time + duration <= end_time:
                schedule.append((start_time.strftime("%H:%M"), (start_time + duration).strftime("%H:%M"), lectures.iloc[lecture_index]["Lecture Name"]))
                start_time += duration
                lecture_index += 1
            else:
                break
    return pd.DataFrame(schedule, columns=["Start Time", "End Time", "Lecture Name"])

def generate_schedule():
    routine = load_routine()
    print("Routine loaded:", routine)  # Debug print statement
    lectures = load_lectures()
    print("Lectures loaded:", lectures)  # Debug print statement
    schedule = assign_lectures(routine, lectures)
    print("Schedule generated:", schedule)  # Debug print statement
    save_lectures(schedule)
    print("Lecture schedule updated in data/lectures.csv")

if __name__ == "__main__":
    generate_schedule()
