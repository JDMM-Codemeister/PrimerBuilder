"""
GUI to check quality of molecular primers for cloning
"""
#TODO add refresh button to screens
#TODO perform individual checks on each primer when doing dual check
#TODO make sure user can only input NT (dual primer)


import tkinter as tk
from main import check_primer_quality, is_primer_pair_compatible
from PIL import Image, ImageTk

#Get user input and check primer quality
def check_user_primer():
    user_primer = entry_a.get()
    result = check_primer_quality(user_primer)
    result_label_a.config(text=result)

def check_user_dual_primers():
    user_primer = entry_b1.get()
    user_primer2 = entry_b2.get()

    result = is_primer_pair_compatible(user_primer, user_primer2)
    result_label_b.config(text=result)

#make frame
def show_frame(frame):
    frame.tkraise()

#Set GUI up
window = tk.Tk()
window.title("PrimerBuilder")
window.geometry("500x300")
window.resizable(False, False)


#set up blank screen
blank_screen = tk.Frame(window, bg='white')
blank_screen.place(relx=0, rely=0, relheight=1, relwidth=1)

#Landing page image
cover_image_bg = Image.open("assets/Primer_bg_title_cropped4.png")
cover_image_bg = cover_image_bg.resize((500, 300), Image.LANCZOS)  # shrink or stretch
cover_image_bg_photo = ImageTk.PhotoImage(cover_image_bg)
cover_image_label =tk.Label(blank_screen, image=cover_image_bg_photo)
cover_image_label.place(x=0,y=0,relwidth=1, relheight=1);

#Set up frames
screen_a = tk.Frame(window, bg='white') #single primer
screen_b = tk.Frame(window, bg='white') #dual primer

for frame in (blank_screen, screen_a, screen_b):
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)


#input labels and fields frame A
entry_label_a = tk.Label(screen_a, text="Enter the primer sequence:", bg='white')
entry_label_a.pack(pady=5)
entry_a = tk.Entry(screen_a, width=30)
entry_a.pack(pady=5)

#Button logic
check_button_a = tk.Button(screen_a, text="Check Primer", command=check_user_primer)
check_button_a.pack(pady=10)

#Label for result
result_label_a = tk.Label(screen_a, text="", wraplength=500, justify="center", bg='white')
result_label_a.pack(pady=5)

#TODO #input labels and fields frame A
#Primer 1 fields
entry_label_b1 = tk.Label(screen_b, text="Enter the first primer sequence:", bg='white')
entry_label_b1.pack(pady=5)
entry_b1 = tk.Entry(screen_b, width=30)
entry_b1.pack(pady=5)

#Primer2 fields
entry_label_b2 = tk.Label(screen_b, text="Enter the second primer sequence:", bg='white')
entry_label_b2.pack(pady=5)
entry_b2 = tk.Entry(screen_b, width=30)
entry_b2.pack(pady=5)

check_button_b = tk.Button(screen_b, text="Check Primers", command=check_user_dual_primers)
check_button_b.pack(pady=10)

result_label_b = tk.Label(screen_b, text="", wraplength=500, justify="center", bg='white')
result_label_b.pack(pady=5)




#Create menu
menu_bar =   tk.Menu(window)
window.config(menu=menu_bar)

nav_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu', menu=nav_menu)
nav_menu.add_command(label='Single Primer Design', command=lambda: show_frame(screen_a))
nav_menu.add_command(label='Dual Primer Design', command=lambda: show_frame(screen_b))

#Show A by default
show_frame(blank_screen)


#Fire up GUI
window.mainloop()



