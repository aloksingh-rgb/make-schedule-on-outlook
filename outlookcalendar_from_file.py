from outlookcalendar import DateTimeStringParser, MakeSchedule
import getpass
import os
import pandas as pd

desc =  """Give the name of the entry/activity as the first param and the date and time \n ([Month] [Date], [Year] from [start time] am/pm to [end time] am/pm)"""
choice = input("Press 1: to input individual calendar items.\nPress 2: to select a file to input calendar items.\nYour Choice: ")

if choice == "1":
    
    try:
        subject = input("Activity Name: ")
        date_and_time = input("Date and Time: ")
    except:
        print("arguments missing")
        print(desc)
        exit(-1)

    
    username = "aloksingh2012@outlook.com"
    password = getpass.getpass()


    dtsp = DateTimeStringParser()
    makesch = MakeSchedule(username, password)
    start_time, end_time = dtsp.parse_datetime_range(date_and_time, desc)
    makesch.make_item(subject, start_time, end_time)

elif choice == "2":
    FILE_PATH = input("File Path: ")
    if os.path.exists(FILE_PATH):
        pass
    else:
        raise FileNotFoundError("File doesnot exists")
        exit(-1)
    
    activities = pd.read_csv(FILE_PATH, sep=",", engine='python')

    username = "aloksingh2012@outlook.com"
    password = getpass.getpass()

    for activity, date_and_time in zip(activities["activity_names"], activities["date_and_time"]):

        dtsp = DateTimeStringParser()
        makesch = MakeSchedule(username, password)
        start_time, end_time = dtsp.parse_datetime_range(date_and_time, desc)
        makesch.make_item(activity, start_time, end_time)
    