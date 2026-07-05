class School:
    school_name = "Alipur school and college"
    school_address = "Hathazari, Chattagram"
    school_phone = "+880 1xxxyyyzzz"
    school_email = "alipurschoolandcollege@email.com"
    school_website = "alipurschool&college.edu.bd"
    def __init__(self):
        pass
    def principal_sir_details(self, name, phone_number, email):
        self.principal_name = name
        self.principal_phone_number = phone_number
        self.principal_email = email
    
    def _a_student_details(self, name, gender, religion, father_name, mother_name, cla_ss, section, birth_cer_num = 0000,):
        self.name = name
        self.gender = gender
        self.religion = religion
        self.father_name = father_name
        self.mother_name = mother_name
        self.cla_ss = cla_ss
        self.section = section
        self.birth_cer_num = birth_cer_num

school = School()
# principal_sir_name = str(input("Principal sir Name: ").strip())
# principal_sir_pnone = str(input("Principal sir Phone number: ").strip())
# principal_sir_email = str(input("Principal sir Email: ".strip()))
# school.principal_sir_details(principal_sir_name, principal_sir_pnone, principal_sir_email)

print("*"*20 + f"{school.school_name}" + "*"*20)