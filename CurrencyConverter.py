import requests
import tkinter as tk

"""

get your api key here: https://free.currencyconverterapi.com/free-api-key

key = "your api key here"

"""


def convert(currency1,currency2,value):
    format_curr1 = f'{currency1.upper()}_{currency2.upper()}'
    format_curr2 = f'{currency2.upper()}_{currency1.upper()}'
    try:
        request_url = f"https://free.currconv.com/api/v7/convert?q={format_curr1},{format_curr2}&compact=ultra&apiKey={key}"
        response = requests.get(request_url)
        convetion_rate = response.json()[format_curr1]
        price_converted = float(value)*convetion_rate
        value_conv['text'] = f'{price_converted:.2f}'
    except:
        value_conv['text'] = 'Error'
        

root = tk.Tk()

canvas = tk.Canvas(root,width=400,height=250)
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

value = tk.Entry(frame,fg="red",font="Courier",bd=2,justify="center")
value.place(relx=0.05,rely=0.1,relwidth=0.4,relheight=0.15)
label_value = tk.Label(frame,text="Value to convert",font=("Courier",10))
label_value.place(relx=0.05,rely=0.25,relwidth=0.4,relheight=0.075)

currency1 = tk.Entry(frame,fg="red",bd=2,font="Courier",justify="center")
currency1.place(relx=0.55,rely=0.1,relwidth=0.4,relheight=0.15)
label_curr1 = tk.Label(frame,text="Current currency",font=("Courier",10))
label_curr1.place(relx=0.55,rely=0.25,relwidth=0.4,relheight=0.075)

value_conv = tk.Label(frame,font="Courier")
value_conv.place(relx=0.05,rely=0.4,relwidth=0.4,relheight=0.15)

currency2 = tk.Entry(frame,fg="red",font="Courier",bd=2,justify="center")
currency2.place(relx=0.55,rely=0.4,relwidth=0.4,relheight=0.15)
label_curr2 = tk.Label(frame,text="Currency to convert",font=("Courier",10))
label_curr2.place(relx=0.55,rely=0.55,relwidth=0.4,relheight=0.075)

Convert_button = tk.Button(frame, text="Convert",font="Courier",  fg = 'red',bd=4, command=lambda:convert(currency1.get(),currency2.get(),value.get()))
Convert_button.place(relx=0,rely=0.65,relwidth=1,relheight=0.35)

root.mainloop()


