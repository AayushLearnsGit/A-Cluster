
import tkinter as tk
from res_page import results

def search():
    term = bar.get()
    root.destroy()
    results(term)


root = tk.Tk()
root.title('Search')
root.geometry('500x250')

tk.Label().pack()
lb = tk.Label(root, text= "Google of Movies", font= ('Consolas', 30, 'bold'))
lb.pack()
tk.Label().pack()

bar = tk.Entry(root, width= 30, font= ('Consolas', 20))
bar.pack()
tk.Label().pack()

bt = tk.Button(root, text= "Search", width= 30, height= 2, fg= 'white', bg= '#03a5fc', font= ('Consolas', 10, 'bold'), command= search)
bt.pack()

root.mainloop()