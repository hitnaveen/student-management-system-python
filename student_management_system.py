# creating class student to add student details

class Student():
  student_dict = {}
  School_name = "High School"
  def __init__(self):
    self.name = str(input("Enter student name:"))
    self.rollno = int(input("Enter student Roll No:"))
    self.phoneno = int(input("Enter student Phone No:"))
    self.address = input("Enter student address:")
    student_class = int(input("Enter student class:"))

    if student_class in studentclass.classes:
      studentclass.classes[student_class].studentList.append(self)
    else:
      new_class = studentclass(student_class)
      new_class.studentList.append(self)
      studentclass.classes[student_class] = new_class
    self.student_class = studentclass.classes[student_class]

    print("\n Student details addedd successfully")
    self.getdetails()

  # creating method to show student details.

  def getdetails(self):
    print("\n ---Student details---")
    print('\t Student Name:',self.name)
    print('\t Student Roll No:',self.rollno)
    print('\t Student Phone No:',self.phoneno)
    print('\t Student Address:',self.address)
    print('\t Student Class:',self.student_class)

  def updatestudent(self):
    print("\n select option to update student details")
    print("\t1) to change Name")
    print("\t2) to change Roll No")
    print("\t3) to change Phone No")
    print("\t4) to change Address")
    print("\t5) to change Class")
    option = input("Enter any above given option")
    print()

    if option in ['1','2','3','4','5']:
      if option =="1":
       self.name = input("\t Enter student New Name:")
       print("\t", self.name, "updated successfully")
      elif option =="2":
        self.rollno = int(input("\t Enter student new roll no: "))
        print("\t", self.rollno, "updated successfully")
      elif option == "3":
        self.phoneno = input("\t Enter student new phone no:")
        print("\t", self.phoneno, "updated successfully")
      elif option == "4":
       self.address = input("\t Enter student new address:")
       print("\t", self.address, "updated successfully")
      else:
       new_class = int(input("\t Enter student new class:"))
       self.student_class.studentList.remove(self)
       try:
        self.student_class = studentclass.classes[new_class]
        self.student_class.studentList.append(self)
       except:
        addclass = studentclass(new_class)
        self.student_class = addclass
        addclass.studentList.append(self)
        print("\t student class updated successfully")

    self.getdetails()

  
  @classmethod
  def updateschoolname(cls, newschoolname):

    cls.School_name = newschoolname
    print("\t School name updated successfully")
  @classmethod
  def totalstudents(cls):

    return len(cls.student_dict)
    


  # creating student class to get any student name with class

class studentclass():
  classes = {}
  def __init__(self,name):

    self.name = name
    studentclass.classes[name] = self
    self.studentList = []

# this main method is to display at first
def main():
  print("---Welcome to our school---\n")
  print("\t1) Get Student Details\n")
  print("\t2) Add Student Details\n")
  print("\t3) Remove Student Details\n")
  print("\t4) Update Student Details\n")
  print("\t5) Update school name\n")
  print("\t6) Get No of students in school\n")
  print("\t7) Get all students details\n")
  print("\t8) Get any class student details\n")
  option = input("Enter any above given option")
  print()

  # options to show
  if option =="1":
    rollno = int(input("Enter student Roll No:"))
    try:
      Student.student_dict[rollno].getdetails()
    except:
      print("\t you have entered wrong roll no")
  elif option =="2":
    st = Student()
    Student.student_dict[st.rollno] = st
  elif option =="3":
    rollno = int(input("Enter student Roll No:"))
    try:
      student = Student.student_dict.pop(rollno)
      student.student_class.studentList.remove(student)
      print("\t", rollno, "deleted successfully")
    except:
      print("\t no student there to delete")

  elif option =="4":
    rollno = int(input("Enter student Roll No:"))
    print()
    try:
      Student.student_dict[rollno].updatestudent()
    except:
      print("\t you have entered wrong roll no")
    
    
  elif option =="5":
    newschoolname = input("Enter new school name:")
    Student.updateschoolname(newschoolname)
    print("\t School name updated successfully")
  elif option =="6":
    print("\t No of students in school:", Student.totalstudents())
  elif option =="7":
    print("\t No of students in school:", Student.totalstudents())
    print("\n total students list with details\n")
    for sno, student in enumerate(Student.student_dict.values()):
      print("student-", sno+1)
      student.getdetails()
      print()

  elif option == "8":
    try:
      stud = studentclass.classes[input("Enter student class:")]
      print("\n Student class - ", stud.name)
      print(f"\n total number students in class {stud.name}:{len(stud.studentList)}")
      print()
      for sno, student in enumerate(stud.studentList):
        print("student-", sno+1)
        student.getdetails()
        print()
    except:
      print("\t you have entered wrong class or no student there")


  else:
    print("\t you have entered wrong option")

if __name__ == "__main__":
  option = "y"
  while option == "y":
    main()
    option = input("\nDo you want to continue [Y/N?]:")
    print()