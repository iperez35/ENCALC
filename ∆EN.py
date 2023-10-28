import tkinter as tk
import time


def calculate_electronegativity():
    value1 = entry1.get().strip()
    value2 = entry2.get().strip()
    entry1.focus_set() 

    # Define a dictionary mapping element names (case-insensitive) to electronegativity values
    elements = {
        'hydrogen': 2.20,
        'helium': 0.00,
        'lithium': 0.98,
        'beryllium': 1.57,
        'boron': 2.04,
        'carbon': 2.55,
        'nitrogen': 3.04, 
        'oxygen': 3.44,
        'fluorine': 3.98,
    }

    time.sleep(1)

    # Initialize electronegativity values
    element1_value = None
    element2_value = None

    # Check if the user input is an element name and convert to lowercase
    if value1.lower() in elements:
        element1_value = elements[value1.lower()]
    elif value1.replace(".", "", 1).isdigit():
        element1_value = float(value1)

    if value2.lower() in elements:
        element2_value = elements[value2.lower()]
    elif value2.replace(".", "", 1).isdigit():
        element2_value = float(value2)

    if element1_value is not None and element2_value is not None:
        electro_value = abs(element1_value - element2_value)

        result_label.config(text=f"Electronegativity Difference = {electro_value:.2f}", font=20)

        # Classify based on electro_value
        if electro_value > 3.21:
            classification_label.config(text="That's not a possible value", font=20)

        elif abs(electro_value - 1.78) < 0.01:
            classification_label.config(text="The bond between these two elements is highly Polar Covalent. Despite being above 1.7, there is not a complete transfer of electrons, hence the molecule is Polar Covalent, rather than Ionic.", font=20, wraplength=475)

        elif electro_value >= 0.5 and electro_value <= 1.7:
            classification_label.config(text="The bond between these two elements is Polar Covalent", font=20)

        elif electro_value > 1.7:
            classification_label.config(text="The bond between these two elements is Ionic", font=20)

        elif electro_value < 0.5:
            classification_label.config(text="The bond between these two elements is Nonpolar Covalent", font=20)
            
    else:
        classification_label.config(text="Error: Invalid Input", font=20)

root = tk.Tk()
root.geometry("800x500")
root.title("ELECTRONEGATIVITY")
root.configure()

Label = tk.Label(root, text="ELECTRONEGATIVITY CALCULATOR", font=('Arial', 25, ), border=2)
Label.pack(padx=20, pady=45)

entry1_label = tk.Label(root, text="Electronegativity Value or Elemental Name", font=('Arial', 20))
entry1_label.pack(padx=20, pady=20)
entry1 = tk.Entry(root)
entry1.pack()

entry2_label = tk.Label(root, text="Electronegativity Value or Elemental Name", font=('Arial', 20))
entry2_label.pack(padx=20, pady=20)
entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="∆EN", command=calculate_electronegativity)
calculate_button.pack(padx=20, pady=20)

result_label = tk.Label(root, text="----------------------------------")
result_label.pack()

classification_label = tk.Label(root, text="")
classification_label.pack() 

root.mainloop()

