# -------- Node Definition --------
class StudentNode:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


# -------- Linked List --------
class StudentLinkedList:
    def __init__(self):
        self.head = None

    def insert_student(self, roll, name, marks):
        new_node = StudentNode(roll, name, marks)
        if self.head is None:
            self.head = new_node
            print("Student added successfully!")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print("Student added successfully!")

    def display_students(self):
        if self.head is None:
            print("No student records found.")
            return
        temp = self.head
        print("\nRoll\tName\tMarks")
        print("-" * 30)
        while temp:
            print(f"{temp.roll}\t{temp.name}\t{temp.marks}")
            temp = temp.next

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print("\nStudent Found!")
                print(f"Roll  : {temp.roll}")
                print(f"Name  : {temp.name}")
                print(f"Marks : {temp.marks}")
                return
            temp = temp.next
        print("Student not found!")

    def update_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                try:
                    temp.name = input("Enter New Name: ")
                    temp.marks = int(input("Enter New Marks: "))
                    print("Student updated successfully!")
                except ValueError:
                    print("Invalid input! Marks must be a number.")
                return
            temp = temp.next
        print("Student not found!")

    def delete_student(self, roll):
        temp = self.head
        prev = None
        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Student deleted successfully!")
                return
            prev = temp
            temp = temp.next
        print("Student not found!")

    def sort_by_marks(self, ascending=True):
        if self.head is None or self.head.next is None:
            print("Not enough records to sort.")
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if (ascending and temp.marks > temp.next.marks) or \
                   (not ascending and temp.marks < temp.next.marks):
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print("Students sorted successfully!")


# -------- Main Program --------
sll = StudentLinkedList()

while True:
    try:
        # --- Print Menu ---
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Sort Students by Marks")
        print("6. Delete Student")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                try:
                    n = int(input("Enter number of students: "))
                    if n <= 0:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid positive number.")
                    continue
                for i in range(n):
                    print(f"\nStudent {i + 1}")
                    try:
                        roll = int(input("Enter Roll Number: "))
                        name = input("Enter Name: ")
                        marks = int(input("Enter Marks: "))
                        sll.insert_student(roll, name, marks)
                    except ValueError:
                        print("Roll and Marks must be numbers!")

            case 2:
                sll.display_students()

            case 3:
                try:
                    roll = int(input("Enter Roll Number to Search: "))
                    sll.search_student(roll)
                except ValueError:
                    print("Invalid roll number!")

            case 4:
                try:
                    roll = int(input("Enter Roll Number to Update: "))
                    sll.update_student(roll)
                except ValueError:
                    print("Invalid roll number!")

            case 5:
                try:
                    order = int(input("1. Ascending\n2. Descending\nChoose: "))
                    match order:
                        case 1:
                            sll.sort_by_marks(True)
                            print("\nStudents sorted in ascending order:")
                            sll.display_students()

                        case 2:
                            sll.sort_by_marks(False)
                            print("\nStudents sorted in descending order:")
                            sll.display_students()

                        case _:
                            print("Invalid option!")
                except ValueError:
                    print("Enter valid input!")

            case 6:
                try:
                    roll = int(input("Enter Roll Number to Delete: "))
                    sll.delete_student(roll)
                except ValueError:
                    print("Invalid roll number!")

            case 7:
                print("Exiting Program...")
                break

            case _:
                print("Invalid choice!")

    except ValueError:
        print("Please enter numbers only!")
