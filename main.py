import customtkinter as tk
import qrcode as qr
from PIL import Image
import os

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.user_desktop = os.path.expanduser('~\\Desktop')

        self.qr_code = None
        self.qr_link = None
        self.path = None

        self.qr_width = 300
        self.qr_height = 300
        self.button_font = ('Arial',16,'normal')

        self.title("Generate QR Code")
        self.iconbitmap('icon.ico')
        self.minsize(width=500,height=500)
        self.maxsize(width=500,height=500)
        self.config(padx=20,pady=20)

        # UI
        self.link_entry = tk.CTkEntry(self,width=460)
        self.link_entry.place(relx=0,rely=0)

        self.convert_button = tk.CTkButton(self,text="Convert text or link to Qr Code",width=200,font=self.button_font,command=self.convert_link)
        self.convert_button.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

        self.image_label = tk.CTkLabel(self)

        self.download_button = tk.CTkButton(self,text="Download Image",font=self.button_font,command=self.download_img)

        self.info_label = tk.CTkLabel(self)

    def convert_link(self):
        self.qr_link = self.link_entry.get()
        self.qr_code = qr.make(self.qr_link)

        self.path = "qr-code.png"
        self.qr_code.save(self.path)

        try:
            self.print_qrcode(self.path)
        except:
            self.image_label.configure(text="ERROR",font=('Arial',40,'bold'),text_color="red")

    def print_qrcode(self,data):
        photo_image = tk.CTkImage(dark_image=Image.open(data),size=(self.qr_width,self.qr_height))

        self.image_label.configure(self,height=self.qr_height, width=self.qr_width,text="",image=photo_image)
        self.image_label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        self.download_button.place(relx=0.5,rely=0.88,anchor=tk.CENTER)

    def download_img(self):
        try:
            copy_img = Image.open(self.path)
            copy_img.save(f"{self.user_desktop}\\QrCodeImg.png")

            self.info_label.configure(text=f"File path : {self.user_desktop}\\QrCodeImg.png\nSuccess",text_color="Light Blue", font=('Arial',18,'normal'))
        except:
            self.info_label.configure(text="Error", text_color="Red", font=('Arial',18,'normal'))
        finally:
            self.info_label.place(relx=0.5,rely=0.97,anchor=tk.CENTER)

if __name__ == "__main__":
    window = App()
    window.mainloop()