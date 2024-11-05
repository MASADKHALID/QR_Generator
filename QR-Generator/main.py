#import libraries
import os                 # for chech file path
import tkinter as tk     #for gui
import qrcode      #for qr
from tkinter import filedialog # for download
# class 
class qrGenerator():
    #constructor
    def __init__(self,root):
        self.root=root
        self.img=None
        self.url=None
        #window icon image
        self.p1 = tk.PhotoImage(file = 'icon.PNG') 
        root.iconphoto(False,self.p1)
        #qr detail
        self.qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=5,border=4)
        # menubar
        self.menubar = tk.Menu(root)
        # menubar file
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Exit",command=quit) 
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # menubar problem
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Contact")
        self.helpmenu.add_command(label="Help Online")
        self.helpmenu.add_command(label="Demo")
        self.menubar.add_cascade(label="Problem?", menu=self.helpmenu)

        root.config(menu=self.menubar)
        #heading
        self.head_label=tk.Label(root,text="QR-Generator")
        # Entry
        self.entry=tk.Entry(root,bg="white",width=40,)
        # Enter button
        self.button=tk.Button(root,background="black",foreground="white",text="Enter",command=self.getQrCode)

        
        # widgets grid loacation
        self.head_label.grid(row=0,column=0,padx=10, pady=5)
        self.entry.grid(row=1,column=0,padx=30, pady=20)
        self.button.grid(row=1,column=1,padx=20, pady=20)
        
    # function
    def getQrCode(self):
        # get entry text
        self.url=self.entry.get()
        #qr genereate
        self.qr.add_data(self.url)
        self.qr.make(fit=True)
        self.img = self.qr.make_image(fill_color="black", back_color="white")
        #qr name
        file_path = "QR.png"
    
        # Save QR code to file, replacing it if it already exists
        if os.path.exists(file_path):
            os.remove(file_path)
        self.img.save(file_path)

        # Load and display the QR code image in the Tkinter window
        image = tk.PhotoImage(file=file_path)
        self.img_label = tk.Label(root)
        self.img_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
        self.img_label.config(image=image)
        self.img_label.image = image 

        # Download Button
        self.downloadButton=tk.Button(root,background="black",foreground="white",text="Download",command=self.download)
        self.downloadButton.grid(row=4,column=1,padx=20, pady=10)

    #Function
    def download(self):
    # Open a file dialog to choose save location
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.img.save(file_path)
            #confirm
            tk.messagebox.showinfo("Saved", f"QR Code saved as {file_path}")


#GUI Window
root=tk.Tk()
#GUI window title
root.title("QR-Generator")
#GUI window size
root.geometry("400x500")        
#object of class qr generatoe
obj1=qrGenerator(root)
#object callmethod
#obj1.getQrCode()
#window close
root.mainloop()
        

    

