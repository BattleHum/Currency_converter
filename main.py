from tkinter import *
from tkinter import Tk, ttk
import requests
from PIL import Image, ImageTk
import json

# colors


window = Tk()
window.geometry('300x320')
window.title('Currency converter')
window.configure(bg='#AFEEEE')
window.resizable(height=False, width=False)

# frames
top = Frame(window, width=300, height=60, bg='#FF7F50')
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg='#E0FFFF')
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    convert1 = combo1.get()
    convert2 = combo2.get()
    amount = value.get()

    querystring = {"from":convert1,"to": convert2,"amount": amount}

    if convert2 == 'USD':
        symbol = '$'
    elif convert2 == 'EUR':
        symbol = '€'
    elif convert2 == 'CAD':
        symbol = 'CAD  $'
    elif convert2 == 'BRL':
        symbol = 'R$'
    elif convert2 == 'INR':
        symbol = '₹'
    elif convert2 == 'UAH':
        symbol = '₴'


    headers = {
        "X-RapidAPI-Key": "API-KEY",
        "X-RapidAPI-Host": "API-HOST"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)

# main frame
result = Label(main, compound=LEFT, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivi 15 bold'), bg='#FFFFFF',fg='#808080')
result.place(x=50, y=10)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD', 'UAH']

From_LABEL = Label(main, compound=LEFT, text="From", width=8, height=1, pady=0, relief="flat", anchor=NW, font=('Ivi 10 bold'), bg='#FFFFFF',fg='#808080')
From_LABEL.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_LABEL = Label(main, compound=LEFT, text="To", width=8, height=1, pady=0, relief="flat", anchor=NW, font=('Ivi 10 bold'), bg='#FFFFFF',fg='#808080')
to_LABEL.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg='#FF7F50', fg='#FFFFFF', font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)

window.mainloop()
