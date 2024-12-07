import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create form for user information
root = tk.Tk()
root.title("Information Entry Form")
root.geometry("600x600")

# Connect to the SQLite database
conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

# Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    national_id TEXT,
    id_number TEXT,
    address TEXT
)
''')
conn.commit()

# Labels and input fields
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_national_id.delete(0, tk.END)
    entry_id_number.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_search.delete(0, tk.END)

label_first_name = tk.Label(root, text="Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = tk.Label(root, text="LastName:")
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_national_id = tk.Label(root, text="National ID:")
label_national_id.grid(row=3, column=0, padx=10, pady=5)
entry_national_id = tk.Entry(root)
entry_national_id.grid(row=3, column=1, padx=10, pady=5)

label_id_number = tk.Label(root, text="Birth Certificate Number:")
label_id_number.grid(row=4, column=0, padx=10, pady=5)
entry_id_number = tk.Entry(root)
entry_id_number.grid(row=4, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=5, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=5, column=1, padx=10, pady=5)

# Function to save data
def save_data():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    national_id = entry_national_id.get()
    id_number = entry_id_number.get()
    address = entry_address.get()
    
    if not first_name or not last_name or not email:
        messagebox.showerror("Error", "Please fill in all required fields!")
        return
    
    cursor.execute('''
    INSERT INTO users (first_name, last_name, email, national_id, id_number, address)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, national_id, id_number, address))
    conn.commit()
    
    clear_entries()
    messagebox.showinfo("Success", "Information saved successfully.")

# Function to search data
def search_data():
    search_term = entry_search.get()
    cursor.execute("SELECT * FROM users WHERE first_name LIKE ? OR last_name LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()
    
    listbox.delete(0, tk.END)
    for row in results:
        listbox.insert(tk.END, row)

# Function to delete a record
def delete_record():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        user_id = selected[0]
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Success", "Record deleted successfully.")

# Function to edit a record
def edit_record():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        user_id = selected[0]
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        record = cursor.fetchone()
        
        # Fill entries with selected record data
        entry_first_name.insert(0, record[1])
        entry_last_name.insert(0, record[2])
        entry_email.insert(0, record[3])
        entry_national_id.insert(0, record[4])
        entry_id_number.insert(0, record[5])
        entry_address.insert(0, record[6])
        
        # Update database on save
        def update_record():
            updated_data = (
                entry_first_name.get(),
                entry_last_name.get(),
                entry_email.get(),
                entry_national_id.get(),
                entry_id_number.get(),
                entry_address.get(),
                user_id
            )
            cursor.execute('''
            UPDATE users
            SET first_name = ?, last_name = ?, email = ?, national_id = ?, id_number = ?, address = ?
            WHERE id = ?
            ''', updated_data)
            conn.commit()
            messagebox.showinfo("Success", "Record updated successfully.")
            clear_entries()
            update_button.destroy()
        
        update_button = tk.Button(root, text="Update Record", command=update_record)
        update_button.grid(row=7, column=1, pady=10)

# Search input
label_search = tk.Label(root, text="Search:")
label_search.grid(row=6, column=0, padx=10, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search", command=search_data)
search_button.grid(row=6, column=2, padx=10, pady=5)

# Listbox to display results
listbox = tk.Listbox(root, width=80)
listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Buttons
submit_button = tk.Button(root, text="Submit", command=save_data)
submit_button.grid(row=9, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete", command=delete_record)
delete_button.grid(row=9, column=1, padx=10, pady=10)

edit_button = tk.Button(root, text="Edit", command=edit_record)
edit_button.grid(row=9, column=2, padx=10, pady=10)

# Close database connection on window close
root.protocol("WM_DELETE_WINDOW", lambda: (conn.close(), root.destroy()))

# MainLoop
root.mainloop()
