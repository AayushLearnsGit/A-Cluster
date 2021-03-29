import io
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


def results(term):
    print(term)
    url = f"http://www.omdbapi.com/?t={term}&apikey=4846248f"
    data = requests.get(url)
    data = data.json()

    root = tk.Tk()
    root.title("Result")
    root.geometry('1000x1000')

    if not eval(data['Response']):
        root.withdraw()
        messagebox.showerror('Not Found', "The movie title you've entered is not valid")
        root.destroy()
    else:
        canvas = tk.Canvas(root, width= 350, height= 500)
        canvas.place(x= 350, y= 10)

        img_url = data['Poster']
        img = requests.get(img_url)
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(img.content)))
        canvas.create_image(20, 20, anchor=tk.NW, image=img)

        tk.Label(text= data['Title'], font= ('Consolas', 30, 'bold')).place(x= 10, y= 550)
        tk.Label(text= f"Year: {data['Year']}", font= ('Consolas', 20)).place(x= 10, y= 600)
        tk.Label(text= f"Genre:           {data['Genre']}", font= ('Consolas', 20)).place(x= 10, y= 700)
        tk.Label(text= f"Director:        {data['Director']}", font= ('Consolas', 20)).place(x= 10, y= 800)
        tk.Label(text= f"Imdb Rating:     {data['imdbRating']}", font= ('Consolas', 20)).place(x= 10, y= 900)
    root.mainloop()