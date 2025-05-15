
from asyncio import Condition
from operator import imod
from pydoc import doc
import tkinter as tk
from tkinter import Menu, ttk
from tkinter.tix import Tk
import pyodbc

class hospital_system:
    def __init__(self,root):
      self.__root= root
      self.__root.title("hospital system")
    #database connection
      self.cnxn = pyodbc.connect(
      "Driver={ODBC Driver 17 for SQL Server};"
      "Server=localhost;"
      "Database=oop;"
      "Trusted_Connection=yes;"
    )
      self.__cursor = self.cnxn.cursor()
    
      self.notebook= ttk.Notebook(self.__root)
      self.notebook.pack(fill='both', expand=True)
      
      self.doctor_tab=ttk.Frame(self.notebook)
      self.patient_tab=ttk.Frame(self.notebook)
      self.appointment_tab=ttk.Frame(self.notebook)
      
      self.notebook.add(self.patient_tab,text="Patient's tab")
      self.notebook.add(self.doctor_tab,text="Doctor's tab")
      self.notebook.add(self.appointment_tab,text="Appointments tab")
      
      self.doctortab()
      self.patienttab()
      self.appointmenttab()
          
    def doctortab(self):
      doctor_frame= ttk.LabelFrame(self.doctor_tab,text="Enter Doctor Info")
      doctor_frame.pack(fill='both',expand=True)
      ttk.Label(doctor_frame,text="Doctor's Name:").grid(row=0)
      ttk.Label(doctor_frame,text="Doctor's Age:").grid(row=1)
      ttk.Label(doctor_frame,text="Doctor's Department:").grid(row=2)
      
      self.doctor_name = ttk.Entry(doctor_frame)
      self.doctor_name.grid(row=0,column=1)
      self.doctor_age = ttk.Entry(doctor_frame)
      self.doctor_age.grid(row=1,column=1)
      self.doctor_department = ttk.Entry(doctor_frame)
      self.doctor_department.grid(row=2,column=1)

      doc_btn= ttk.Button(doctor_frame,text='Register Doctor',command=self.register_doctor)
      doc_btn.grid(row=3,column=0)
      
    def patienttab(self):
      patient_frame= ttk.LabelFrame(self.patient_tab,text="Enter Patient Info")
      patient_frame.pack(fill='both',expand=True)
      ttk.Label(patient_frame,text="Patient's Name:").grid(row=0)
      ttk.Label(patient_frame,text="Patient's Age:").grid(row=1)
      ttk.Label(patient_frame,text="Patient Condition:").grid(row=2)
      
      self.patient_name = ttk.Entry(patient_frame)
      self.patient_name.grid(row=0,column=1)
      self.patient_age = ttk.Entry(patient_frame)
      self.patient_age.grid(row=1,column=1)  
      self.patient_condition = ttk.Combobox(patient_frame)
      self.patient_condition.grid(row=2,column=1)
      self.patient_condition['values']=('minor','urgent','critical')
      
      pat_btn=ttk.Button(patient_frame,text='Register Patient',command=self.register_patient)
      pat_btn.grid(row=3,column=0)
      
    def appointmenttab(self):
      appointment_frame= ttk.LabelFrame(self.appointment_tab,text="Enter Appointment Info")
      appointment_frame.pack(fill='both',expand=True)
      ttk.Label(appointment_frame,text="Appointment Doctor:").grid(row=0)
      ttk.Label(appointment_frame,text="Appointment Date:").grid(row=1)
      ttk.Label(appointment_frame,text="Patient Name:").grid(row=2)
      
      self.a_doctor_name = ttk.Entry(appointment_frame)
      self.a_doctor_name.grid(row=0,column=1)
      self.a_date_entry = ttk.Entry(appointment_frame)
      self.a_date_entry.grid(row=1,column=1)
      self.a_patient_name = ttk.Entry(appointment_frame)
      self.a_patient_name.grid(row=2,column=1)

      appoint_btn = ttk.Button(appointment_frame,text='Register Appointment',command=self.register_appointment)
      appoint_btn.grid(row=3,column=0)
    def register_patient(self):
      name = self.patient_name.get()
      age= int(self.patient_age.get())
      condition = self.patient_condition.get()
      self.__cursor.execute(
                            f"INSERT INTO patient (name, age, condition) VALUES ('{name}', '{age}', '{condition}')"
      )
      self.cnxn.commit()
      self.patient_name.delete(0, tk.END)
      self.patient_age.delete(0, tk.END)
      self.patient_condition.set('')
      
    def register_doctor(self):
      name= self.doctor_name.get()
      age = int(self.doctor_age.get())
      department = self.doctor_department.get()
      self.__cursor.exectute(
        f"INSERT INTO doctor (name, age, department) VALUES ('{name}', {age}, '{department}')"
      )
      self.cnxn.commit()
      self.doctor_name.delete(0,tk.END)
      self.doctor_age.delete(0,tk.END)
      self.doctor_department.delete(0,tk.END)
          
    def register_appointment(self):
      name = self.a_doctor_name.get()
      date = self.a_date_entry.get()
      p_name = self.a_patient_name.get()
      
      self.__cursor.execute(
        f"INSERT INTO appointment (doctor, date, patient_name) VALUES ('{name}', '{date}', '{p_name}')"
      )
      self.cnxn.commit()
      self.a_doctor_name.delete(0,tk.END)
      self.a_date_entry.delete(0,tk.END)
      self.a_patient_name.delete(0,tk.END)
      
  

root =Tk()
app = hospital_system(root)
root.mainloop()

if app.cnxn:
  app.cnxn.close()