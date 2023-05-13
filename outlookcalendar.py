from exchangelib import DELEGATE, Account, Credentials, EWSDateTime, EWSTimeZone, CalendarItem
import re, getpass, sys
from datetime import datetime



"""TODO: 1. Add the functionality to read from a file and fill in the calendar. 
2. We can get chatgpt to directly output in the format readable in this code and 
save it in a file where it can be read and fill in the calendar

"""


class DateTimeStringParser():
    def parse_datetime_range(self, date_and_time: str, desc: str):
        tz = EWSTimeZone.localzone()
        datetime_range_regex = r'^(\w{3})\s+(\d{1,2}),\s+(\d{4})\s+from\s+(\d{1,2}):(\d{2})\s+(am|pm)\s+to\s+(\d{1,2}):(\d{2})\s+(am|pm)$'
        match = re.match(datetime_range_regex, date_and_time, re.IGNORECASE)
        if not match:
            raise ValueError(f'Invalid datetime range string: {date_and_time}\n{desc}')
            
        month_abbr = match.group(1)
        day = int(match.group(2))
        year = int(match.group(3))
        start_hour = int(match.group(4))
        start_minute = int(match.group(5))
        start_ampm = match.group(6).lower()
        end_hour = int(match.group(7))
        end_minute = int(match.group(8))
        end_ampm = match.group(9).lower()

        if start_ampm == 'pm' and start_hour != 12:
            start_hour += 12
        elif start_ampm == 'am' and start_hour == 12:
            start_hour = 0

        if end_ampm == 'pm' and end_hour != 12:
            end_hour += 12
        elif end_ampm == 'am' and end_hour == 12:
            end_hour = 0

        start = EWSDateTime(year, self.month_abbr_to_number(month_abbr), day, start_hour, start_minute, tzinfo=tz)
        end = EWSDateTime(year, self.month_abbr_to_number(month_abbr), day, end_hour, end_minute, tzinfo=tz)

        return (start, end)

    def month_abbr_to_number(self, month_abbr):
        months = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12,
        }
        return months.get(month_abbr.lower())

class MakeSchedule():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.credentials = Credentials(username=self.username, password=self.password)
        self.account = Account(primary_smtp_address=username, credentials=self.credentials, autodiscover=True, access_type=DELEGATE)

    def make_item(self, subject: str, start_time, end_time, body=None, location=None):
        tz = EWSTimeZone.localzone()

        item = CalendarItem(
        account=self.account,
        folder=self.account.calendar,
        subject=subject,
        start=start_time,
        end=end_time,
        body=body,
        location=location)


        item.save()



def main():

    desc = """Give the name of the entry/activity as the first param and the date and time ([Month] [Date], [Year] from [start time] am/pm to [end time] am/pm)"""


    try:
        subject = sys.argv[1]
        date_and_time = sys.argv[2]
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


if __name__ == "__main__":
    main()
