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
            display_charts(relevance_percentage)
        else:
            relevance_label.config(text="Error reading files.")
    else:
        messagebox.showwarning("Input Error", "Please select both files.")

def browse_file(var):
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    var.set(filename)

def display_charts(relevance_percentage):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Pie chart
    pie_figure = plt.Figure(figsize=(6, 4), dpi=100)
    pie_ax = pie_figure.add_subplot(111)
    labels = ['Relevance', 'Non-Relevance']
    sizes = [relevance_percentage, 100 - relevance_percentage]
    colors = ['gold', 'lightcoral']
    explode = (0.1, 0)
    pie_ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    pie_ax.axis('equal')
    pie_canvas = FigureCanvasTkAgg(pie_figure, chart_frame)
    pie_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    pie_canvas.draw()

    # Bar chart
    bar_figure = plt.Figure(figsize=(6, 4), dpi=100)
    bar_ax = bar_figure.add_subplot(111)
    bar_ax.bar(labels, sizes, color=colors)
    bar_ax.set_ylim(0, 100)
    bar_ax.set_ylabel('Percentage')
    bar_ax.set_title('Relevance between File 1 and File 2')
    for i, v in enumerate(sizes):
        bar_ax.text(i, v + 2, f"{v:.1f}%", ha='center', va='bottom')
    bar_canvas = FigureCanvasTkAgg(bar_figure, chart_frame)
    bar_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    bar_canvas.draw()

    # Line chart
    line_figure = plt.Figure(figsize=(6, 4), dpi=100)
    line_ax = line_figure.add_subplot(111)
    line_ax.plot(labels, sizes, marker='o', linestyle='-', color='b')
    line_ax.set_ylim(0, 100)
    line_ax.set_ylabel('Percentage')
    line_ax.set_title('Relevance Trend')
    line_canvas = FigureCanvasTkAgg(line_figure, chart_frame)
    line_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    line_canvas.draw()

# UI setup
root = tk.Tk()
root.title("Data Relevance Analyzer")
root.geometry("1400x800")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14))

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

file1_var = tk.StringVar()
file2_var = tk.StringVar()

file1_label = ttk.Label(frame, text="Select File 1:")
file1_label.grid(row=0, column=0, sticky=tk.W, pady=(10, 5))

file1_entry = ttk.Entry(frame, textvariable=file1_var, state='readonly')
file1_entry.grid(row=0, column=1, pady=(10, 5), padx=10, sticky=tk.EW)

file1_button = ttk.Button(frame, text="Browse", command=lambda: browse_file(file1_var))
file1_button.grid(row=0, column=2, pady=(10, 5), padx=10)

file2_label = ttk.Label(frame, text="Select File 2:")
file2_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 10))

file2_entry = ttk.Entry(frame, textvariable=file2_var, state='readonly')
file2_entry.grid(row=1, column=1, pady=(5, 10), padx=10, sticky=tk.EW)

file2_button = ttk.Button(frame, text="Browse", command=lambda: browse_file(file2_var))
file2_button.grid(row=1, column=2, pady=(5, 10), padx=10)

analyze_button = ttk.Button(frame, text="Analyze Data", command=analyze_data)
analyze_button.grid(row=2, column=0, columnspan=3, pady=20)

relevance_label = ttk.Label(frame, text="")
relevance_label.grid(row=3, column=0, columnspan=3, pady=(5, 20))

chart_frame = ttk.Frame(frame)
chart_frame.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky=tk.NSEW)

frame.columnconfigure(1, weight=1)
frame.rowconfigure(4, weight=1)

root.mainloop()
