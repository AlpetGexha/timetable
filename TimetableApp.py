import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class TimetableApp:
    MAX_COURSES = 6

    def __init__(self, root):
        self.root = root
        self.root.title("University Timetable")

        self.filename = tk.StringVar()
        self.selected_courses = []
        self.courses = []
        self.filtered_courses = []
        self.selected_indices = []

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.create_file_input(frame)
        self.create_filters(frame)
        self.create_buttons(frame)
        self.create_course_listbox(frame)
        self.create_warning_label(frame)
        self.create_selected_courses_display(frame)

    def create_file_input(self, frame):
        """Create file input elements."""
        tk.Label(frame, text="CSV File:").grid(row=0, column=0, padx=5)
        tk.Entry(frame, textvariable=self.filename, width=40).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=5)

    def create_filters(self, frame):
        """Create filter elements."""
        tk.Label(frame, text="Year:").grid(row=1, column=0, padx=5)

        # Create a style for the Combobox with a blue background
        style = ttk.Style()
        style.configure("TCombobox", fieldbackground="blue")

        self.year_cb = ttk.Combobox(frame, values=["1", "2", "3", "4"], style="TCombobox")
        self.year_cb.grid(row=1, column=1, padx=5, sticky='w')

        tk.Label(frame, text="Departament:").grid(row=1, column=2, padx=5)
        self.code_entry = tk.Entry(frame, width=10)
        self.code_entry.grid(row=1, column=3, padx=5, sticky='w')

    def create_buttons(self, frame):
        """Create action buttons."""
        tk.Button(frame, text="Display", command=self.display_courses).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="Clear", command=self.clear_selection).grid(row=2, column=1, pady=10)
        tk.Button(frame, text="Save", command=self.save_timetable).grid(row=2, column=2, pady=10)

    def create_course_listbox(self, frame):
        """Create the course listbox."""
        self.course_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=60, height=15)
        self.course_listbox.grid(row=3, column=0, columnspan=4, pady=10)
        self.course_listbox.bind('<<ListboxSelect>>', self.select_course)

    def create_warning_label(self, frame):
        """Create the warning label."""
        self.warning_label = tk.Label(frame, text="", fg="red")
        self.warning_label.grid(row=4, column=0, columnspan=4)

    def create_selected_courses_display(self, frame):
        """Create the text widget to display selected course details."""
        tk.Label(frame, text="Selected Courses:").grid(row=3, column=4, padx=5, sticky='n')
        self.selected_courses_text = tk.Text(frame, width=40, height=15, state=tk.DISABLED)
        self.selected_courses_text.grid(row=3, column=5, padx=5, pady=10)

    def browse_file(self):
        """Open file dialog to select CSV file."""
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.filename.set(filename)

    def read_csv(self):
        """Read courses from the selected CSV file."""
        try:
            with open(self.filename.get(), 'r') as file:
                reader = csv.reader(file)
                self.courses = [{"Code": row[0], "Course": row[1], "Days": row[2], "Times": row[3]} for row in reader if
                    len(row) >= 4]
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")

    def display_courses(self):
        """Display filtered courses based on the selected year and code."""
        if not self.filename.get():
            self.warning_label.config(text="Please choose a CSV file.")
            return

        self.read_csv()
        self.course_listbox.delete(0, tk.END)
        self.selected_indices = []

        year = self.year_cb.get()
        code = self.code_entry.get().upper()  # Ensure code is uppercase

        self.filtered_courses = [course for course in self.courses if
            (not year or year in course['Code']) and (not code or code in course['Code'].upper())]

        if not self.filtered_courses:
            self.warning_label.config(text="No courses found for the given filter.")
        else:
            self.warning_label.config(text="")
            for course in self.filtered_courses:
                self.course_listbox.insert(tk.END,
                                           f"{course['Course']} ({course['Code']}) {course['Days']} {course['Times']}")

    def select_course(self, event):
        """Select a course from the listbox."""
        selected_index = self.course_listbox.curselection()
        if not selected_index:
            return

        selected_course = self.filtered_courses[selected_index[0]]
        selected_course_times = selected_course['Times'].split()

        # Check for time conflicts and course limit
        if len(self.selected_courses) >= self.MAX_COURSES:
            self.warning_label.config(text=f"You can select a maximum of {self.MAX_COURSES} courses.")
            return

        for selected in self.selected_courses:
            existing_times = selected['Times'].split()
            if any(time in existing_times for time in selected_course_times):
                self.warning_label.config(text="You have selected courses with conflicting times.")
                return

        self.warning_label.config(text="")
        self.selected_courses.append(selected_course)
        self.selected_indices.append(selected_index[0])
        self.update_course_listbox()
        self.display_selected_courses()
        print(f"Selected courses: {[course['Course'] for course in self.selected_courses]}")

    def update_course_listbox(self):
        """Update the course listbox to highlight selected courses."""
        self.course_listbox.delete(0, tk.END)
        for i, course in enumerate(self.filtered_courses):
            if i in self.selected_indices:
                self.course_listbox.insert(tk.END,
                                           f"{course['Course']} ({course['Code']}) {course['Days']} {course['Times']}")
                self.course_listbox.itemconfig(i, {'bg': 'lightblue'})
            else:
                self.course_listbox.insert(tk.END,
                                           f"{course['Course']} ({course['Code']}) {course['Days']} {course['Times']}")

    def display_selected_courses(self):
        """Display all selected course details in the text widget."""
        self.selected_courses_text.config(state=tk.NORMAL)
        self.selected_courses_text.delete(1.0, tk.END)
        for course in self.selected_courses:
            self.selected_courses_text.insert(tk.END, f"Course: {course['Course']}\n")
            self.selected_courses_text.insert(tk.END, f"Departament: {course['Code']}\n")
            self.selected_courses_text.insert(tk.END, f"Days: {course['Days']}\n")
            self.selected_courses_text.insert(tk.END, f"Times: {course['Times']}\n")
            self.selected_courses_text.insert(tk.END, "-"*40 + "\n")
        self.selected_courses_text.config(state=tk.DISABLED)

    def clear_selection(self):
        """Clear the current course selection."""
        self.course_listbox.selection_clear(0, tk.END)
        self.selected_courses = []
        self.selected_indices = []
        self.warning_label.config(text="")
        self.update_course_listbox()
        self.selected_courses_text.config(state=tk.NORMAL)
        self.selected_courses_text.delete(1.0, tk.END)
        self.selected_courses_text.config(state=tk.DISABLED)

    def save_timetable(self):
        """Save the selected courses to a CSV file."""
        if not self.selected_courses:
            self.warning_label.config(text="No courses selected to save.")
            return

        try:
            with open("timetable.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Course", "Code", "Days", "Times"])
                for course in self.selected_courses:
                    writer.writerow([course['Course'], course['Code'], course['Days'], course['Times']])
            messagebox.showinfo("Success", "Timetable saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save timetable: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()
