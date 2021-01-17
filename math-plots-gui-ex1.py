from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')
axis = fig.add_subplot(211)

xValues = [1, 2, 3, 4]
yValues = [3, 5, 5, 7]
axis.plot(xValues, yValues)
axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')
axis.grid(linestyle='-')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas ._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()
