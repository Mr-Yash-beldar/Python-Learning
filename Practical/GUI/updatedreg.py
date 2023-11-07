import tkinter as tk

def save_registration():
    patient_name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    symptoms = symptoms_text.get("1.0", "end-1c")
    doctor_name = doctor_entry.get()
    appointment_number = appointment_entry.get()

    if patient_name and age and gender and symptoms and doctor_name and appointment_number:
        # Create a patient code using the name
        filename = patient_name.lower().replace(" ", "_")

        # Store the form data in a text file
        with open(f"{filename}.txt", "w") as file:
            file.write(f"Patient Name: {patient_name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Gender: {gender}\n")
            file.write(f"Symptoms:\n{symptoms}\n")
            file.write(f"Doctor's Name: {doctor_name}\n")
            file.write(f"Appointment Number: {appointment_number}\n")

        # Clear fields
        name_entry.delete(0, "end")
        age_entry.delete(0, "end")
        symptoms_text.delete("1.0", "end")
        doctor_entry.delete(0, "end")
        appointment_entry.delete(0, "end")
        gender_var.set("Male")  # Reset gender selection
        tk.messagebox.showinfo("Registration saved.")
    else:
        tk.messagebox.showerror("Error", "Please fill out all fields.")

Hospital = tk.Tk()
Hospital.title("Hospital Registration Form")
Hospital.geometry("500x400")  # Adjusted window size

# Styling
Hospital.configure(bg="lightblue")  # Background color

hospital_name_label = tk.Label(Hospital, text="Yashodip Hospital", bg="black", fg="white", font=("Arial", 20))
hospital_name_label.pack(fill="x")

# Create form elements
tk.Label(Hospital, text="Patient Name:", bg="lightblue").pack()
name_entry = tk.Entry(Hospital, bg="white", fg="black", font=("Arial", 12))  # Background and foreground colors
name_entry.pack()

tk.Label(Hospital, text="Age:", bg="lightblue").pack()
age_entry = tk.Entry(Hospital, bg="white", fg="black", font=("Arial", 12))  # Background and foreground colors
age_entry.pack()

tk.Label(Hospital, text="Gender:", bg="lightblue").pack()
gender_var = tk.StringVar(value='Male')
gender_radio_male = tk.Radiobutton(Hospital, text="Male", variable=gender_var, value="Male", bg="lightblue")
gender_radio_female = tk.Radiobutton(Hospital, text="Female", variable=gender_var, value="Female", bg="lightblue")
gender_radio_male.pack()    
gender_radio_female.pack()


tk.Label(Hospital, text="Symptoms:", bg="lightblue").pack()
symptoms_text = tk.Text(Hospital, height=4, width=40, bg="white", fg="black", font=("Arial", 12))  # Background and foreground colors
symptoms_text.pack()

tk.Label(Hospital, text="Doctor's Name:", bg="lightblue").pack()
doctor_entry = tk.Entry(Hospital, bg="white", fg="black", font=("Arial", 12))  # Background and foreground colors
doctor_entry.pack()

tk.Label(Hospital, text="Appointment Number:", bg="lightblue").pack()
appointment_entry = tk.Entry(Hospital, bg="white", fg="black", font=("Arial", 12))  # Background and foreground colors
appointment_entry.pack()

submit_button = tk.Button(Hospital, text="Submit", command=save_registration, bg="green", fg="white", font=("Arial", 14))  # Background and foreground colors
submit_button.pack()

# status_message = tk.mesagebox(Hospital, text="", bg="lightblue", font=("Arial", 12))
# status_message.pack()

Hospital.mainloop()
