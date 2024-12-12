import tkinter as tk
import random


root = tk.Tk()
root.title("Vizualizare Bubble sort")
canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

n = 100
data = [random.randint(5, 100) for _ in range(n)]
bar_width= canvas_width//n

def draw_bars(data, color="blue"):
    canvas.delete("all")
    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - val * 3
        x1 = (i+1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update_idletasks()

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print(data)
                draw_bars(data, color="yellow")
    draw_bars(data, color="purple")
draw_bars(data)
root.after(10, bubble_sort, data)

root.mainloop()
