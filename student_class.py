class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id = id
    
    def get_student_data(self, first_name, last_name, major, credit_hours, gpa, id):
        return self.__first_name, self.__last_name, self.__major, self.__credit_hours, self.__gpa, self.__id
    
    def set_major(self, new_major):
        self.__major = new_major

    def set_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours

    def get_class_level(self):
        if self.__credit_hours>=0 and self.__credit_hours<=30:
            return "Freshman"
        elif self.__credit_hours>30 and self.__credit_hours<=60:
            return "Sophomore"
        elif self.__credit_hours>60 and self.__credit_hours<=90:
            return "Junior"
        elif self.__credit_hours>90:
            return "Senior"
        else:
            return "Error"
        
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa


    def print_student_data(self):
        print(f"Name: {self.__first_name} {self.__last_name}. Major: {self.__major}. Credit hours: {self.__credit_hours}. GPA: {self.__gpa}. ID#: {self.__id}")
