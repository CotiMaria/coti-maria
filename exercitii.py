import tkinter as tk
from tkinter import ttk
import random


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(pady=10)

        self.algorithm_var = tk.StringVar()
        self.algorithm_menu = ttk.Combobox(
            self.controls_frame, textvariable=self.algorithm_var, values=[
                "Bubble Sort", "Selection Sort", "Insertion Sort", "Bogo Sort", "Gnome Sort"],
            state="readonly", width=15
        )
        self.algorithm_menu.set("Choose Algorithm")
        self.algorithm_menu.grid(row=0, column=0, padx=5)

        self.speed_var = tk.DoubleVar(value=0.5)
        tk.Label(self.controls_frame, text="Speed:").grid(row=0, column=1, padx=5)
        self.speed_scale = tk.Scale(
            self.controls_frame, variable=self.speed_var, from_=0.1, to=2.0, resolution=0.1,
            orient="horizontal", label="Slow <-> Fast"
        )
        self.speed_scale.grid(row=0, column=2, padx=5)

        self.num_elements_var = tk.IntVar(value=20)
        tk.Label(self.controls_frame, text="Elements:").grid(row=0, column=3, padx=5)
        self.num_elements_scale = tk.Scale(
            self.controls_frame, variable=self.num_elements_var, from_=5, to=100,
            orient="horizontal", label="5 <-> 100"
        )
        self.num_elements_scale.grid(row=0, column=4, padx=5)

        self.start_button = tk.Button(self.controls_frame, text="Start", command=self.start_sort)
        self.start_button.grid(row=0, column=5, padx=5)

        self.stop_button = tk.Button(self.controls_frame, text="Stop", command=self.stop_sort)
        self.stop_button.grid(row=0, column=6, padx=5)

        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset_array)
        self.reset_button.grid(row=0, column=7, padx=5)

        self.new_list_button = tk.Button(self.controls_frame, text="New List", command=self.generate_array)
        self.new_list_button.grid(row=0, column=8, padx=5)

        self.close_button = tk.Button(self.controls_frame, text="Close", command=self.generate_array)
        self.close_button.grid(row=0, column=9,padx=5)

        self.array = []
        self.running = False
        self.index = 0

        self.algorithm_colors = {
            "Bubble Sort": "pink",
            "Selection Sort": "green",
            "Insertion Sort": "orange",
            "Bogo Sort": "purple",
            "Gnome Sort": "teal"
        }

        self.generate_array()

    def generate_array(self):
        num_elements = self.num_elements_var.get()
        self.array = [random.randint(10, 400) for _ in range(num_elements)]
        self.draw_array()

    def draw_array(self, highlight_index=None, color="blue"):
        self.canvas.delete("all")
        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)
        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            bar_color = color if i != highlight_index else "red"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=bar_color)
            self.canvas.create_text(
                (x0 + x1) // 2, y0 - 10, text=str(value), font=("Arial", 8), fill="black"
            )

    def is_sorted(self):
        return all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1))

    def start_sort(self):
        self.running = True
        algorithm = self.algorithm_var.get()
        selected_color = self.algorithm_colors.get(algorithm, "blue")  # Default color is blue
        if algorithm == "Bubble Sort":
            self.bubble_sort(0, 0, selected_color)
        elif algorithm == "Selection Sort":
            self.selection_sort(0, 1, selected_color)
        elif algorithm == "Insertion Sort":
            self.insertion_sort(1, selected_color)
        elif algorithm == "Bogo Sort":
            self.bogo_sort(selected_color)
        elif algorithm == "Gnome Sort":
            self.gnome_sort(0, selected_color)

    def stop_sort(self):
        self.running = False

    def reset_array(self):
        self.stop_sort()
        self.generate_array()

    def bubble_sort(self, i, j, color):
        if not self.running:
            return
        if i < len(self.array) - 1:
            if j < len(self.array) - i - 1:
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                self.draw_array(j, color)
                self.root.after(int(self.speed_var.get() * 100), self.bubble_sort, i, j + 1, color)
            else:
                self.bubble_sort(i + 1, 0, color)
        else:
            self.running = False

    def selection_sort(self, i, j, color):
        if not self.running:
            return
        if i < len(self.array) - 1:
            min_idx = i
            for k in range(i + 1, len(self.array)):
                if self.array[k] < self.array[min_idx]:
                    min_idx = k
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array(i, color)
            self.root.after(int(self.speed_var.get() * 100), self.selection_sort, i + 1, i + 2, color)
        else:
            self.running = False

    def insertion_sort(self, i, color):
        if not self.running:
            return
        if i < len(self.array):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array(i, color)
            self.root.after(int(self.speed_var.get() * 100), self.insertion_sort, i + 1, color)
        else:
            self.running = False

    def bogo_sort(self, color):
        if not self.running:
            return
        if not self.is_sorted():
            random.shuffle(self.array)
            self.draw_array(color=color)
            self.root.after(int(self.speed_var.get() * 500), self.bogo_sort, color)
        else:
            self.running = False

    def gnome_sort(self, i, color):
        if not self.running:
            return
        if i < len(self.array):
            if i == 0 or self.array[i] >= self.array[i - 1]:
                i += 1
            else:
                self.array[i], self.array[i - 1] = self.array[i - 1], self.array[i]
                i -= 1
            self.draw_array(i, color)
            self.root.after(int(self.speed_var.get() * 100), self.gnome_sort, i, color)
        else:
            self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
