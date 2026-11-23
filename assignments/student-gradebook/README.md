# 📘 Assignment: File I/O Mini-Project: Student Gradebook

## 🎯 Objective

Build a simple gradebook that reads and saves student grades in a CSV file. Practice opening files, reading rows, and appending new data using Python's built-in `csv` module.

## 📝 Tasks

### 🛠️ Create and Read the Gradebook

#### Description
Create a `gradebook.csv` file with a `student,grade` header and at least three student grade rows. Write a Python program that reads and displays its contents.

#### Requirements
Completed program should:
- Open and read `gradebook.csv` using Python's built-in `csv` module.
- Display each student's name and grade.
- Close the file after reading.

### 🛠️ Add a Grade

#### Description
Let the user enter a student's name and grade, then save that record to the gradebook.

#### Requirements
Completed program should:
- Ask the user for a student name and numeric grade.
- Append the new record to `gradebook.csv` without replacing existing rows.
- Keep the CSV header and row format consistent.

### 🛠️ Calculate Student Averages

#### Description
Read the saved gradebook and calculate the average grade for each student who has more than one entry.

#### Requirements
Completed program should:
- Read the grades from `gradebook.csv`.
- Calculate and display each student's average.
- Continue to work after new grades have been added to the file.