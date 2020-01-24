import tkinter
from tkinter import font
import requests


HEIGHT = 500
WIDTH = 600

def results(result):
    try:
        city = result['name']
        country = result['sys']['country']
        desc = result['weather'][0]['description']
        temp = result['main']['temp']

        final_result = f'City: {city} \nCountry: {country} \nConditions: {desc} \nTemperature(°C): {temp}'
    except:
        final_result = 'There was a problem fetching weather of the city'

    return final_result



def forecast(city):
    weather_key = '70f213c63fa5ea18064d46d56931d57d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url, params=params)
    result = response.json()

    label['text'] = results(result)



root = tkinter.Tk()
root.title('Get Report')

canvas = tkinter.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

bg_image = tkinter.PhotoImage(file='rk.png')
bg_label = tkinter.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

root_label = tkinter.Label(root, text='Get Weather Report Of The City You Want', font='Helvetica 12 bold')
root_label.place(relx = 0.1, rely=0, relwidth=0.8, relheight=0.1)

frame = tkinter.Frame(root, bg='#5bebc9', bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.075, anchor='n')

label1 = tkinter.Label(frame, text='City Name', bg='#5bebc9', font='Helvetica 12 bold')
label1.place(relwidth=0.2, relheight=1)

entry = tkinter.Entry(frame, font = 'Helvetica 12 bold')
entry.place(relx=0.25, rely=0, relwidth=0.4, relheight=1)

button= tkinter.Button(frame, text='Weather Report', font='Courier 9 bold', command=lambda: forecast(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lFrame = tkinter.Frame(root, bg='#5bebc9', bd=5)
lFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

label = tkinter.Label(lFrame, font='Helvetica 12 bold', anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()
