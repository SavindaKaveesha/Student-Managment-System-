import tkinter as tk
from tkinter import ttk, messagebox

def create_window():
    window = tk.Tk()
    window.title("Student Management System")
    window.geometry("1024x480")
    
    # align center of the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 1024) // 2
    y = (screen_height - 600) // 2
    window.geometry(f"1024x600+{x}+{y}")
   
    
    
    label_font = ("Helvetica", 16, "bold")
    
    label = tk.Label(window, text="Student Management System",fg="white",bg="#373a52", width=1024, height=3, font=label_font)
    label.pack(side="top", fill="both")
    
    group_frame = tk.Frame(window)
    group_frame.pack(side="left", padx=10, pady=10, anchor="nw")
    
    group_box = tk.LabelFrame(group_frame, text="Student Information")
    group_box.pack(padx=10, pady=10, anchor="w")

    
#label and textbox
    name_label = tk.Label(group_box, text="ID:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(group_box)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    
    
    name_labe2 = tk.Label(group_box, text="Name:")
    name_labe2.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(group_box)
    name_entry.grid(row=1, column=1, padx=5, pady=5)
    
    
    gender_labe2 = tk.Label(group_box, text="Gender:")
    gender_labe2.grid(row=2, column=0, padx=5, pady=5)
# Dropdown menu
    options = ["Male", "Female"]

    selected_option = tk.StringVar()
    selected_option.set(options[0])

    dropdown_menu = tk.OptionMenu(group_box, selected_option, *options)
    dropdown_menu.grid(row=2, column=0, columnspan=2, pady=10)

    
#label and textbox
    age_labe2 = tk.Label(group_box, text="Age:")
    age_labe2.grid(row=3, column=0, padx=5, pady=5)
    age_entry = tk.Entry(group_box)
    age_entry.grid(row=3, column=1, padx=5, pady=5)
    
    
    
    date_labe2 = tk.Label(group_box, text="En-Date:")
    date_labe2.grid(row=4, column=0, padx=5, pady=5)
    date_entry = tk.Entry(group_box)
    date_entry.grid(row=4, column=1, padx=5, pady=5)
    
    
    midterm_labe2 = tk.Label(group_box, text="Midterm:")
    midterm_labe2.grid(row=5, column=0, padx=5, pady=5)
    midterm_entry = tk.Entry(group_box)
    midterm_entry.grid(row=5, column=1, padx=5, pady=5)
    
    
    
    final_labe2 = tk.Label(group_box, text="Final:")
    final_labe2.grid(row=6, column=0, padx=5, pady=5)
    final_entry = tk.Entry(group_box)
    final_entry.grid(row=6, column=1, padx=5, pady=5)
    
    
    gpa_labe2 = tk.Label(group_box, text="GPA:")
    gpa_labe2.grid(row=7, column=0, padx=5, pady=5)
    gpa_entry = tk.Entry(group_box)
    gpa_entry.grid(row=7, column=1, padx=10 ,pady=5)
    
#buttons
    add_button = tk.Button(group_box, text="Add", bg="#373a52", fg="white", width=10, command = self.add_student)
    add_button.grid(row=8, column=0, padx=5, pady=10)

    update_button = tk.Button(group_box, text="Update", bg="#373a52", fg="white", width=10)
    update_button.grid(row=8, column=1, pady=10)
    
    calculate_button = tk.Button(group_box, text="Calculate", bg="#373a52", fg="white", width=10)
    calculate_button.grid(row=9, column=0, pady=10)
    
    save_button = tk.Button(group_box, text="Save", bg="#373a52", fg="white", width=10)
    save_button.grid(row=9, column=1, pady=10)
    
    clear_button = tk.Button(group_box, text="Clear", bg="#373a52", fg="white", width=10)
    clear_button.grid(row=10, column=0, pady=10)
    
    delete_button = tk.Button(group_box, text="Delete", bg="#373a52", fg="white", width=10)
    delete_button.grid(row=10, column=1, pady=10)

    right_frame = tk.Frame(window)
    right_frame.pack(side="left", padx=10, pady=10, anchor="nw")  # Use pack instead of grid


    # Treeview
    tree_columns = ("ID", "Name", "Gender", "Age", "Enroll Date", "Midterm", "Final", "GPA")
    student_tree = ttk.Treeview(right_frame, columns=tree_columns, show="headings", selectmode="browse")

    # Set column headings
    for col in tree_columns:
        student_tree.heading(col, text=col)

    # Set column widths
    for col in tree_columns:
        student_tree.column(col, width=100)

    student_tree.pack(pady=10)

    window.mainloop()

create_window()

def add_student(self):
        roll_number = self.roll_number_entry.get()
        name = self.name_entry.get()
        grade = self.grade_entry.get()

        if not roll_number or not name or not grade:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Add student to the Treeview
        self.student_tree.insert("", "end", values=(roll_number, name, grade))

        # Clear input fields
        self.roll_number_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

def view_students(self):
        # View all students in the Treeview
        # For demo purposes, let's add some sample data
        students_data = [
            ("1", "John Doe", "A"),
            ("2", "Jane Smith", "B"),
            ("3", "Bob Johnson", "C")
        ]

        for student_data in students_data:
            self.student_tree.insert("", "end", values=student_data)

        def search_student(self):
            roll_number = self.roll_number_entry.get()
            if not roll_number:
                messagebox.showerror("Error", "Please enter Roll Number to search")
                return

        # Search for the student in the Treeview
        found = False
        for item in self.student_tree.get_children():
            if roll_number == self.student_tree.item(item, "values")[0]:
                found = True
                messagebox.showinfo("Student Found", f"Roll Number: {roll_number}\nName: {self.student_tree.item(item, 'values')[1]}\nGrade: {self.student_tree.item(item, 'values')[2]}")
                break

        if not found:
            messagebox.showinfo("Student Not Found", f"No student found with Roll Number: {roll_number}")

        def delete_student(self):
            roll_number = self.roll_number_entry.get()
            if not roll_number:
                messagebox.showerror("Error", "Please enter Roll Number to delete")
                return

        # Delete the student from the Treeview
        found = False
        for item in self.student_tree.get_children():
            if roll_number == self.student_tree.item(item, "values")[0]:
                found = True
                self.student_tree.delete(item)
                break

        if not found:
            messagebox.showinfo("Student Not Found", f"No student found with Roll Number: {roll_number}")

        def update_student(self):
            roll_number = self.roll_number_entry.get()
            name = self.name_entry.get()
            grade = self.grade_entry.get()

            if not roll_number:
                messagebox.showerror("Error", "Please enter Roll Number to update")
                return

            # Update the student in the Treeview
            found = False
            for item in self.student_tree.get_children():
                if roll_number == self.student_tree.item(item, "values")[0]:
                    found = True
                    self.student_tree.item(item, values=(roll_number, name, grade))
               
