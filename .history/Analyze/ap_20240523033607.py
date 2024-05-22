import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import FancyBboxPatch

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

def on_plot_hover(event):
    if event.inaxes == bar_ax:
        for bar in bar_ax.containers:
            for rect in bar:
                if rect.contains(event)[0]:
                    rect.set_alpha(0.7)
                    value = rect.get_height()
                    bar_ax.annotate(f"{value:.2f}%", (rect.get_x() + rect.get_width() / 2, rect.get_height()), 
                                    ha='center', va='bottom')
                else:
                    rect.set_alpha(1)
    else:
        pass

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

    bg_color = "#2E2E2E" if dark_mode.get() else "#FFFFFF"
    text_color = "#FFFFFF" if dark_mode.get() else "#000000"

    # Pie chart
    pie_figure = plt.Figure(figsize=(4, 3), dpi=100, facecolor=bg_color)
    pie_ax = pie_figure.add_subplot(111)
    sizes = [relevance_percentage, 100 - relevance_percentage]
    colors = ['#FFD700', '#FF6347'] if dark_mode.get() else ['gold', 'lightcoral']
    explode = (0.1, 0)
    pie_ax.pie(sizes, explode=explode, colors=colors, shadow=True, startangle=140)
    pie_ax.axis('equal')
    pie_ax.set_title('Relevance Distribution', color=text_color)
    pie_canvas = FigureCanvasTkAgg(pie_figure, chart_frame)
    pie_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    pie_canvas.mpl_connect('motion_notify_event', on_plot_hover)

    # Bar chart
    bar_figure = plt.Figure(figsize=(4, 3), dpi=100, facecolor=bg_color)
    bar_ax = bar_figure.add_subplot(111)
    labels = ['Relevance', 'Non-Relevance']
    rects = bar_ax.bar(labels, sizes, color=colors)
    bar_ax.set_ylim(0, 100)
    bar_ax.set_ylabel('Percentage', color=text_color)
    bar_ax.set_title('Relevance Comparison', color=text_color)
    bar_ax.tick_params(axis='x', colors=text_color)
    bar_ax.tick_params(axis='y', colors=text_color)
    for rect in rects:
        height = rect.get_height()
        bar_ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    f'{height:.2f}%', ha='center', va='bottom', color=text_color)
    bar_canvas = FigureCanvasTkAgg(bar_figure, chart_frame)
    bar_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    bar_canvas.mpl_connect('motion_notify_event', on_plot_hover)

    # Line chart (no hover effect)
    line_figure = plt.Figure(figsize=(4, 3), dpi=100, facecolor=bg_color)
    line_ax = line_figure.add_subplot(111)
    line_ax.plot(labels, sizes, marker='o', linestyle='-', color='b')
    line_ax.set_ylim(0, 100)
    line_ax.set_ylabel('Percentage', color=text_color)
    line_ax.set_title('Relevance Trend', color=text_color)
    line_ax.tick_params(axis='x', colors=text_color)
    line_ax.tick_params(axis='y', colors=text_color)
    line_canvas = FigureCanvasTkAgg(line_figure, chart_frame)
    line_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def toggle_dark_mode():
    bg_color = "#2E2E2E" if dark_mode.get() else "#FFFFFF"
    fg_color = "#FFFFFF" if dark_mode.get() else "#000000"
    root.config(bg=bg_color)
    frame.config(style='Dark.TFrame' if dark_mode.get() else 'Light.TFrame')
    file1_label.config(background=bg_color, foreground=fg_color)
    file2_label.config(background=bg_color, foreground=fg_color)
    relevance_label.config(background=bg_color, foreground=fg_color)
    analyze_button.config(style='Dark.TButton' if dark_mode.get() else 'Light.TButton')
    chart_frame.config(style='Dark.TFrame' if dark_mode.get() else 'Light.TFrame')

def on_enter(e):
    e.widget['background'] = '#555555'

def on_leave(e):
    e.widget['background'] = '#333333' if dark_mode.get() else '#DDDDDD'

# UI setup
root = tk.Tk()
root.title("Data Relevance Analyzer")
root.geometry("800x600")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14))
style.configure("TFrame", background="#FFFFFF")
style.configure("Dark.TFrame", background="#2E2E2E")
style.configure("Dark.TButton", background="#2E2E2E", foreground="#FFFFFF")
style.configure("Light.TButton", background="#FFFFFF", foreground="#000000")

dark_mode = tk.BooleanVar()

frame = ttk.Frame(root, padding="10", style='Light.TFrame')
frame.pack(fill=tk.BOTH, expand=True)

file1_var = tk.StringVar()
file2_var = tk.StringVar()

file1_label = ttk.Label(frame, text="Select File 1:", background="#FFFFFF", foreground="#000000")
file1_label.grid(row=0, column=0, sticky=tk.W, pady=(10, 5))

file1_entry
