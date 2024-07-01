from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
 
# time function used to calculate time
from time import time
 
# creating tkinter window
root = Tk()
 
button = Button(root, text = 'Geeks')
button.pack(side = TOP, pady = 5)
 
print('Running...')
# Calculating starting time
start = time()
root.after(5000, root.destroy)
 
mainloop()
 
# calculating end time
end = time()
print('Destroyed after % d seconds' % (end-start))
 