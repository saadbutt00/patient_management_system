import streamlit as st
from datetime import datetime

class Patient:
    def __init__(self, p_id, name, age, medical_cond, urgency_level, admission_time):
        self.patient_id = p_id
        self.name = name
        self.age = age
        self.medical_cond = medical_cond
        self.urgency_level = urgency_level
        self.admission_time = admission_time
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addpatient(self, patient):
        if not self.head:
            self.head = patient
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = patient

    def rmvpatient(self, patient_id):
        cur = self.head
        prev = None

        if cur and cur.patient_id == patient_id:
            self.head = cur.next
            return

        while cur:
            if cur.patient_id == patient_id:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        st.error(f'Patient No. {patient_id} not found!')

    def updatepatient(self, patient_id, new_data):
        cur = self.head
        while cur:
            if cur.patient_id == patient_id:
                cur.name = new_data['name']
                cur.age = new_data['age']
                cur.medical_cond = new_data['medical_cond']
                cur.urgency_level = new_data['urgency_level']
                cur.admission_time = new_data['admission_time']
                st.success(f'Patient No. {patient_id} updated.')
                return
            cur = cur.next
        st.error(f'No Patient Found with ID {patient_id}!')

    def get_patients(self):
        patients = []
        cur = self.head
        while cur:
            patients.append(cur)
            cur = cur.next
        return patients

    def display(self, patients):
        if not patients:
            st.write("No patients in the list.")
        for cur in patients:
            st.write(f"Patient ID: {cur.patient_id}")
            st.write(f"Name: {cur.name}")
            st.write(f"Age: {cur.age}")
            st.write(f"Medical Condition: {cur.medical_cond}")
            st.write(f"Urgency Level: {cur.urgency_level}")
            st.write(f"Admission Time: {cur.admission_time}")
            st.write("---")

if 'patient_list' not in st.session_state:
    st.session_state.patient_list = LinkedList()

st.title("Patient Management System")

st.subheader("Add a Patient")
p_id = st.text_input("Patient ID")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, step=1)
medical_cond = st.text_input("Medical Condition")
urgency_level = st.slider("Urgency Level", 1, 5)
admission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if st.button("Add Patient"):
    patient = Patient(p_id, name, age, medical_cond, urgency_level, admission_time)
    st.session_state.patient_list.addpatient(patient)
    st.success("Patient added successfully!")

st.subheader("Update a Patient")
update_id = st.text_input("Enter Patient ID to Update")
new_name = st.text_input("New Name")
new_age = st.number_input("New Age", min_value=1, step=1, key="age_update")
new_medical_cond = st.text_input("New Medical Condition")
new_urgency_level = st.slider("New Urgency Level", 1, 5, key="urgency_update")

if st.button("Update Patient"):
    new_data = {
        "name": new_name,
        "age": new_age,
        "medical_cond": new_medical_cond,
        "urgency_level": new_urgency_level,
        "admission_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.patient_list.updatepatient(update_id, new_data)

st.subheader("Remove a Patient")
remove_id = st.text_input("Enter Patient ID to Remove")

if st.button("Remove Patient"):
    st.session_state.patient_list.rmvpatient(remove_id)
    st.success("Patient removed successfully!")

st.subheader("Display Patients")
sort_option = st.radio("Show Patients:", ["In order of admission time", "In order of urgency level"])

if st.button("Show Patients"):
    patients = st.session_state.patient_list.get_patients()

    if sort_option == "In order of admission time":
        patients.sort(key=lambda x: x.admission_time)
    elif sort_option == "In order of urgency level":
        patients.sort(key=lambda x: x.urgency_level, reverse=True)

    st.session_state.patient_list.display(patients)

# streamlit run "F:\MyProject\Lib\DSA.py"
