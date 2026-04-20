from student_grades import StudentsGrades
from sorting import random_numbers


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů:", results.count())
    print()

    for i in range(results.count()):
        score = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {score} points – {grade}")
    print()

    print("Studenti s 100 body:", results.find(100))
    print()

    print("Seřazené výsledky:")
    print(results.get_sorted())
    print()

    random_results = StudentsGrades(random_numbers(30, 0, 100))

    print("Náhodná data:")
    print("Počet studentů:", random_results.count())
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()