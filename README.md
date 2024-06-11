# timetable (University Timetable Application) tool

The University Timetable Application is a desktop application built using Python and Tkinter that allows university students to manage and organize their courses efficiently

![image](https://github.com/AlpetGexha/timetable/assets/50520333/e65479e5-49f8-4a5c-a9dc-263279e123a4)

## Description

The University Timetable Application is a desktop application built using Python and Tkinter that allows university students to manage and organize their courses efficiently. Users can upload a CSV file containing course details, filter courses based on the year and department, and select up to six courses while avoiding time conflicts. The selected courses can be saved into a new CSV file, ensuring that the student's timetable is well-organized and free of scheduling conflicts.

## Features

- **CSV File Import**: Allows users to upload a CSV file containing course details.
- **Filtering**: Users can filter courses by year and department.
- **Course Selection**: Users can select up to six courses while avoiding time conflicts.
- **Course List Display**: Displays the list of courses that match the filter criteria.
- **Selected Courses Display**: Shows details of the selected courses.
- **Timetable Saving**: Saves the selected courses into a CSV file.

## How It Works

### User Interface

The application interface is divided into several sections:

1. **File Input**: 
   - **CSV File**: Entry to display the selected CSV file path.
   - **Browse**: Button to open a file dialog for selecting a CSV file.

2. **Filters**:
   - **Year**: Combobox to select the year of study (1 to 4).
   - **Department**: Entry to input the department code for filtering courses.

3. **Action Buttons**:
   - **Display**: Button to filter and display the courses based on the selected year and department.
   - **Clear**: Button to clear the current selection.
   - **Save**: Button to save the selected courses to a CSV file.

4. **Course Listbox**: 
   - Displays the list of courses matching the filter criteria.
   - Allows users to select a course from the list.

5. **Warning Label**:
   - Displays warnings and error messages to the user.

6. **Selected Courses Display**:
   - Text widget showing details of the selected courses.

### Functionality

1. **Browse File**: 
   - Opens a file dialog to select a CSV file containing course details.
   - Sets the file path in the CSV File entry.

2. **Read CSV**:
   - Reads the selected CSV file and stores course details in a list of dictionaries.

3. **Display Courses**:
   - Filters courses based on the selected year and department code.
   - Displays the filtered courses in the listbox.

4. **Select Course**:
   - Allows the user to select a course from the listbox.
   - Checks for time conflicts and ensures the maximum number of courses is not exceeded.
   - Highlights selected courses and displays their details in the text widget.

5. **Clear Selection**:
   - Clears the current selection of courses.
   - Resets the listbox and text widget.

6. **Save Timetable**:
   - Saves the selected courses into a CSV file named "timetable.csv".
   - Displays a success message upon successful save.

## Usage

1. **Start the Application**: Run the application to open the main window.
2. **Upload CSV File**: Click the "Browse" button to select a CSV file containing course details.
3. **Filter Courses**: Select the year and enter the department code to filter the courses.
4. **Display Courses**: Click the "Display" button to show the filtered courses in the listbox.
5. **Select Courses**: Click on a course in the listbox to select it. Ensure there are no time conflicts.
6. **Clear Selection**: Click the "Clear" button to clear the current selection.
7. **Save Timetable**: Click the "Save" button to save the selected courses to a CSV file.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- A CSV file with course details (Course Code, Course Name, Days, Times)

## Running the Application

To run the application, execute the following commands:

```bash
python TimetableApp.py
```

Ensure that you have the required CSV file in the appropriate format ready for upload.

Departament,Course,Days,Times
```csv
CS101,Introduction to Computer Science,Mon Wed Fri,10:00-11:00
MATH201,Calculus II,Tue Thu,12:00-13:30
PHY301,Physics III,Mon Wed,Fri 14:00-15:30
CHEM101,General Chemistry,Tue Thu,16:00-17:30
```
