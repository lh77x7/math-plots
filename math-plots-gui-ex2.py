from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')
axis = fig.add_subplot(111) # 1 row, 1 column

xValues = [1, 3, 5, 7]
yValues0 = [6, 8, 10, 12]
yValues1 = [2, 4, 6, 8]
yValues2 = [3, 5, 7, 9]

t0, = axis.plot(xValues, yValues0)
t1, = axis.plot(xValues, yValues1)
t2, = axis.plot(xValues, yValues2)

axis.set_ylabel('Y label')
axis.set_xlabel('X label')
#scalling y label
#axis.set_ylim(2, 8)
axis.grid()

fig.legend((t0, t1, t2), ('1st line', '2nd line', '3hd line'), 'upper right')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas ._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()
