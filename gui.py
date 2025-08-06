"""
GUI to check quality of molecular primers for cloning
"""
import tkinter as tk
from main import check_primer_quality

#Get user input and check primer quality
def check_user_primer():
    user_primer = entry.get()
    result = check_primer_quality(user_primer)
    result_label.config(text=result)


#Set GUI up
window = tk.Tk()
window.title("PrimerBuilder")
window.geometry("500x300")
window.resizable(False, False)

#input labels and fields
entry_label = tk.Label(window, text="Enter the primer sequence:")
entry_label.pack(pady=5)



entry = tk.Entry(window, width=30)
entry.pack(pady=5)

#Button logic
check_button = tk.Button(window, text="Check Primer", command=check_user_primer)
check_button.pack(pady=10)

#Label for result
result_label = tk.Label(window, text="", wraplength=500, justify="center")
result_label.pack(pady=5)

#Fire up GUI
window.mainloop()



