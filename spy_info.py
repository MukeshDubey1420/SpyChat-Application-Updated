# Datetime function has been imported from datetime library.
from datetime import datetime


# Spy class contains all basic info of a spy.
class Spy:

    def __init__(self, name, salutation, age, rating, marital):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.marital = marital
        self.is_online = True
        self.chats = []
        self.current_status_message = None


# ChatMessage class contains all chat related info.
class ChatMessage:

    def __init__(self, message, sent_by_me, avg, sender):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
        self.avg = avg
        self.sender = sender

# Spy class has been initialized with some values.
spy = Spy('Alpha', 'Mr.', 24, 3.4, 'Not Married')

# Few friends pre-added
friend_one = Spy('Delta', 'Mr.', 27, 3.5, 'Not Married')
friend_two = Spy('Charlie', 'Ms.', 33, 3.7, 'Married')
friend_three = Spy('Tango', 'Mr.', 35, 3.9, 'Married')

# Friends list contains 3 friends.
friends = [friend_one, friend_two, friend_three]

