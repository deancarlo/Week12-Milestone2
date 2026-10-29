import os 
import tkinter as tk 
from tkinter import messagebox 

import django 


# Connect Tkinter with Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from employees.models import Employee


#Create Main Window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("650x600")
root.resizable(False, False)

#Application Heading 
title_label = tk.Label(
    root,
    text="Employee Management System",
    font=("Arial", 18, "bold"),
)

title_label.pack(pady=15)


#Employee name input
name_label = tk.Label(root, text="Employee Name:")
name_label.pack()

name_entry = tk.Entry(root, width=45)
name_entry.pack(pady=5)

#Employee position input
position_label = tk.Label(root, text="Position:")
position_label.pack()

position_entry = tk.Entry(root, width=45)
position_entry.pack(pady=5)

#Display employee list
records_label = tk.Label(
    root, 
    text="Employee Records:",
    font=("Arial", 11, "bold"),
)
records_label.pack(pady=10)

employees_list = tk.Listbox(root, width=75, height=12)
employees_list.pack(pady=5)

#Display records from Django database
def load_employees():
    employees_list.delete(0, tk.END)

    employees = Employee.objects.all().order_by("id")

    for employee in employees:
        employees_list.insert(
            tk.END,
            f"ID: {employee.id} | "
            f"Name: {employee.name} | "
            f"Position: {employee.position} | "
            f"Hired: {employee.date_hired.strftime('%Y-%m-%d')}"
        )
    # Add a new employee
def add_employee():
    name = name_entry.get().strip()
    position = position_entry.get().strip()

    if not name and not position:
        messagebox.showerror(
            "Validation Error",
            "Please enter the employee name and position."
        )

    elif not name:
        messagebox.showerror(
            "Validation Error",
            "Employee name cannot be blank."
        )

    elif not position:
        messagebox.showerror(
            "Validation Error",
            "Employee position cannot be blank."
        )

    else:
        try:
            Employee.objects.create(
                name=name,
                position=position
            )

            messagebox.showinfo(
                "Success",
                "Employee added successfully!"
            )

            name_entry.delete(0, tk.END)
            position_entry.delete(0, tk.END)

            load_employees()

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                f"Unable to save employee:\n{error}"
            )


# Buttons
add_button = tk.Button(
    root,
    text="Add Employee",
    width=20,
    command=add_employee
)
add_button.pack(pady=5)

refresh_button = tk.Button(
    root,
    text="Refresh Records",
    width=20,
    command=load_employees
)
refresh_button.pack(pady=5)


# Load existing employees when the application starts
load_employees()


# Keep the window running 
root.mainloop()