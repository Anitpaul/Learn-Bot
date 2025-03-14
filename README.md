# LearnBot

## Overview
LearnBot processes lecture times, adjusts them based on playback speed, adds note-taking time, and integrates them into a structured study plan.

## 🔧 Installation

1. **Clone the repository** (or download the ZIP):
   ```sh
   git clone https://github.com/AnitPaul/LearnBot.git
   cd LearnBot

## Setup
2. Install dependencies:
    ```sh
    pip install -r requirements.txt

3. Place lecture durations in `data/lecture_times.txt` (format: `duration,speed`).
4. Run the program:
    ```sh
    python main.py

5. Check `data/lectures.csv` for the updated schedule.

## Features
- Reads lecture durations and playback speed.
- Calculates adjusted time and adds note-taking time.
- Saves the structured schedule to `lectures.csv`.

## Future Updates
- Calendar integration
- Adaptive scheduling based on study patterns
