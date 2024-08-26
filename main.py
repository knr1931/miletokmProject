from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

converted_km_label = Label(text="0")
converted_km_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def convert_mile_km():
    miles_inputted = float(mile_input.get())
    km_converted = round(miles_inputted * 1.609, 3)
    converted_km_label["text"] = str(km_converted)


calculate_button = Button(text="Calculate", command=convert_mile_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
