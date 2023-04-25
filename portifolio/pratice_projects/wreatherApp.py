from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import Timezonefinder
from datetime import datetime
import requests
import pytz

root = tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)


textfield=tk.Entry(root, justify="center", width=17,font=('popins', 25, 'bold'))
textfield.place(x=50, y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon(image=Search_icon,borderwidth=0, cursor="hand2")
myimage_icon.place(x=400, y=34)








root.mainloop()