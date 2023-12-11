from datetime import datetime, time, timedelta

date_format = "%Y-%m-%d"
hour_format = "%H:%M" # ne pas mettre les % en pratique
# -> date_string = date_object.strftime(date_format)
# -> date_object = datetime.strptime(date_string, date_format)

# créer une sous classe datevent

class Date :
    def __init__(self, date, hour=None):
        self._date = date # see date_format for format
        self._hour = hour # see hour_format for format

    ## property / setter

    @property
    def date(self):
        return self._date

    @property
    def hour(self):
        return self._hour

    @date.setter
    def date(self, new_date):
        try:
            date_object = datetime.strptime(new_date, "%Y-%m-%d")
            self._date = new_date
        except ValueError:
            print("Invalid date format.")

    @hour.setter
    def hour(self, new_hour):
        try:
            date_object = datetime.strptime(new_hour, "%H:%M")
            self._date = new_hour
        except ValueError:
            print("Invalid hour format.")

    ## display / conversion

    def to_datetime(self):
        day, month, year = map(int, self.date.split('-'))
        return datetime(year, month, day)

    def display_date(self):
       print(self.date)

    ## get

    def get_day(self):
        # Extract and return the day from the date
        return int(self.date.split('-')[2])

    def get_month(self):
        # Extract and return the month from the date
        return int(self.date.split('-')[1])

    def get_year(self):
        # Extract and return the year from the date
        return int(self._date.split('-')[0])

    def get_weekday(self):
        # Return the weekday of the date (Monday is 0 and Sunday is 6)
        day, month, year = map(int, self._date.split('-'))
        return datetime(year, month, day).weekday()

    ## info

    def days_in_month(self):
        # Return the number of days in the month of the date
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = self.get_month()
        if month == 2 and self.is_leap_year():
            return 29
        return month_days[month]

    def difference_in_days(self, other_date):
        # Calculate the difference in days between two dates
        date1 = datetime.strptime(self._date, date_format)
        date2 = datetime.strptime(other_date._date, date_format)
        return abs((date1 - date2).days)

    def days_until(self, future_date):
        # Calculate the number of days until a future date
        current_date = datetime.now()
        target_date = datetime.strptime(future_date._date, date_format)
        return max(0, (target_date - current_date).days)

    def months_until(self, future_date):
        # Calculate the number of months until a future date
        months_until = (future_date.get_year() - self.get_year()) * 12
        months_until += future_date.get_month() - self.get_month()
        return max(0, months_until)

    def days_until_month_end(self):
        # Calculate the number of days until the end of the month
        days_in_month = self.days_in_month()
        current_day = self.get_day()
        return days_in_month - current_day

    def days_since_month_start(self):
        # Calculate the number of days since the start of the month
        current_day = self.get_day()
        return current_day - 1

    ## verification

    def is_leap_year(self):
        # Check if the year in the date is a leap year
        year = self.get_year()
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def is_future(self):
        # Check if the date is in the future
        current_date = datetime.now()
        target_date = datetime.strptime(self._date, date_format)
        return target_date > current_date

    def is_weekend(self):
        # Check if the date falls on a weekend (Saturday or Sunday)
        weekday = self.get_weekday()
        return weekday == 5 or weekday == 6

    def is_same_date(self, other_date):
        # Check if two dates have the same day, month, and year
        return self._date == other_date._date

    def is_same_month(self, other_date):
        # Check if two dates are in the same month
        return self.get_month() == other_date.get_month() and self.get_year() == other_date.get_year()

    def is_same_year(self, other_date):
        # Check if two dates are in the same year
        return self.get_year() == other_date.get_year()

class DateEvent(Date):
        def __init__(self, date, hour=None, listev=[]):
            super().__init__(date, hour)
            self._event = listev

        @property
        def event(self):
            return self._event

        def check_event(self, event_to_check):
            return event_to_check in self._event

        def remove_event(self, event_to_remove):
            if event_to_remove in self._event:
                self._event.remove(event_to_remove)

        def add_event(self, event_to_add):
            self._event.append(event_to_add)

        ## Display

        def __str__(self):
            event_names = [event.name for event in self.event]
            return f"Date: {self.date}, Events: {', '.join(event_names) if event_names else 'None'}"

    ### °°° other functions °°°