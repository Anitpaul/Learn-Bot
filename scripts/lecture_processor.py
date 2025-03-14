import pandas as pd
from datetime import datetime, timedelta

def load_lectures():
    """Loads lecture data from a file."""
    try:
        lectures = pd.read_csv("data/lecture_times.txt", names=["Lecture Name", "Duration (min)"])
        return lectures
    except FileNotFoundError:
        print("Error: lecture_times.txt not found.")
        return pd.DataFrame(columns=["Lecture Name", "Duration (min)"])
    except Exception as e:
        print(f"An error occurred while loading the lectures: {e}")
        return pd.DataFrame(columns=["Lecture Name", "Duration (min)"])

def assign_lectures(routine, lectures):
    """Assigns lectures to available study blocks in the routine."""
    study_blocks = routine[routine["Activity"].str.contains("Study")].copy()
    study_blocks["Start Time"] = pd.to_datetime(study_blocks["Start Time"], format="%H:%M")
    study_blocks["End Time"] = pd.to_datetime(study_blocks["End Time"], format="%H:%M")
    
    schedule = []
    lecture_index = 0
    
    for _, block in study_blocks.iterrows():
        start_time = block["Start Time"]
        end_time = block["End Time"]
        remaining_time = (end_time - start_time).total_seconds() / 60  # in minutes
        
        while lecture_index < len(lectures) and remaining_time > 0:
            lecture_duration = int(lectures.iloc[lecture_index]["Duration (min)"])  # Convert to int
            if lecture_duration <= remaining_time:
                schedule.append([start_time.strftime("%H:%M"), (start_time + timedelta(minutes=lecture_duration)).strftime("%H:%M"), lectures.iloc[lecture_index]["Lecture Name"]])
                start_time += timedelta(minutes=lecture_duration)
                remaining_time -= lecture_duration
                lecture_index += 1
            else:
                schedule.append([start_time.strftime("%H:%M"), (start_time + timedelta(minutes=remaining_time)).strftime("%H:%M"), lectures.iloc[lecture_index]["Lecture Name"] + " (Part 1)"])
                lectures.at[lecture_index, "Duration (min)"] -= remaining_time
                start_time += timedelta(minutes=remaining_time)
                remaining_time = 0
    
    # Add meal times and breaks to the schedule
    non_study_blocks = routine[~routine["Activity"].str.contains("Study")].copy()
    non_study_blocks["Start Time"] = pd.to_datetime(non_study_blocks["Start Time"], format="%H:%M")
    non_study_blocks["End Time"] = pd.to_datetime(non_study_blocks["End Time"], format="%H:%M")
    
    for _, block in non_study_blocks.iterrows():
        schedule.append([block["Start Time"].strftime("%H:%M"), block["End Time"].strftime("%H:%M"), block["Activity"]])
    
    # Sort the schedule by start time
    schedule_df = pd.DataFrame(schedule, columns=["Start Time", "End Time", "Lecture Name"])
    schedule_df["Start Time"] = pd.to_datetime(schedule_df["Start Time"], format="%H:%M")
    schedule_df = schedule_df.sort_values(by="Start Time")
    schedule_df["Start Time"] = schedule_df["Start Time"].dt.strftime("%H:%M")
    
    return schedule_df

def save_lectures(schedule):
    """Saves the updated lecture schedule to a CSV file."""
    try:
        schedule.to_csv("data/lectures.csv", index=False)
    except Exception as e:
        print(f"An error occurred while saving the schedule: {e}")

