from __future__ import annotations

def get_grade_points(letter: str) -> float | None:
    """
    Standard 4.0 scale with +/-.
    Returns None if the input is invalid.
    """
    scale = {
        "A": 4.0,  "A-": 3.7,
        "B+": 3.3, "B": 3.0,  "B-": 2.7,
        "C+": 2.3, "C": 2.0,  "C-": 1.7,
        "D+": 1.3, "D": 1.0,  "D-": 0.7,
        "E": 0.0,  "F": 0.0,  # OSU often uses E for failing; F is also common elsewhere
    }
    letter = letter.strip().upper()
    return scale.get(letter)

def prompt_float(msg: str, allow_blank: bool = False) -> float | None:
    while True:
        raw = input(msg).strip()
        if allow_blank and raw == "":
            return None
        try:
            val = float(raw)
            return val
        except ValueError:
            print("Please enter a number (or press Enter to skip).")

def prompt_int(msg: str) -> int:
    while True:
        raw = input(msg).strip()
        try:
            val = int(raw)
            if val <= 0:
                print("Please enter a positive integer.")
                continue
            return val
        except ValueError:
            print("Please enter a whole number (e.g., 5).")

def prompt_credits(msg: str) -> float:
    while True:
        raw = input(msg).strip()
        try:
            val = float(raw)
            if val <= 0:
                print("Credits must be > 0.")
                continue
            return val
        except ValueError:
            print("Please enter credits as a number (e.g., 3 or 4).")

def prompt_grade(msg: str) -> float:
    while True:
        raw = input(msg).strip()
        gp = get_grade_points(raw)
        if gp is None:
            print("Invalid grade. Use: A, A-, B+, B, B-, C+, C, C-, D+, D, D-, E/F")
            continue
        return gp

def main() -> None:
    print("=== GPA Calculator (Semester + Cumulative) ===\n")

    print("Optional (recommended): Enter your CURRENT cumulative GPA and total credits.")
    current_gpa = prompt_float("Current cumulative GPA (press Enter to skip): ", allow_blank=True)
    current_credits = None
    if current_gpa is not None:
        current_credits = prompt_float("Total earned credits so far (e.g., 15) : ", allow_blank=False)
        if current_credits is not None and current_credits <= 0:
            print("Credits must be > 0. Skipping cumulative calculation.")
            current_gpa = None
            current_credits = None

    print("\nNow enter THIS SEMESTER'S courses.")
    num_courses = prompt_int("How many courses are you entering? ")

    semester_quality_points = 0.0
    semester_credits = 0.0

    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        course_name = input("  Course name (optional): ").strip()
        credits = prompt_credits("  Credits (e.g., 3): ")
        grade_points = prompt_grade("  Final grade (A, A-, B+, ... , E/F): ")

        semester_quality_points += credits * grade_points
        semester_credits += credits

        if course_name:
            print(f"  Added: {course_name} | {credits} credits | {grade_points:.1f} pts")

    semester_gpa = semester_quality_points / semester_credits if semester_credits > 0 else 0.0

    print("\n=== Results ===")
    print(f"Semester credits: {semester_credits:.1f}")
    print(f"Semester GPA:     {semester_gpa:.3f}")

    if current_gpa is not None and current_credits is not None:
        cumulative_quality_points = current_gpa * current_credits
        new_total_quality_points = cumulative_quality_points + semester_quality_points
        new_total_credits = current_credits + semester_credits
        new_cumulative_gpa = new_total_quality_points / new_total_credits

        print("\n--- Cumulative Update ---")
        print(f"Previous credits: {current_credits:.1f}")
        print(f"Previous GPA:     {current_gpa:.3f}")
        print(f"New total credits:{new_total_credits:.1f}")
        print(f"New cumulative GPA:{new_cumulative_gpa:.3f}")

    print("\nDone.")

if __name__ == "__main__":
    main()
