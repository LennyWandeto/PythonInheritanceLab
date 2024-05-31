#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    knowledge = ["wp"]
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(first_name, last_name)
    def teach(self):
        if len(Teacher.knowledge) == 0:
            return None
        else:
            for knowl in Teacher.knowledge:
                return knowl
        pass