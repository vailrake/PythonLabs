from __future__ import annotations


class University:
    def __init__(self, university_name: str):
        self.university_name = university_name


class Institute(University):

    def __init__(self, institute_name: str, university_name: str):
        super().__init__(university_name)
        self.institute_name = institute_name


class Group(Institute):
    def __init__(self, group_name: str, institute_name: str, university_name: str):
        super().__init__(institute_name, university_name)
        self.group_name = group_name


class Schedule(Group):
    def __init__(self, schedule: dict, group_name: str, institute_name: str, university_name: str):
        super().__init__(group_name, institute_name, university_name)
        self.schedule = schedule

    def get_schedule(self):
        print(f"{self.group_name} schedule \n {self.schedule}")


class Student(Schedule):
    def __init__(self, name: str, surname: str, schedule: dict, group_name: str, institute_name: str,
                 university_name: str, academic_performance: AcademicPerformance):
        super().__init__(schedule, group_name, institute_name, university_name)
        self.name = name
        self.surname = surname
        self.academic_performance = academic_performance

    def __str__(self):
        return f"Student {self.name} {self.surname} from {self.university_name} institute {self.institute_name} group {self.group_name} " \
               + "has scholarship" if self.academic_performance.is_student_has_scholarship else "."


class AcademicPerformance:
    def __init__(self, is_student_has_academic_debt: bool, is_student_has_scholarship: bool, rating: float):
        self.is_student_has_academic_debt = is_student_has_academic_debt
        self.is_student_has_scholarship = is_student_has_scholarship
        self.rating = rating
