import re


class Electronic_Diary():
    def __init__(self, username):
        self.username = username
        self.subjects = {}

    def email_validation(self, email):
        email_validation_pattern = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

        if re.match(email_validation_pattern, email):
            return True

        return False

    def subject_validation(self, subject):
        if subject in self.subjects.keys():
            return True

        return False

    def show_subjects_and_grades(self):
        print("Subjects:")

        for subject, grades in self.subjects.items():
            total_grades = list(map(float, grades))  # This is the same as the grades variable, but it is a float.

            if grades:
                average_grade = f"{sum(total_grades) / len(total_grades)}"
                print(f"{subject}: {", ".join(grades)} | Average grade: {average_grade}")
            else:
                print(f"{subject}: no grades")

        print()

    def add_subject(self, subject):
        self.subjects[subject] = ()
        print()  # To look prettier on the console

    def add_grade(self, subject, grade):
        self.subjects[subject] += (grade,)


def main():
    print("Registration:\n")

    username = input("Username: ")

    user_diary = Electronic_Diary(username)

    # Email validation
    while True:
        email = input("Email: ")

        is_valid = user_diary.email_validation(email)

        if is_valid:
            print(f"Welcome, {username}!\n")
            break
        else:
            print("Invalid email! Please try again!")

    # Operations
    while True:
        print(f"Chose one of the following operations:")
        print("1) Show subjects \n2) Add subjects \n3) Add grade \n4) Quit\n")

        choice = int(input("Enter the number of the operation: "))

        if choice == 1:
            print()  # To look prettier on the console
            user_diary.show_subjects_and_grades()
        elif choice == 2:
            subject = input("\nEnter the subject that you would like to add: \n")

            user_diary.add_subject(subject)
        elif choice == 3:
            print("Which of the following subjects would you like to add a grade?")
            user_diary.show_subjects_and_grades()

            while True:
                subject = input("Subject: ")

                if user_diary.subject_validation(subject):
                    grade = input("Grade: ")

                    user_diary.add_grade(subject, grade)
                    break
                else:
                    print("Subject not found!")
        elif choice == 4:
            print(f"Goodbye, {username}! Have a great day!")
            break


if __name__ == "__main__":
    main()
