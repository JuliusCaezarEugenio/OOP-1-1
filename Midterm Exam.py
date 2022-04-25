def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp

 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32

 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15

 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return (self._temp - 32) * 5/9

 class KelvintoCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")

 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit:"))
 convert = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + "Celsius")

 tempInKelvin =  float(input("Enter the temperature in Kelvin:"))
 convert = KelvintoCelsius (tempInKelvin)
 print(str(convert.conversion()) + "Celsius")

main()

from tkinter import *
window = Tk()

window.geometry("700x400")
window. title("Midterm in OOP")


lbl = Label(window, text="Enter your fullname:",fg="red")
lbl.place(x=50, y=125)
txtfld = Entry(window, bd=3, font=("Arial",16))
txtfld.place(x=270,y=125)

def click():
    value=txtfld.get()
    txtfld2.insert(END,str(value))

btn = Button(window, text="Click to display your Fullname", fg="red",command=click)
btn.place(x=50, y=180)

txtfld2 = Entry(window, bd=3, font=("Arial",16))
txtfld2.place(x=270,y=180)

window.mainloop()

