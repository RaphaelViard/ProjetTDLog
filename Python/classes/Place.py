from datetime import datetime

class Place:
    def __init__(self, place, event):
        self._place = place # country-city
        self._event = []

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

    ## display

    def __str__(self):
        return f"Place: {self._place}, Events: {[event.name for event in self._events]}"

    ## verification

    def is_same_place(self, other_place):
        return self._place == other_place._place

    def has_event(self, event_to_check):
        return event_to_check in self._events

    def is_popular_location(self):
        return len(self._events) > 5

    def is_event_conflicting(self, other_place):
        return any(event in other_place._events for event in self._events)

    ## operation

    def merge_places(self, other_place):
        merged_place = Place(self._place)
        merged_place._events = self._events + other_place._events
        return merged_place

    def remove_past_events(self):
        current_date = datetime.now()
        self._event = [event for event in self._event if event.date.to_datetime() > current_date]

    def remove_duplicate_events(self):
        self._events = list(set(self._events))

    ## info events

    # name

    def find_events_by_info_keyword(self, keyword):
        # Return a list of events containing a specified keyword in their information
        keyword_events = [event for event in self._events if keyword.lower() in event.info.lower()]
        return keyword_events

    def events_starting_with(self, prefix):
        return [event for event in self._events if event.name.startswith(prefix)]

    def average_event_length(self):
        if not self._events:
            return 0
        total_length = sum(len(event.name) for event in self._events)
        return total_length / len(self._events)

    def find_event_by_name(self, event_name):
        # Find and return the first event with a matching name
        for event in self._events:
            if event.name == event_name:
                return event
        return None

    def get_event_names(self):
        # Return a list of names of events associated with the place
        return [event.name for event in self._events]

    # time

    def common_event(self, other_place):
        common_events = list(set(self._events) & set(other_place._events))
        return common_events[0] if common_events else None

    def upcoming_events(self, num_events=3):
        sorted_events = sorted(self._events, key=lambda event: event.date)
        return sorted_events[:num_events]

    def most_common_event(self):
        if not self._events:
            return None
        return max(set(self._events), key=self._events.count)

    def get_total_events(self):
        # Return the total number of events associated with the place
        return len(self._events)

    def events_in_future(self):
        # Return a list of events that are scheduled for the future
        current_date = datetime.now()
        future_events = [event for event in self._events if event.date.to_datetime() > current_date]
        return future_events

    def upcoming_events_by_category(self, num_events=3):
        # Get a dictionary with categories as keys and a list of upcoming events in each category as values
        upcoming_events_by_category = {}
        sorted_events = sorted(self._events, key=lambda event: event.date.to_datetime())

        for event in sorted_events[:num_events]:
            category = event.category
            if category not in upcoming_events_by_category:
                upcoming_events_by_category[category] = []
            upcoming_events_by_category[category].append(event)

        return upcoming_events_by_category

    def find_events_by_date_range(self, start_date, end_date):
        # Return a list of events scheduled within a specified date range
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")
        end_datetime = datetime.strptime(end_date, "%d-%m-%Y")
        range_events = [event for event in self._events if start_datetime <= event.date.to_datetime() <= end_datetime]
        return range_events

    def average_event_duration(self):
        # Calculate the average duration of events in hours
        if not self._events:
            return 0
        total_duration = sum(event.duration for event in self._events)
        return total_duration / len(self._events)

    def find_events_by_hour_range(self, start_hour, end_hour):
        # Return a list of events scheduled within a specified hour range
        hour_range_events = [event for event in self._events if start_hour <= event.hour < end_hour]
        return hour_range_events

    def events_between_dates(self, start_date, end_date):
        # Return a list of events scheduled between two dates
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")
        end_datetime = datetime.strptime(end_date, "%d-%m-%Y")
        selected_events = [event for event in self._events if
                           start_datetime <= event.date.to_datetime() <= end_datetime]
        return selected_events

    def get_event_dates(self):
        # Return a list of dates for events associated with the place
        return [event.date.to_string() for event in self._events]

    def sort_events_by_date(self, reverse=False):
        # Sort events based on their date
        self._events.sort(key=lambda event: event.date.to_datetime(), reverse=reverse)

    def events_in_month(self, target_month):
        # Return a list of events scheduled for a specific month
        month_events = [event for event in self._events if event.date.get_month() == target_month]
        return month_events

    # category

    def find_events_by_category(self, category):
        # Return a list of events belonging to a specific category
        category_events = [event for event in self._events if event.category == category]
        return category_events

    def most_popular_category(self):
        # Find the most popular event category based on the number of events
        if not self._events:
            return None
        category_count = {}
        for event in self._events:
            category = event.category
            category_count[category] = category_count.get(category, 0) + 1
        most_popular_category = max(category_count, key=category_count.get)
        return most_popular_category

    def get_event_categories(self):
        # Return a set of unique categories for events associated with the place
        return set(event.category for event in self._events)

    def events_with_multiple_categories(self):
        # Return a list of events that belong to multiple categories
        multi_category_events = [event for event in self._events if len(set(event.categories)) > 1]
        return multi_category_events

    # price

    def average_ticket_price(self):
        # Calculate the average ticket price of events at the place
        if not self._events:
            return 0
        total_price = sum(event.get_average_ticket_price() for event in self._events)
        return total_price / len(self._events)

    def get_event_ticket_prices(self):
        # Return a dictionary where event names are keys and their average ticket prices are values
        event_ticket_prices = {event.name: event.get_average_ticket_price() for event in self._events}
        return event_ticket_prices

    # comments

    def events_with_comments(self, min_comments=5):
        # Return a list of events with comments exceeding a specified threshold
        events_with_comments = [event for event in self._events if event.get_total_comments() > min_comments]
        return events_with_comments

    def events_without_comments(self):
        # Return a list of events with no comments
        events_without_comments = [event for event in self._events if event.get_total_comments() == 0]
        return events_without_comments

    def get_event_comments(self):
        # Return a dictionary where event names are keys and their comments are values
        event_comments = {event.name: event.comments for event in self._events}
        return event_comments

    # place

    def find_events_by_location(self, location):
        # Return a list of events taking place in a specific location
        location_events = [event for event in self._events if event.place == location]
        return location_events

    ### °°° other functions °°°