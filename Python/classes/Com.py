import json
from datetime import datetime

class Comment:
    def __init__(self, author, title, content, rating, date, statereply=0, likes=0, replies=[]):
        self._author = author
        self._title = title
        self._rating = rating # 0-> bad, 1-> medium, 2-> good
        self._date = date
        self._content = content
        self._likes = likes
        self._replies = replies
        self._statereply = statereply

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
    def author(self, new_author):
        self._author = new_author

    @statereply.setter
    def statereply(self, new_state_reply):
        self._state_reply = new_state_reply

    @rating.setter
    def rating(self, new_rating):
        self._rating = new_rating

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @content.setter
    def content(self, new_content):
        self._content = new_content

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @likes.setter
    def likes(self, new_num_likes):
        self._likes = new_num_likes

    def add_like(self):
        self._likes += 1

    def remove_like(self):
        self._likes -= 1

    @replies.setter
    def replies(self, new_replies):
        self._replies = new_replies

    def add_reply(self, reply_comment):
        """Adds a reply to a comment."""
        # Ensure that reply_comment is an instance of the Comment class
        if self.statereply == True or reply_comment.statereply == False:
            raise ValueError("You can only add replies to comments")
        self.add_reply(reply_comment)

    def remove_reply(self, reply_comment):
        """Removes a specific reply to a comment."""
        if reply_comment in self._replies:
            self.remove_reply(reply_comment)

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
        return keyword.lower() in self.content.lower()

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
            author=self.author,
            rating=self.rating,
            title=self.title,
            content=self.content,
            date=self.date,
            likes=self.likes,
            replies=self.replies,
            statereply=self.statereply
        )

    ## display / format

    def __str__(self):
        return f"Comment by {self.author.username} on {self.date.date}: {self.title}"

    def display_details(self):
        """Displays all comment details."""
        print(f"Author: {self.author}")
        print(f"Date: {self.date.date}")  # Using the to_string method from the Date class
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Rating: {self.rating}")
        print(f"Likes: {self.likes}")

    def truncate_title(self, length=30):
        """Truncates the title to a certain length."""
        return self._title[:length] + "..." if len(self.title) > length else self.title

    def summarize(self, length=20):
        """Returns a summarized version of the comment."""
        return f"{self._content[:length]}..." if len(self._content) > length else self.content

    def to_json(self):
        """Returns a JSON representation of the comment."""
        comment_json = {
            "author": self.author,
            "date": self.date.date,
            "title": self.title,
            "content": self.content,
            "rating": self.rating,
            "likes": self.likes
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

    ### °°° other functions °°°
