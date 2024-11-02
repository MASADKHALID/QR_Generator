## import libraries
import os
import tkinter as tk
import qrcode as qr
## initial structue
root=tk.Tk()
root.title("QR-Generator")
root.geometry("400x400")
##method
def getQrCode():
    global url
    global downloadButton
    url=entry.get()
    label.config(text=f"URL Entered: {url}")
    img=qr.make(url)
    file_path = "QR.png"
    
    # Save QR code to file, replacing it if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)
    img.save(file_path)

    # Load and display the QR code image in the Tkinter window
    image = tk.PhotoImage(file=file_path)
    img_label.config(image=image)
    img_label.image = image 

    downloadButton=tk.Button(root,background="black",foreground="white",text="Download",borderwidth=10)
    
entry=tk.Entry(root,bg="white",width=40)
button=tk.Button(root,background="black",foreground="white",text="Enter",command=getQrCode)
label=tk.Label(root,text="")


entry.grid(row=0,column=0,padx=30, pady=20)
button.grid(row=0,column=1,padx=20, pady=20)
label.grid(row=1,column=0,padx=20, pady=10)


# Placeholder label for the QR code image
img_label = tk.Label(root)
img_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
downloadButton.grid(row=3,column=3)

root.mainloop()