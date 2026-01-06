# Student Grade Calculator
# Author: Pavani Ravuvari
# Week 2 Project – Control Flow & Data Structures

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent! Keep it up."
    elif avg >= 80:
        return "B", "Very Good! You're doing well."
    elif avg >= 70:
        return "C", "Good. Can improve more."
    elif avg >= 60:
        return "D", "Needs improvement."
    else:
        return "F", "Failed. Please work harder."

def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input! Enter a number.")

def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Get number of students
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Invalid input! Enter an integer.")

    students = []

    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        name = input("Student Name: ").strip()
        while name == "":
            print("Name cannot be empty.")
            name = input("Student Name: ").strip()

        math = get_valid_mark("Math")
        science = get_valid_mark("Science")
        english = get_valid_mark("English")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        students.append({
            "name": name,
            "average": avg,
            "grade": grade,
            "comment": comment
        })

    # Display results
    print("\n" + "=" * 60)
    print("RESULT SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20}{'Avg':>8}{'Grade':>8}  Comment")
    print("-" * 60)

    averages = []
    for s in students:
        print(f"{s['name']:<20}{s['average']:>8.1f}{s['grade']:>8}  {s['comment']}")
        averages.append(s['average'])

    # Statistics
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students : {n}")
    print(f"Class Average  : {sum(averages)/len(averages):.2f}")
    print(f"Highest Avg   : {max(averages):.2f}")
    print(f"Lowest Avg    : {min(averages):.2f}")

    print("\nThank you for using the Grade Calculator!")

if __name__ == "__main__":
    main()
