# **Brief Description of the Program**

This program creates a **Graphical User Interface (GUI)** for managing user information using **SQLite** as the database and **Tkinter** for the user interface in Python. The application allows users to perform operations such as inputting, searching, editing, deleting, and displaying records.

---

## **Program Overview**

1. **Database Connection**  
   - Connects to (or creates) an SQLite database named `user_data.db`.
   - Creates a table named `users` if it doesn’t already exist. The table has fields:  
     - `first_name`  
     - `last_name`  
     - `email`  
     - `national_id`  
     - `id_number`  
     - `address`

2. **Data Entry**  
   - Provides input fields for user information.  
   - Users can save data by clicking the **"Submit"** button.  
   - Ensures required fields like name and email are filled. Otherwise, an error message is shown.

3. **Search Functionality**  
   - Allows users to search by **first name** or **last name**.  
   - Displays matching results in a listbox.

4. **Edit Functionality**  
   - Users can select a record from the displayed list, and its details are loaded into input fields.  
   - Changes can be made, and the **"Update Record"** button saves these modifications to the database.

5. **Delete Functionality**  
   - Users can select and delete a record using the **"Delete"** button.  
   - The record is removed from both the database and the displayed list.

6. **Program Exit Management**  
   - Ensures the database connection is properly closed when the program exits.

---

## **Main Components of the GUI**

- **Input Fields:**  
  - Fields for entering details such as name, email, national ID, etc.
- **Result Listbox:**  
  - Displays the search results or all saved records.
- **Buttons:**  
  - **"Submit"**: Save new data.  
  - **"Search"**: Retrieve data based on input.  
  - **"Delete"**: Remove a selected record.  
  - **"Edit"**: Modify an existing record.

---

## **Applications**

- A simple data management system for small projects.  
- An educational tool for learning **databases** and **GUIs** in Python.  
- Basic software for personal or organizational record-keeping.
