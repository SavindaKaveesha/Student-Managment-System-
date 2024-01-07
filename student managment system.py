import tkinter as tk
from tkinter import ttk, messagebox

class StudentManagementSystem:
    def __init__(self, window):

        self.root = window
        self.root.title("Student Management System")
        self.root.geometry("1024x480")
        
        # align center of the window
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - 1024) // 2
        y = (screen_height - 600) // 2
        window.geometry(f"1024x600+{x}+{y}")
    
        label_font = ("Helvetica", 16, "bold")
        
        label = tk.Label(window, text="Student Management System",fg="white",bg="#373a52", width=1024, height=3, font=label_font)
        label.pack(side="top", fill="both")
        
        self.group_frame = tk.Frame(window)
        self.group_frame.pack(side="left", padx=10, pady=10, anchor="nw")
        
        self.group_box = tk.LabelFrame(self.group_frame, text="Student Information")
        self.group_box.pack(padx=10, pady=10, anchor="w")

        
    #label and textbox
        self.ID_label = tk.Label(self.group_box, text="ID:")
        self.ID_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.group_box)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        
        self.name_labe2 = tk.Label(self.group_box, text="Name:")
        self.name_labe2.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.group_box)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        
        self.gender_labe2 = tk.Label(self.group_box, text="Gender:")
        self.gender_labe2.grid(row=2, column=0, padx=5, pady=5)

    # Dropdown menu
        options = ["Male", "Female"]

        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])

        self.dropdown_menu = tk.OptionMenu(self.group_box, self.selected_option, *options)
        self.dropdown_menu.grid(row=2, column=0, columnspan=2, pady=10)

        
    #label and textbox
        self.age_labe2 = tk.Label(self.group_box, text="Age:")
        self.age_labe2.grid(row=3, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.group_box)
        self.age_entry.grid(row=3, column=1, padx=5, pady=5)
        
        
        
        self.date_labe2 = tk.Label(self.group_box, text="En-Date:")
        self.date_labe2.grid(row=4, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.group_box)
        self.date_entry.grid(row=4, column=1, padx=5, pady=5)
        
        
        self.midterm_labe2 = tk.Label(self.group_box, text="Midterm:")
        self.midterm_labe2.grid(row=5, column=0, padx=5, pady=5)
        self.midterm_entry = tk.Entry(self.group_box)
        self.midterm_entry.grid(row=5, column=1, padx=5, pady=5)
        
        
        self.final_labe2 = tk.Label(self.group_box, text="Final:")
        self.final_labe2.grid(row=6, column=0, padx=5, pady=5)
        self.final_entry = tk.Entry(self.group_box)
        self.final_entry.grid(row=6, column=1, padx=5, pady=5)
        
        
        self.gpa_labe2 = tk.Label(self.group_box, text="GPA:")
        self.gpa_labe2.grid(row=7, column=0, padx=5, pady=5)
        self.gpa_entry = tk.Entry(self.group_box)
        self.gpa_entry.grid(row=7, column=1, padx=10 ,pady=5)
        
    #buttons
        self.add_button = tk.Button(self.group_box, text="Add", bg="#373a52", fg="white", width=10, command = self.add_student)
        self.add_button.grid(row=8, column=0, padx=5, pady=10)

        self.update_button = tk.Button(self.group_box, text="Update", bg="#373a52", fg="white", width=10, command=self.update_student)
        self.update_button.grid(row=8, column=1, pady=10)
        
        self.clear_button = tk.Button(self.group_box, text="Clear", bg="#373a52", fg="white", width=10, command=self.clear_Inputes)
        self.clear_button.grid(row=9, column=0, pady=10)
        
        self.delete_button = tk.Button(self.group_box, text="Delete", bg="#373a52", fg="white", width=10, command=self.delete_student)
        self.delete_button.grid(row=9, column=1, pady=10)

        self.delete_button = tk.Button(self.group_box, text="Search", bg="#373a52", fg="white", width=10, command=self.search_student)
        self.delete_button.grid(row=10, column=0, pady=10)

        self.delete_button = tk.Button(self.group_box, text="View", bg="#373a52", fg="white", width=10)
        self.delete_button.grid(row=10, column=1, pady=10)

        self.right_frame = tk.Frame(window)
        self.right_frame.pack(side="left", padx=10, pady=10, anchor="nw")  # Use pack instead of grid


        # Treeview
        tree_columns = ("ID", "Name", "Gender", "Age", "Enroll Date", "Midterm", "Final", "GPA")
        self.student_tree = ttk.Treeview(self.right_frame, columns=tree_columns, show="headings", selectmode="browse")

        # Set column headings
        for col in tree_columns:
            self.student_tree.heading(col, text=col)
            self.student_tree['height'] = 15

        # Set column widths
        for col in tree_columns:
            self.student_tree.column(col, width=100)

        self.student_tree.pack(pady=10)


    def add_student(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        enDate = self.date_entry.get()
        midterm = self.midterm_entry.get()
        final = self.final_entry.get()
        gpa = self.gpa_entry.get()
        gender = self.selected_option.get()

        if not id or not name or not age or not enDate or not midterm or not final or not gpa:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Add student to the Treeview
        self.student_tree.insert("", "end", values=(id,name,gender,age,enDate,midterm,final,gpa))

        self.clear_Inputes() 

    def delete_student(self):
        # Get ID to be deleted
        delete_id = self.id_entry.get()

        # Ensure an ID is provided
        if not delete_id:
            messagebox.showerror("Error", "Please enter the ID to delete.")
            return

        # Search for the student in the Treeview
        found = False
        for item in self.student_tree.get_children():
            if delete_id == self.student_tree.item(item, "values")[0]:
                found = True
                # Ask for confirmation before deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you really want to delete the student with ID: {delete_id}?")
                if confirm:
                    # Delete the student from the Treeview
                    self.student_tree.delete(item)
                    messagebox.showinfo("Deletion Successful", f"Student with ID: {delete_id} has been deleted.")
                break

        if not found:
            messagebox.showinfo("Student Not Found", f"No student found with ID: {delete_id}")


    def clear_Inputes(self):
            # Clear input fields
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.midterm_entry.delete(0, tk.END)
            self.final_entry.delete(0, tk.END)
            self.gpa_entry.delete(0, tk.END)


    def update_student(self):
        # Get ID to be updated
        update_id = self.id_entry.get()

        # Ensure an ID is provided
        if not update_id:
            messagebox.showerror("Error", "Please enter the ID to update.")
            return

        # Get updated Name and Grade
        updated_name = self.name_entry.get()
        updated_grade = self.gpa_entry.get()
        updated_age = self.age_entry.get()
        updated_date = self.date_entry.get()
        updated_midterm = self.midterm_entry.get()
        updated_final = self.final_entry.get()

        # Search for the student in the Treeview
        found = False
        for item in self.student_tree.get_children():
            if update_id == self.student_tree.item(item, "values")[0]:
                found = True
                # Update the student's information
                if updated_name:
                    self.student_tree.item(item, values=(update_id, updated_name, self.student_tree.item(item, 'values')[2], updated_age, updated_date, updated_midterm, updated_final, updated_grade))
                    messagebox.showinfo("Update Successful", f"Student with ID: {update_id} has been updated.")
                    break

        if not found:
            messagebox.showinfo("Student Not Found", f"No student found with ID: {update_id}")

    def search_student(self):
        # Get ID to be searched
        search_id = self.id_entry.get()

        # Ensure an ID is provided
        if not search_id:
            messagebox.showerror("Error", "Please enter the ID to search.")
            return

        # Search for the student in the Treeview
        found = False
        for item in self.student_tree.get_children():
            if search_id == self.student_tree.item(item, "values")[0]:
                found = True
                # Display the corresponding student's information in a messagebox
                student_info = "\n".join([f"{col}: {self.student_tree.item(item, 'values')[i]}" for i, col in enumerate(self.student_tree['columns'])])
                messagebox.showinfo("Student Information", student_info)
                break

        if not found:
            messagebox.showinfo("Student Not Found", f"No student found with ID: {search_id}")



if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
