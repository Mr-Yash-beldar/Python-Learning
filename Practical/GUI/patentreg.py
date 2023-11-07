import tkinter as tk

def save_registration():
    patient_name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    symptoms = symptoms_text.get("1.0", "end-1c")

    if patient_name and age and gender and symptoms:
        # Create a patient code using the name
        patient_code = patient_name.lower().replace(" ", "_")

        # Store the form data in a text file
        with open(f"{patient_code}.txt", "w") as file:
            file.write(f"Patient Name: {patient_name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Gender: {gender}\n")
            file.write(f"Symptoms:\n{symptoms}")

        name_entry.delete(0, "end")
        age_entry.delete(0, "end")
        symptoms_text.delete("1.0", "end")
        gender_var.set("Male")  # Reset gender selection
        status_label.config(text="Registration saved.")
    else:
        status_label.config(text="Please fill out all fields.")

Hospital = tk.Tk()
Hospital.title("Hospital Registration Form")
Hospital.geometry("400x300")  # Adjusted window size

# Styling
Hospital.configure(bg="lightblue")  # Background color

# Create form elements
tk.Label(Hospital, text="Patient Name:", bg="lightblue").pack()
name_entry = tk.Entry(Hospital, bg="white", fg="black")  # Background and foreground colors
name_entry.pack()

tk.Label(Hospital, text="Age:", bg="lightblue").pack()
age_entry = tk.Entry(Hospital, bg="white", fg="black")  # Background and foreground colors
age_entry.pack()

tk.Label(Hospital, text="Gender:", bg="lightblue").pack()
gender_var = tk.StringVar(value="Male")
gender_options = ["Male", "Female", "Other"]
gender_dropdown = tk.OptionMenu(Hospital, gender_var, *gender_options)
gender_dropdown.pack()

tk.Label(Hospital, text="Symptoms:", bg="lightblue").pack()
symptoms_text = tk.Text(Hospital, height=4, width=30, bg="white", fg="black")  # Background and foreground colors
symptoms_text.pack()

submit_button = tk.Button(Hospital, text="Submit", command=save_registration, bg="green", fg="white")  # Background and foreground colors
submit_button.pack()

status_label = tk.Label(Hospital, text="", bg="lightblue")
status_label.pack()

Hospital.mainloop()
