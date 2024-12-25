import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = str(eval(expression))  # Evaluating the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget (where the user inputs expressions)
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button text and create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, font=("Arial", 18), width=5, height=2, 
              command=lambda b=button: button_click(b) if b not in ['=', 'C'] else button_equal() if b == '=' else button_clear()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
