from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import glob


root = Tk()
# root.title('Title')
# root.iconbitmap('tiktok_logo.png')



folder = '/home/manju/Desktop/delete/' 

res = [i for i in glob.glob(folder+'*jpg')]

image_list = []

count = 0
for img in res:

	count += 1
	image = img

	image = ImageTk.PhotoImage(Image.open(img).resize((700,500),Image.ANTIALIAS))
	image_list.append(image)
	



my_label = Label(image=image)
my_label.grid(row=0, column=0, columnspan=3)

status_bar = Label(text="Image 1 of "+str(len(image_list)),bd=3, pady=20)
status_bar.grid(row=2,column=2)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])


	status_bar = Label(text=f"Image {image_number} of {len(image_list)} ",bd=3, pady=20)
	status_bar.grid(row=2,column=2)



	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == len(image_list):
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))


	status_bar = Label(text=f"Image {image_number} of {len(image_list)} ",bd=3, pady=20)
	status_bar.grid(row=2,column=2)

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)



button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# lle00070 

root.mainloop()