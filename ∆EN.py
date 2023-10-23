import tkinter as tk
import time

def calculate_electronegativity():
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    # Calculate the greaterValue and lesserValue
    greaterValue = max(value1, value2)
    lesserValue = min(value1, value2)

    electro_value = greaterValue - lesserValue

    time.sleep(2)
    
    result_label.config(text=f"Electronegativity Difference = {electro_value:.2f}", font=20)

    # Classify based on electro_value
    if electro_value > 3.19:
        classification_label.config(text="That's not possible value", font=20)
    elif electro_value < 0.79:
        classification_label.config(text="That's not a possible value", font=20)
    elif electro_value >= 2.0:
        classification_label.config(text="The bond between these two elements is Ionic", font=20)
    elif electro_value < 0.5:
        classification_label.config(text="The bond between these two elements is Nonpolar Covalent", font=20)
    elif electro_value >= 0.5 and electro_value < 2.0:
        classification_label.config(text="The bond between these two elements is Polar Covalent", font=20)
    else:
        classification_label.config(text="Not a possible value", font=20)

root = tk.Tk()
root.geometry("800x500")
root.title("ELECTRONEGATIVITY")
root.configure()

Label = tk.Label(root, text="ELECTRONEGATIVITY CALCULATOR", font=('Arial', 25, ))
Label.pack(padx=20, pady=45)

entry1_label = tk.Label(root, text="First Electronegativity Value", font=('Arial', 20))
entry1_label.pack(padx=20, pady=20)
entry1 = tk.Entry(root)
entry1.pack()

entry2_label = tk.Label(root, text="Second Electronegativity Value", font=('Arial', 20))
entry2_label.pack(padx=20, pady=20)
entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate Electronegativity", command=calculate_electronegativity, font=(20))
calculate_button.pack(padx=20, pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

classification_label = tk.Label(root, text="")
classification_label.pack()

root.mainloop()

