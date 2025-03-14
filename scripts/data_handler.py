import pandas as pd

def load_routine():
    """Loads the daily routine from CSV."""
    try:
        routine = pd.read_csv("data/daily_routine.csv")
        return routine
    except FileNotFoundError:
        print("Error: daily_routine.csv not found.")
        return pd.DataFrame(columns=["Start Time", "End Time", "Activity"])
    except Exception as e:
        print(f"An error occurred while loading the routine: {e}")
        return pd.DataFrame(columns=["Start Time", "End Time", "Activity"])

def save_routine(routine):
    """Saves the updated routine back to CSV."""
    try:
        routine.to_csv("data/daily_routine.csv", index=False)
    except Exception as e:
        print(f"An error occurred while saving the routine: {e}")
