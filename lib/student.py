#!/usr/bin/env python
#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None:
            self.knowledge = []
        else:
            self.knowledge = knowledge

    def learn(self, unit):
        if unit not in self.knowledge:
            self.knowledge.append(unit)


# knowledge = [
#     "str is a data type in Python",
# ]
# s = Student("Halani", "hikey", knowledge)
# s.learn(
#     "JavaScript async web request",
# )