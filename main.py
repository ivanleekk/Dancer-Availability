import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy

data_file = 'data/data.csv'
data = pd.read_csv(data_file)
print(data.columns)

# get time of people who are not free
print(data['Please indicate the timings and days in which you are generally 𝗡𝗢𝗧 free for rehearsals.  [1000-1100]'])

class Day:
    def __init__(self, name):
        self.name = name
        self.time_slots = []
        self.people = set()
        self.num_people = 0
        self.add_time_slots()

    def add_time_slot(self, time_slot):
        self.time_slots.append(time_slot)

    def add_time_slots(self):
        for i in range(10,22):
            self.add_time_slot(TimeSlot(str(i) + '00-' + str(i+1) + '00'))   

    def add_person(self, person):
        self.people.add(person)
        self.num_people += 1

    def __repr__(self):
        return self.name + str(self.time_slots) + str(self.people)

class TimeSlot:
    def __init__(self, name):
        self.name = name
        self.people = set()
        self.num_people = 0

    def add_person(self, person):
        self.people.add(person)
        self.num_people += 1

    def __repr__(self):
        return self.name + str(self.people)

class Person:
    def __init__(self, name):
        self.name = name
        self.days = []
        self.num_days = 0

    def add_day(self, day):
        self.days.append(day)
        self.num_days += 1

    def __repr__(self):
        return self.name + self.days

# create days
monday = Day('Monday')
tuesday = Day('Tuesday')
wednesday = Day('Wednesday')
thursday = Day('Thursday')
friday = Day('Friday')
saturday = Day('Saturday')
sunday = Day('Sunday')

# iterate through data and add people to days
for i in range(len(data)):
    name = data['Full Name'][i]
    for j in range(10,22):
        col = 'Please indicate the timings and days in which you are generally 𝗡𝗢𝗧 free for rehearsals.  [' + str(j) + '00-' + str(j+1) + '00' ']'
        print(col)
        days = data[col][i]

        if pd.isnull(days):
            continue
        days = days.split(',')
        for day in days:
            day = day.strip()
            if day == 'Monday':
                monday.add_person(name)
                monday.time_slots[j-10].add_person(name)
            elif day == 'Tuesday':
                tuesday.add_person(name)
                tuesday.time_slots[j-10].add_person(name)
            elif day == 'Wednesday':
                wednesday.add_person(name)
                wednesday.time_slots[j-10].add_person(name)
            elif day == 'Thursday':
                thursday.add_person(name)
                thursday.time_slots[j-10].add_person(name)
            elif day == 'Friday':
                friday.add_person(name)
                friday.time_slots[j-10].add_person(name)
            elif day == 'Saturday':
                saturday.add_person(name)
                saturday.time_slots[j-10].add_person(name)
            elif day == 'Sunday':
                sunday.add_person(name)
                sunday.time_slots[j-10].add_person(name)
print(saturday)