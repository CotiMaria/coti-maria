import tkinter as tk
import random


class SelectionSortVisualizer:
    def __init__(self, root, array):
        self.root = root
        self.array = array
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()
        self.bar_width = 600 // len(array)
        self.i = 0  # Index for outer loop
        self.j = self.i + 1  # Index for inner loop
        self.min_idx = self.i

    def draw_array(self, highlight_indices=[]):
        self.canvas.delete("all")
        for i, val in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = 400 - val * 20
            x1 = (i + 1) * self.bar_width
            y1 = 400
            color = 'pink' if i in highlight_indices else 'purple'
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')
        self.root.update_idletasks()

    def selection_sort_step(self):
        n = len(self.array)
        if self.i < n - 1:
            if self.j < n:
                self.draw_array(highlight_indices=[self.i, self.j])
                if self.array[self.j] < self.array[self.min_idx]:
                    self.min_idx = self.j
                self.j += 1
            else:
                self.array[self.i], self.array[self.min_idx] = self.array[self.min_idx], self.array[self.i]
                self.draw_array(highlight_indices=[self.i, self.min_idx])
                self.i += 1
                self.j = self.i + 1
                self.min_idx = self.i
            self.root.after(200, self.selection_sort_step)
        else:
            print("Sorted array:", self.array)


if __name__ == "__main__":
    random.seed(42)
    array_to_sort = random.sample(range(1, 20), 10)
    print("Initial array:", array_to_sort)

    root = tk.Tk()
    root.title("Selection Sort Visualization")
    visualizer = SelectionSortVisualizer(root, array_to_sort)

    root.after(0, visualizer.selection_sort_step)
    root.mainloop()








