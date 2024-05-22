import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        messagebox.showerror("File Read Error", f"Error reading file {filename}: {e}")
        return None

def calculate_relevance(text1, text2):
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio * 100

def analyze_data():
    file1_path = file1_var.get()
    file2_path = file2_var.get()
    
    if file1_path and file2_path:
        file1_data = read_file(file1_path)
        file2_data = read_file(file2_path)
        
        if file1_data is not None and file2_data is not None:
            relevance_percentage = calculate_relevance(file1_data, file2_data)
            relevance_label.config(text=f"Relevance: {relevance_percentage:.2f}%")
            display_chart(relevance_percentage)
        else:
            relevance_label.config(text="Error reading files.")
    else:
        messagebox.showwarning("Input Error", "Please select both files.")

def browse_file(var):
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    var.set(filename)

def display_chart(relevance_percentage):
    figure = plt.Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    
    labels = 'Relevance', 'Non-Relevance'
    sizes = [relevance_percentage, 100 - relevance_percentage]
    colors = ['gold', 'lightcoral']
    explode = (0.1, 0)  # explode 1st slice
    
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=140)
    
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    chart = FigureCanvasTkAgg(figure, root)
    chart.get_tk_widget().pack()

# UI setup
root = tk.Tk()
root.title("Data Relevance Analyzer")

file1_var = tk.StringVar()
file2_var = tk.StringVar()

file1_label = ttk.Label(root, text="Select File 1:")
file1_label.pack(pady=(10, 0))

file1_entry = ttk.Entry(root, textvariable=file1_var, state='readonly')
file1_entry.pack(pady=(0, 5), padx=10, fill='x', expand=True)

file1_button = ttk.Button(root, text="Browse", command=lambda: browse_file(file1_var))
file1_button.pack(pady=(0, 10), padx=10)

file2_label = ttk.Label(root, text="Select File 2:")
file2_label.pack()

file2_entry = ttk.Entry(root, textvariable=file2_var, state='readonly')
file2_entry.pack(pady=(0, 5), padx=10, fill='x', expand=True)

file2_button = ttk.Button(root, text="Browse", command=lambda: browse_file(file2_var))
file2_button.pack(pady=(0, 10), padx=10)

analyze_button = ttk.Button(root, text="Analyze Data", command=analyze_data)
analyze_button.pack(pady=10)

relevance_label = ttk.Label(root, text="")
relevance_label.pack()

root.mainloop()
