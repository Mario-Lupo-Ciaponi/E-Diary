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

    def subject_presence(self):
        if self.subjects:
            return True

        return False

    def calculate_average_grade(self, grades):
        average_grade = sum(grades) / len(grades)

        return average_grade

    def show_subjects_and_grades(self):
        if self.subjects:
            print("Subjects:")

            all_average_grades = ()

            for subject, grades in self.subjects.items():
                total_grades = list(map(float, grades))  # This is the same as the grades variable, but it is a float.

                if grades:
                    average_grade = self.calculate_average_grade(total_grades)
                    print(f"{subject}: {", ".join(grades)} | Average grade: {average_grade:.2f}")

                    all_average_grades += (average_grade,)
                else:
                    print(f"{subject}: no grades")

            total_average_grade = self.calculate_average_grade(all_average_grades)

            print(f"----------\nTotal: {total_average_grade}")
        else:
            print("No subjects entered.")

    def show_subjects(self):
        number_of_subject = 1

        for subject in self.subjects:
            print(f"{number_of_subject} - {subject}")
            number_of_subject += 1

        print()  # To look prettier on the console

    def add_subject(self, subject):
        self.subjects[subject] = ()
        print(f"Subject {subject} added successfully!")

    def add_grade(self, subject, grade):
        if 2.00 <= float(grade) <= 6.00 and self.subject_validation(subject):
            self.subjects[subject] += (f"{grade:.2f}",)
        elif not self.subject_validation(subject):
            print("Subject not found!")
        elif grade < 2.00 or grade > 6.00:
            print("Invalid grade!")
        else:
            print("Invalid grade and subject not found!")

        print(f"\nGrade added successfully!")


def main():
    print("Registration:\n")

    username = input("Username: ")

    user_diary = Electronic_Diary(username)

    # Email validation
    while True:
        email = input("Email: ")

        is_valid = user_diary.email_validation(email)

        if is_valid:
            print(f"Welcome, {username}!")
            break
        else:
            print("Invalid email! Please try again!")

    # Operations
    while True:
        print(f"\nChose one of the following operations:")
        print("1) Show subject \n2) Add subjects \n3) Add grade \n4) Quit\n")

        choice = int(input("Enter the number of the operation: "))

        if choice == 1:  # Show subjects
            print()  # To look prettier on the console
            user_diary.show_subjects_and_grades()
        elif choice == 2:  # Add subject
            subject = input("\nEnter the subject that you would like to add: \n")

            user_diary.add_subject(subject)
        elif choice == 3:  # Add grade
            print()  # To look prettier on the console

            if user_diary.subject_presence():
                print("Which of the following subjects would you like to add a grade?")
                user_diary.show_subjects()

                while True:
                    subject = input("Subject: ")

                    if user_diary.subject_validation(subject):
                        grade = float(input("Grade: "))

                        user_diary.add_grade(subject, grade)
                        break
                    else:
                        print("Subject not found!")
            else:
                print("No subject in the diary.")
        elif choice == 4:  # Quit
            print(f"------------------------------------"
                  f"\nGoodbye, {username}! Have a great day!")
            break


if __name__ == "__main__":
    main()
