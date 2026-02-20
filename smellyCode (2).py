# Activity Code Snippet: "Student Grade Report"
# NOTE: This code works, but it has many code smells on purpose.

def make_report(students, extra_credit, do_rounding, verbose):
    # students is a list of dicts like:
    # {"name": "Ava", "scores": [88, 91, 79], "late_days": 1}
    # {"name": "Ben", "scores": [70, 68, 72], "late_days": 0}

    report = []
    i = 0

    while i < len(students):
        s = students[i]
        n = s["name"]
        sc = s["scores"]
        ld = s["late_days"]

        # compute average (duplicated logic style)
        total = 0
        j = 0
        while j < len(sc):
            total += sc[j]
            j += 1
        avg = total / len(sc)

        # apply penalties for late work (magic numbers + nested logic)
        if ld > 0:
            if ld == 1:
                avg = avg - 5
            elif ld == 2:
                avg = avg - 10
            else:
                avg = avg - 20

        # extra credit option (boolean flag smell)
        if extra_credit:
            avg = avg + 2

        # rounding option (boolean flag smell)
        if do_rounding:
            avg = int(avg + 0.5)

        # compute letter grade (deep condition chain)
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        # more special rules (more magic numbers)
        if grade == "F":
            if avg >= 59:  # "mercy point" rule
                avg = 60
                grade = "D"

        # verbose output (mixing concerns: computation + printing)
        if verbose:
            print("Student:", n, "Avg:", avg, "Grade:", grade, "LateDays:", ld)

        # inconsistent data structure use
        report.append(n + ": " + str(avg) + " (" + grade + ")")

        # commented-out code smell
        # if grade == "A":
        #     report.append("Excellent work!")

        i += 1

    # sorting results (more hidden behavior)
    report.sort()
    return report


# Example data so it can be run immediately
students = [
    {"name": "Ava", "scores": [88, 91, 79], "late_days": 1},
    {"name": "Ben", "scores": [70, 68, 72], "late_days": 0},
    {"name": "Cora", "scores": [95, 92, 98], "late_days": 3},
    {"name": "Dan", "scores": [59, 60, 58], "late_days": 0},
]

print(make_report(students, extra_credit=True, do_rounding=True, verbose=True))
