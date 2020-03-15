class School:
    def __init__(self):
        self.rosterDict = {}

    def add_student(self, name, grade):
        if str(grade) in self.rosterDict:
            self.rosterDict[str(grade)].append(name)
            self.rosterDict[str(grade)] = sorted(self.rosterDict[str(grade)])
        else:
            self.rosterDict[str(grade)] = [name]

    def roster(self):
        roster = []
        grades = []
        for grade in self.rosterDict:
            grades.append(int(grade))
        grades = sorted(grades)
        for grade in grades:
            roster = [*roster, *self.rosterDict[str(grade)]]
        return roster

    def grade(self, grade_number):
        if str(grade_number) in self.rosterDict:
            return self.rosterDict[str(grade_number)]
        else:
            return []
