class Lieu:
    def __init__(self, place, event):
        self._place = place # country - city
        self._event = event

    ## property / setter

    @property
    def place(self):
        return self._place

    @property
    def event(self):
        return self._event

    @place.setter
    def set_place(self, new_place):
        self._place = new_place

    @event.setter
    def set_event(self, new_event):
        self._event = new_event

    def withdraw_event(self, event_to_withdraw):
        if event_to_withdraw in self._event:
            self._event.remove(event_to_withdraw)

    def add_event(self, event_to_add):
        self._event.append(event_to_add)

    ### °°° other functions °°°



