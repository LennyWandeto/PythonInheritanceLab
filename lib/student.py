#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(first_name, last_name)
    
    def learn(self, string):
        Student.knowledge.append(string)
        pass