#  Hospital Class - This class manages basic hospital info along with its doctors and patients
class Hospital(): 
    # Constructor
    def __init__(self, name, location):
        self.hospital_name = name               #  Hospital name
        self.hospital_location = location       #  Hospital location
        self.patients = []                      #  Empty List of patients
        self.doctors = []                       # Empty list of doctors

    # Method to add a doctor
    def add_doctor(self, doctor):
        return self.doctors.append(doctor)

    # Method to remove a doctor
    def remove_doctor(self, doctor):
        return self.doctors.remove(doctor)

    # 📋 Method to get the list of all doctors
    def get_doctors(self):
        return self.doctors


    # Method to add a patient
    def add_patient(self, patient):
        return self.patients.append(patient)

    # Method to remove a patient
    def remove_patient(self, patient):
        return self.patients.remove(patient)

    # 📋 Method to get the list of all patients
    def get_patients(self):
        return self.patients


# 👨‍⚕️ Doctor Class - This class stores a doctor's information
class Doctor():
    def __init__(self, name, specialization, availability):
        self.doctor_name = name                      # 👨‍⚕️ Doctor's name
        self.doctor_specialization = specialization  # 🧠 Doctor's field/specialization
        self.doctor_availability = availability      # ✅ Doctor's availability status


# 🧍‍♂️ Patient Class - This class stores a patient's details
class Patient():
    def __init__(self, name, age, ailment):
        self.patient_name = name         # 🙋‍♂️ Patient's name
        self.patient_age = age           # 🔢 Patient's age
        self.patient_ailment = ailment   # 🤒 Patient's illness/issue


# ✅ Create doctors
doctor = Doctor("Dr.Haider", "Cardiologist ❤️", True)
doctor1 = Doctor("Dr.Nabia", "Ophthalmologist 👁️", True)
doctor2 = Doctor("Dr.Shazz", "General Physician 🩺", False)
doctor3 = Doctor("Dr.Aisha", "Pediatrician 👶", True)

# ✅ Create patients
patient = Patient("Ali", 30, "Blood Pressure")
patient1 = Patient("Umair", 5, "Fever 🌡️")
patient2 = Patient("Sara", 25, "Headache 🤕")
patient3 = Patient("Humna", 40, "Diabetes 🍬")
patient4 = Patient("Muntaha", 35, "Heart Disease ❤️")
patient5 = Patient("Ayesha", 30, "Eye Injury 👁️")
patient6 = Patient("Rayyan", 28, "Sore Throat 😷")

# 🏥 Create a hospital
hospital = Hospital("City Hospital", "Karachi")

# Add doctors to the hospital
hospital.add_doctor(doctor)
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)
hospital.add_doctor(doctor3)

# Add patients to the hospital
hospital.add_patient(patient)
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.add_patient(patient3)
hospital.add_patient(patient4)
hospital.add_patient(patient5)
hospital.add_patient(patient6)

# ❌ Remove a doctor and a patient
hospital.remove_doctor(doctor1)
hospital.remove_patient(patient5)

# 📋 Print list of doctors
print("👨‍⚕️ Doctors in Hospital:")   
doctors = hospital.get_doctors()   # hospital object will get the list of doctors.
for doc in doctors:
    print(f"➡️ {doc.doctor_name} - {doc.doctor_specialization}") # print doctor name and field 

# 📋 Print list of patients
print("\n🧍‍♂️ Patients in Hospital:")
patients = hospital.get_patients() # hospital object will get the list of patients.
for pat in patients:
    print(f"➡️ {pat.patient_name} ({pat.patient_age} yrs) - {pat.patient_ailment}") # print doctor name or illness

