import json
from datetime import datetime

class Comment:
    def __init__(self, rating,author, title, content, date, statereply=0, likes=0,):
        self._rating = rating
        self._title = title
        self._content = content
        self._likes = likes
        self._replies = []
        self._statereply = statereply
        self._author = author
        self._date = date

    ## property / setter

    @property
    def author(self):
        return self._author

    @property
    def replies(self):
        return self._replies

    @property
    def statereply(self):
        return self._statereply

    @property
    def rating(self):
        return self._rating

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def date(self):
        return self._date

    @property
    def likes(self):
        return self._likes

    @author.setter
    def set_author(self, new_author):
        self._author = new_author

    @replies.setter
    def set_reply(self, new_replies):
        self._replies = new_replies

    @statereply.setter
    def set_statereply(self, new_state_reply):
        self._state_reply = new_state_reply

    @rating.setter
    def set_rating(self, new_rating):
        self._rating = new_rating

    @title.setter
    def set_title(self, new_title):
        self._title = new_title

    @content.setter
    def set_content(self, new_content):
        self._content = new_content

    @date.setter
    def set_date(self, new_date):
        self._date = new_date

    @likes.setter
    def set_likes(self, new_num_likes):
        self._likes = new_num_likes

    def add_like(self):
        self._likes += 1

    def with_like(self):
        self._likes -= 1

    ## features

    def is_empty(self):
        """Checks if the comment is empty."""
        return not self.title and not self.content

    def content_length(self):
        """Returns the length of the comment's content."""
        return len(self.content)

    def is_valid(self):
        """Checks if the comment is valid."""
        return bool(self.title) and bool(self.content)

    def has_keyword(self, keyword):
        """Checks the presence of a keyword in the comment's content."""
        return keyword.lower() in self._content.lower()

    def time_since_creation(self):
        """Returns the time difference since the comment's creation."""
        time_difference = datetime.now() - self.date.to_datetime()
        return time_difference


    ## update / clone

    def update_properties(self, **kwargs):
        """Updates multiple comment properties at once."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def clone(self, new_date):
        """Clones the comment with a new date."""
        return Comment(
            author=self._author,
            rating=self._rating,
            title=self._title,
            content=self._content,
            date=new_date,
            likes=self._likes,
            replies=self._replies,
            statereply=self._statereply
        )

    ## display / format

    def __str__(self):
        return f"Comment by {self._author} on {self._date}: {self._title}"

    def display_details(self):
        """Displays all comment details."""
        print(f"Author: {self._author}")
        print(f"Date: {self._date._date}")  # Using the to_string method from the Date class
        print(f"Title: {self._title}")
        print(f"Content: {self._content}")
        print(f"Rating: {self._rating}")
        print(f"Likes: {self._likes}")

    def truncate_title(self, length=30):
        """Truncates the title to a certain length."""
        return self._title[:length] + "..." if len(self._title) > length else self._title

    def summarize(self, length=20):
        """Returns a summarized version of the comment."""
        return f"{self._content[:length]}..." if len(self._content) > length else self._content

    def to_json(self):
        """Returns a JSON representation of the comment."""
        comment_json = {
            "author": self._author,
            "date": self._date.to_string(),
            "title": self._title,
            "content": self._content,
            "rating": self._rating,
            "likes": self._likes
        }
        return json.dumps(comment_json)

    ## comparison

    def compare_to(self, other_comment):
        """Compares two comments based on the date."""
        if not isinstance(other_comment, Comment):
            raise ValueError("Comparison must be done with another Comment object.")
        return self.date.to_datetime() > other_comment.date.to_datetime()

    ## popularity

    def relative_popularity(self, total_likes):
        """Calculates the relative popularity of the comment."""
        return (self.likes / total_likes) * 100 if total_likes > 0 else 0

    def is_popular(self, threshold=100):
        """Checks if the comment is popular based on a likes threshold."""
        return self.likes >= threshold

    ## reply

    def add_reply(self, reply_comment):
        """Adds a reply to a comment."""
        # Ensure that reply_comment is an instance of the Comment class
        if self.statereply == True or reply_comment.statereply == False:
            raise ValueError("You can only add replies to comments")
        self._replies.append(reply_comment)

    def remove_reply(self, reply_comment):
        """Removes a specific reply to a comment."""
        if reply_comment in self._replies:
            self._replies.remove(reply_comment)

    ### °°° other functions °°°