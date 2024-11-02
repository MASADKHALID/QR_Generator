import os
import tkinter as tk
import qrcode as qr
class qrGenerator():
    def __init__(self,root):
        self.root=root
        self.menubar = tk.Menu(root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Contact")
        self.helpmenu.add_command(label="Help Online")
        self.helpmenu.add_command(label="Demo")
        self.helpmenu.add_cascade(label="Problem?", menu=self.helpmenu)

        root.config(menu=self.menubar)

        self.entry=tk.Entry(root,bg="white",width=40)
        self.button=tk.Button(root,background="black",foreground="white",text="Enter",command=self.getQrCode)
        self.label=tk.Label(root,text="")


        self.entry.grid(row=0,column=0,padx=30, pady=20)
        self.button.grid(row=0,column=1,padx=20, pady=20)
        self.label.grid(row=1,column=0,padx=20, pady=10)

    def getQrCode(self):
        global url
        global downloadButton
        url=self.entry.get()
        self.label.config(text=f"URL Entered: {url}")
        img=qr.make(url)
        file_path = "QR.png"
    
        # Save QR code to file, replacing it if it already exists
        if os.path.exists(file_path):
            os.remove(file_path)
        img.save(file_path)

        # Load and display the QR code image in the Tkinter window
        image = tk.PhotoImage(file=file_path)
        self.img_label = tk.Label(root)
        self.img_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
        self.img_label.config(image=image)
        self.img_label.image = image 

root=tk.Tk()
root.title("QR-Generator")
root.geometry("400x400")        
obj1=qrGenerator(root)
obj1.getQrCode()
root.mainloop()
        

    

