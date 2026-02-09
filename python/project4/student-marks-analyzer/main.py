def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def main():
    print("Student Marks Analyzer")

    name = input("Enter student name: ")

    subjects = int(input("Enter number of subjects: "))

    marks = []
    total = 0

    for i in range(subjects):
        m = float(input(f"Enter mark {i+1}: "))
        marks.append(m)
        total += m

    average = total / subjects
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
