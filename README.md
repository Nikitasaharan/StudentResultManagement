# Student Result Management System

## Overview
The **Student Result Management System** is designed to manage and analyze student records using **data structures and algorithms** like Hashing, Searching, and Sorting.  
It allows efficient storage, quick lookup, and ordered display of student results.

## Features
- Roll number-based **Sequential & Binary Search**
- Record storage using **Hash Table** with collision handling
- Sorting by **Marks** using Heap Sort and Quick Sort
- Sorting by **Roll Number** using Radix Sort or Bucket Sort
- **Performance comparison** between sorting algorithms

## Data Structure Design
### Student Record ADT
| Attribute | Type | Description |
|------------|------|-------------|
| StudentID | Integer | Unique roll number |
| StudentName | String | Student’s name |
| Marks | Integer | Marks obtained |
| CourseDetails | String | Course information |

### Methods
- `insertStudent(data)`
- `searchStudent(StudentID)`
- `sortRecords()`

## Implementation Steps
1. Create a hash table for storing student records.  
2. Implement sequential and binary search for roll number lookup.  
3. Implement Heap Sort and Quick Sort for sorting by marks.  
4. Implement Radix or Bucket Sort for sorting roll numbers.  
5. Compare the time taken by each sorting algorithm.

## output Screenshot
<img width="525" height="798" alt="image" src="https://github.com/user-attachments/assets/8fc0aa81-3560-49fe-88c9-ceb322ab8324" />

## Performance Comparison Example
| Algorithm | Dataset Size | Time (ms) |
|------------|---------------|-----------|
| Heap Sort | 100 | 3.5 |
| Quick Sort | 100 | 2.9 |
| Radix Sort | 100 | 2.2 |

## Technologies Used
- Language: Python 
- Data Structures: Hash Table, Arrays  
- Algorithms: Heap Sort, Quick Sort, Radix Sort, Sequential & Binary Search

## By
- Nikita Saharan
- B.Sc (Hons) Data Science, Semester 3
- DSA Theory Assignment 3
   



