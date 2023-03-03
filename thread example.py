import flet as ft
from threading import Thread
import time

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(text_align=ft.TextAlign.CENTER,width=500,expand=True,text_size=20,label='Time and date')
    
    def getTime():
        return time.strftime("Time is: %I:%M:%S  and date is: %Y-%m-%d")

#start thread to update time every seconds...

    def timeUpdate():
            #to update label 
        while True:
            time = getTime()
            txt_number.value=time
            page.update()

    t = Thread(target=timeUpdate, daemon=True)
    t.start()
    page.add(
            ft.Row(
                [
                    txt_number,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

ft.app(target=main)