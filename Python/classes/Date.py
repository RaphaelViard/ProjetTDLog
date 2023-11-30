class Date:
    def __init__(self, date, event):
        self._date = date # day - month - year
        self._event = event

    ## property / setter

    @property
    def date(self):
        return self._date

    @property
    def event(self):
        return self._event

    @date.setter
    def set_date(self, new_date):
        self._date = new_date

    @event.setter
    def set_event(self, new_event):
        self._event = new_event

    def check_event(self, event_to_check):
        return event_to_check in self._event

    def withdraw_event(self, event_to_withdraw):
        if event_to_withdraw in self._event:
            self._event.remove(event_to_withdraw)

    def add_event(self, event_to_add):
        self._event.append(event_to_add)

    ### °°° other functions °°°



