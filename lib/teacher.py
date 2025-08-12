#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Python is a versatile programming language.",
            "Object-oriented programming is a paradigm.",
            "Inheritance allows code reuse.",
            "Polymorphism enables flexible code.",
            "Encapsulation protects data."
        ]

    def teach(self):
        import random
        return random.choice(self.knowledge)