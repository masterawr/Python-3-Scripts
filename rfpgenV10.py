import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
import re
import webbrowser
import os

# Function to load clauses from an Excel file
def load_clauses_from_excel(file_path):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        # Convert the DataFrame to a dictionary
        clauses_dict = dict(zip(df['Clause Title'], df['Clause Content']))
        return clauses_dict
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load clauses from Excel: {e}")
        return {}

# Extract placeholders using a regular expression
def extract_placeholders(clauses):
    placeholders = set()
    placeholder_pattern = r"\{\{(.*?)\}\}"  # Matches text inside double curly braces
    for text in clauses.values():
        matches = re.findall(placeholder_pattern, text)
        placeholders.update(matches)
    return placeholders

# Function to update placeholder inputs based on selected clauses
def update_placeholder_inputs():
    # Clear existing placeholder entries
    for frame in placeholder_entries.values():
        frame.destroy()
    placeholder_entries.clear()

    # Show or hide existing placeholder entries based on selected checkboxes
    for clause, var in clause_checkboxes.items():
        if var.get():  # If the checkbox is selected
            clause_placeholders = extract_placeholders({clause: clauses[clause]})
            for placeholder in clause_placeholders:
                if placeholder not in placeholder_entries:
                    # Create a new frame for the label and entry
                    frame = tk.Frame(placeholder_frame)
                    frame.pack(anchor="w", pady=2)
                    
                    placeholder_label = tk.Label(frame, text=f"Enter value for {{{{ {placeholder} }}}}:")
                    placeholder_label.pack(side="left")
                    
                    entry = tk.Entry(frame)
                    entry.pack(side="left")
                    
                    placeholder_entries[placeholder] = frame  # Store the frame in the dictionary

# Function to generate the contract with header-based numbering
def generate_contract(preview=False):
    # Get user inputs for placeholders
    user_inputs = {placeholder: entry.winfo_children()[1].get() for placeholder, entry in placeholder_entries.items()}

    # Generate the HTML content
    html_content = "<html>\n<head><title>Contract</title>\n"
    
    # Add external CSS if provided
    if css_file_path:
        html_content += f'<link rel="stylesheet" type="text/css" href="{css_file_path}">\n'
    html_content += "</head>\n<body>\n<h1>Contract</h1>\n"

    # Generate Table of Contents (TOC)
    html_content += "<h2>Table of Contents</h2>\n<ul>\n"
    h1_counter = 0
    h2_counter = 0

    # First pass: Collect TOC entries
    toc_entries = []
    for clause, text in clauses.items():
        if clause_checkboxes[clause].get():
            # Remove "**OPTIONAL**" from the clause title
            clause = clause.replace("**OPTIONAL**", "").strip()

            # Determine the header type based on the clause title
            if clause.startswith("<h1>"):
                h1_counter += 1
                h2_counter = 0  # Reset h2 counter
                toc_entries.append(f"<li><a href='#h1-{h1_counter}'>{h1_counter}.0 {clause[4:]}</a></li>\n")
            elif clause.startswith("<h2>"):
                h2_counter += 1
                toc_entries.append(f"<li><a href='#h2-{h1_counter}-{h2_counter}'>{h1_counter}.{h2_counter} {clause[4:]}</a></li>\n")

    # Add TOC entries to the HTML content
    html_content += "".join(toc_entries)
    html_content += "</ul>\n"

    # Second pass: Generate the main content
    h1_counter = 0
    h2_counter = 0
    h3_counter = 0

    for clause, text in clauses.items():
        # Check if the clause is selected
        if clause_checkboxes[clause].get():
            for placeholder, user_input in user_inputs.items():
                text = text.replace(f"{{{{{placeholder}}}}}", user_input)

            # Remove "**OPTIONAL**" from the clause title and content
            clause = clause.replace("**OPTIONAL**", "").strip()
            text = text.replace("**OPTIONAL**", "").strip()

            # Determine the header type based on the clause title
            if clause.startswith("<h1>"):  # Example condition for <h1>
                h1_counter += 1
                h2_counter = 0  # Reset h2 counter
                h3_counter = 0  # Reset h3 counter
                html_content += f"<h1 id='h1-{h1_counter}'>{h1_counter}.0 {clause[4:]}</h1>\n<p>{text}</p>\n"
            elif clause.startswith("<h2>"):  # Example condition for <h2>
                h2_counter += 1
                h3_counter = 0  # Reset h3 counter
                html_content += f"<h2 id='h2-{h1_counter}-{h2_counter}'>{h1_counter}.{h2_counter} {clause[4:]}</h2>\n<p>{text}</p>\n"
            elif clause.startswith("<h3>"):  # Example condition for <h3>
                h3_counter += 1
                html_content += f"<h3>{h1_counter}.{h2_counter}.{h3_counter} {clause[4:]}</h3>\n<p>{text}</p>\n"

    html_content += "</body>\n</html>"

    # Save the HTML content to a file
    with open("contract.html", "w") as file:
        file.write(html_content)

    if not preview:
        messagebox.showinfo("Success", "Contract has been generated and saved as 'contract.html'.")
    else:
        # Open the generated HTML file in the default web browser for preview
        webbrowser.open("file://" + os.path.abspath("contract.html"))

# Function to select an external CSS file
def select_css_file():
    global css_file_path
    css_file_path = filedialog.askopenfilename(
        title="Select a CSS File",
        filetypes=[("CSS Files", "*.css")]
    )
    if css_file_path:
        messagebox.showinfo("CSS File Selected", f"Using CSS file: {css_file_path}")

# Load clauses from the Excel file
excel_file_path = "clauses.xlsx"  # Replace with the path to your Excel file
clauses = load_clauses_from_excel(excel_file_path)

# Create the GUI
root = tk.Tk()
root.title("Contract Generator")

# Use grid layout for better organization
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Frame for clause checkboxes (left side)
clause_frame = tk.Frame(root)
clause_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

tk.Label(clause_frame, text="Select clauses to include:").pack(anchor="w")

clause_checkboxes = {}
placeholder_entries = {}

for clause in clauses.keys():
    var = tk.BooleanVar(value=True)  # Default to include all clauses
    checkbox = tk.Checkbutton(clause_frame, text=clause, variable=var, command=update_placeholder_inputs)
    checkbox.pack(anchor="w")
    clause_checkboxes[clause] = var

# Frame for placeholder inputs (right side)
placeholder_frame = tk.Frame(root)
placeholder_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

tk.Label(placeholder_frame, text="Enter placeholder values:").pack(anchor="w")

# Initialize placeholder entries
update_placeholder_inputs()  # Call this to show placeholders for all selected clauses

# Buttons on the right side (below placeholder values)
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=1, sticky="e", padx=10, pady=10)

# Button to select an external CSS file
css_file_path = None  # Global variable to store the CSS file path
css_button = tk.Button(button_frame, text="Select CSS File", command=select_css_file)
css_button.pack(side="top", pady=5)

# Preview button
preview_button = tk.Button(button_frame, text="Preview Contract", command=lambda: generate_contract(preview=True))
preview_button.pack(side="top", pady=5)

# Generate button
generate_button = tk.Button(button_frame, text="Generate Contract", command=lambda: generate_contract(preview=False))
generate_button.pack(side="top", pady=5)

root.mainloop()
