from tkinter import *
import csv
import main
import lib.GoogleMapDownloader
from tkinter import messagebox


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        Label(text='Enter your Api-Key :', fg="blue", font=("Dubai", 12)).pack(side=TOP, padx=5, pady=5)
        self.api = Entry(root, width=45)
        self.api.pack(side=TOP, padx=5, pady=5)

        Label(text=' Enter decimal coordinates ', fg="blue",font=("Dubai", 13)).pack(side=TOP, padx=0, pady=0)


        Label(text='Latitude :',fg="blue",font=("Dubai", 12)).pack(side=TOP, padx=5, pady=5)
        self.lat = Entry(root, width=30)
        self.lat.pack(side=TOP, padx=5, pady=5)

        Label(text='Longitude :',fg="blue",font=("Dubai", 12)).pack(side=TOP, padx=6, pady=6)
        self.lon = Entry(root, width=30)
        self.lon.pack(side=TOP, padx=6, pady=6)

        self.b = Button(root, text='Submit',bg="green",fg="white",font=("Dubai", 12),width=20,height=1, command=self.run)
        self.b.pack(side=TOP,padx=7,pady=7)


    def run(self):

        strlat = self.lat.get()
        strlon = self.lon.get()

        if (("N" in strlat) and ("W" in strlon)):
            with open(r'C:\Users\moham\PycharmProjects\SatelliteImageDownloader-main\HighResGoogleMapsDownloader\datasets_positive\airport-data.csv','a', newline='') as f:
                w = csv.writer(f)
                w.writerow([self.lat.get(),self.lon.get(),1,2,self.api.get()])
            lib.CoordinateConverter.func1()



        else:
            with open(r'C:\Users\moham\PycharmProjects\SatelliteImageDownloader-main\HighResGoogleMapsDownloader\datasets_positive\airport-data.csv','a', newline='') as f:
                w = csv.writer(f)
                w.writerow([1,2,self.lat.get(),self.lon.get(),self.api.get()])

        main.func2()





if __name__ == "__main__":
    root=Tk()
    root.title('Runways Detector')
    root.geometry('400x550')
    image = PhotoImage(file="download.png")
    img_resize = image.subsample(1,1)
    Label(root, image=img_resize, bg="white").pack(pady=5)
    app = App(master=root)
    app.mainloop()
    root.mainloop()








