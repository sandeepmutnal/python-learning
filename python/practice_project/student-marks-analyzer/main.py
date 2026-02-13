import os


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
    print("📊 Student Marks Analyzer")

    name = input("Enter student name: ")

    # Validate number of subjects
    while True:
        try:
            subjects = int(input("Enter number of subjects: "))
            if subjects <= 0:
                print("Subjects must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    marks = []
    total = 0

    for i in range(subjects):
        while True:
            try:
                m = float(input(f"Enter mark {i+1}: "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks.append(m)
                total += m
                break
            except ValueError:
                print("Invalid input. Enter numeric value.")

    average = total / subjects
    grade = calculate_grade(average)
    status = "PASS" if average >= 50 else "FAIL"

    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Status:", status)

    print("\nMarks Entered:")
    for i, m in enumerate(marks, start=1):
        print(f"Subject {i}: {m}")

    # Save result in script folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "result.txt")

    with open(file_path, "w") as f:
        f.write("Student Marks Analyzer\n")
        f.write(f"Name: {name}\n")
        f.write(f"Total: {total}\n")
        f.write(f"Average: {round(average,2)}\n")
        f.write(f"Grade: {grade}\n")
        f.write(f"Status: {status}\n")

    print("\nResult saved to result.txt")


if __name__ == "__main__":
    main()
