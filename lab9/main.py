from models import Student, AcademicPerformance


def main():
    schedule = {
        "Monday": "Вишмат - 12:00",
        "Tuesday": "Вишмат - 13:00",
        "Wednesday": "Вишмат - 14:00",
        "Thursday": "Вишмат - 15:00",
        "Friday": "Вишмат - 16:00",
    }
    academic_performance = AcademicPerformance(False, True, 89)
    student = Student("Oleg", "Antonio", schedule, "ir1337", "IKTA", "LPNU", academic_performance)
    print(student)
    print(student.get_schedule())


if __name__ == '__main__':
    main()
