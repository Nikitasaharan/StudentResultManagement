# Student Result Management System
# by: Nikita Saharan
import time

class Student:
    def __init__(self, roll_no, name, marks, course):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.course = course

    def __str__(self):
        return f"{self.roll_no}\t{self.name}\t{self.marks}\t{self.course}"


class StudentResultManagement:
    def __init__(self):
        self.records = {}
        self.size = 10  # hash table size

    # Hash function
    def hash_function(self, roll_no):
        return roll_no % self.size

    # Insert record using hashing with linear probing
    def insert_student(self, student):
        index = self.hash_function(student.roll_no)
        while index in self.records:
            index = (index + 1) % self.size
        self.records[index] = student
        print(f"Record added for Roll No: {student.roll_no}")

    # Sequential Search
    def sequential_search(self, roll_no):
        for student in self.records.values():
            if student.roll_no == roll_no:
                return student
        return None

    # Binary Search (on sorted list)
    def binary_search(self, sorted_list, roll_no):
        low = 0
        high = len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid].roll_no == roll_no:
                return sorted_list[mid]
            elif sorted_list[mid].roll_no < roll_no:
                low = mid + 1
            else:
                high = mid - 1
        return None

    # Quick Sort (by marks)
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2].marks
        left = [x for x in arr if x.marks < pivot]
        middle = [x for x in arr if x.marks == pivot]
        right = [x for x in arr if x.marks > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # Heap Sort (by marks)
    def heapify(self, arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l].marks > arr[largest].marks:
            largest = l
        if r < n and arr[r].marks > arr[largest].marks:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

    # Display all records
    def display_records(self):
        print("\nRollNo\tName\tMarks\tCourse")
        for student in self.records.values():
            print(student)

    # Compare performance of sorting algorithms
    def compare_sorting(self):
        data = list(self.records.values())

        start = time.time()
        self.quick_sort(data)
        quick_time = (time.time() - start) * 1000

        start = time.time()
        self.heap_sort(data)
        heap_time = (time.time() - start) * 1000

        print("\n🔹 Sorting Performance Comparison:")
        print(f"Quick Sort Time: {quick_time:.3f} ms")
        print(f"Heap Sort Time:  {heap_time:.3f} ms")


# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    system = StudentResultManagement()

    # Adding some student records
    system.insert_student(Student(101, "Nikita", 89, "Data Structures"))
    system.insert_student(Student(102, "Karsh", 76, "Machine Learning"))
    system.insert_student(Student(103, "Muskan", 92, "Java Programming"))
    system.insert_student(Student(104, "Neha", 85, "Statistics"))

    # Display all records
    print("\n📋 All Student Records:")
    system.display_records()

    # Searching for a student
    roll = int(input("\nEnter Roll Number to Search: "))
    found = system.sequential_search(roll)
    if found:
        print(f"Student Found: {found.name}, Marks: {found.marks}")
    else:
        print("Student Not Found.")

    # Sorting by marks using Quick Sort
    sorted_by_marks = system.quick_sort(list(system.records.values()))
    print("\n Sorted by Marks (Quick Sort):")
    for s in sorted_by_marks:
        print(s)

    # Performance comparison
    system.compare_sorting()
