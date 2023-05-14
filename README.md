# Outlook Calendar Automation
This project is designed to automate the process of creating calendar events in Microsoft Outlook. 
# Requirements
- Python 3.6 or later
- pandas ()
- exchangelib ()
# Installation
1. Clone or download this repository to your local machine.
```
   git clone https:https://github.com/aloksingh-rgb/make-schedule-on-outlook.git
   ```
2. Open a terminal or command prompt in the project directory.
3. Install the required packages using the following command:
```
    pip install -r requirements.txt
```
# Usage
There are two Python scripts included in this project:

- outlookcalendar.py: Allows you to manually input the details of a calendar event (activity name, date and time) and create it in Outlook.
- outlookcalendar_from_file.py: Allows you to create multiple calendar events at once by reading the details from a CSV file. Also, you can choose other options by following the prompts.

# Note
The date and time format for the date_and_time column in the CSV file should be as follows: [Month] [Date], [Year] from [start time] am/pm to [end time] am/pm. For example: May 25, 2023 from 9:00 am to 10:00 am.
