from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys
import csv
import os
from fpdf import FPDF
from datetime import date
from datetime import datetime

global login_user   
global current_date
class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Student")
        self.setFixedWidth(500)
        self.setFixedHeight(450)

        self.QBtn.clicked.connect(self.addstudent)

        layout = QVBoxLayout()

        
        title = QLabel("Roll No")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.rollinput = QLineEdit()
        self.rollinput.setPlaceholderText("Roll no")
        layout.addWidget(self.rollinput)
        self.rollinput.textChanged.connect(self.fillStudents)

        
        title = QLabel("Name")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        
        title = QLabel("Course")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)
        self.branchinput = QComboBox()
        self.branchinput.addItem("5 Th")
        self.branchinput.addItem("6 Th")
        self.branchinput.addItem("7 Th")
        self.branchinput.addItem("8 Th")
        self.branchinput.addItem("9 Th")
        self.branchinput.addItem("10 Th")
        self.branchinput.addItem("11 Th")
        self.branchinput.addItem("12 Th")
        layout.addWidget(self.branchinput)

        
        title = QLabel("Batch")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)

        
        title = QLabel("Total fees")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)
        
        self.total_fees_input = QLineEdit()
        self.total_fees_input.setPlaceholderText("Total fees ")
        self.onlyInt = QIntValidator()
        self.total_fees_input.setValidator(self.onlyInt)
        layout.addWidget(self.total_fees_input)

        
        title = QLabel("Fees Paid ")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.paid_fees_input = QLineEdit()
        self.paid_fees_input.setPlaceholderText("Fees paid ")
        self.onlyInt = QIntValidator()
        self.paid_fees_input.setValidator(self.onlyInt)
        layout.addWidget(self.paid_fees_input)

        
        title = QLabel("Mobile NO")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)


        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        self.onlyInt = QIntValidator()
        self.mobileinput.setValidator(self.onlyInt)
        layout.addWidget(self.mobileinput)

        
        title = QLabel("Address ")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)


        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):
        roll_no=0 
        name = ""
        branch = ""
        sem = -1
        mobile = -1
        address = ""
        total_fees=0
        fees_paid=0
        roll_no= self.rollinput.text() 
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        total_fees = self.total_fees_input.text()
        fees_paid = self.paid_fees_input.text()
        add_student = True
        try:
            with open('user_data/students.csv', 'a') as appendFile:
                writer=csv.writer(appendFile)
                list_append=[str(roll_no),str(name),str(branch),str(sem),str(total_fees),str(fees_paid),str(mobile),str(address)]
                writer.writerow(list_append)
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')
    
    def fillStudents(self):
        fill_roll=self.rollinput.text()
        # print(fill_roll)
        try:
            with open('user_data/students.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row==[]:
                        continue
                    elif str(row[0])==str(fill_roll):
                        self.nameinput.setText(str(row[1]))
                        total_feees=int(row[4])
                        paid_feees=int(row[5])
                        self.total_fees_input.setText(str(total_feees))
                        self.paid_fees_input.setText(str(paid_feees))
                        self.mobileinput.setText(str(row[6]))
                        self.addressinput.setText(str(row[7]))
                        self.seminput.SelectedItem = "3"
                         
                        pending_feees=total_feees-paid_feees
                        self.pending_fees_input.setText(str(pending_feees))
        except:
            # print("")
            QMessageBox.information(QMessageBox(), 'Error')

class AddMarksDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddMarksDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Add Marks")

        self.setWindowTitle("Add Marks Details")
        self.setFixedWidth(500)
        self.setFixedHeight(450)

        self.QBtn.clicked.connect(self.addstudent_mark)

        layout = QVBoxLayout()

        
        title = QLabel("Roll No")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.rollinput = QLineEdit()
        self.rollinput.setPlaceholderText("Roll no")
        layout.addWidget(self.rollinput)
        self.rollinput.textChanged.connect(self.fillStudents)

        
        title = QLabel("Name")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)


        
        title = QLabel("Course")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.branchinput = QComboBox()
        self.branchinput.addItem("5 Th")
        self.branchinput.addItem("6 Th")
        self.branchinput.addItem("7 Th")
        self.branchinput.addItem("8 Th")
        self.branchinput.addItem("9 Th")
        self.branchinput.addItem("10 Th")
        self.branchinput.addItem("11 Th")
        self.branchinput.addItem("12 Th")
        layout.addWidget(self.branchinput)
        
        title = QLabel("Batch")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)


        
        title = QLabel("Subject 1")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.subject1_input = QLineEdit()
        self.subject1_input.setPlaceholderText("Subject 1 ")
        self.onlyInt = QIntValidator()
        self.subject1_input.setValidator(self.onlyInt)
        layout.addWidget(self.subject1_input)

        
        title = QLabel("Subject 2")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.subject2_input = QLineEdit()
        self.subject2_input.setPlaceholderText("Subject 2 ")
        self.onlyInt = QIntValidator()
        self.subject2_input.setValidator(self.onlyInt)
        layout.addWidget(self.subject2_input)

        
        title = QLabel("Subject 3")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.subject3_input = QLineEdit()
        self.subject3_input.setPlaceholderText("Subject 3")
        self.onlyInt = QIntValidator()
        self.subject3_input.setValidator(self.onlyInt)
        layout.addWidget(self.subject3_input)

        
        title = QLabel("Subject 4")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.subject4_input = QLineEdit()
        self.subject4_input.setPlaceholderText("Subject 4")
        layout.addWidget(self.subject4_input)


        
        title = QLabel("Subject 4")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.subject5_input = QLineEdit()
        self.subject5_input.setPlaceholderText("Subject 5")
        layout.addWidget(self.subject5_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent_mark(self):
        roll_no=0 
        name = ""
        branch = ""
        sem = -1
        sub1 = 0
        sub2 = 0
        sub3 = 0
        sub4 = 0
        sub5 = 0
        roll_no= self.rollinput.text() 
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        sub1 = self.subject1_input.text()
        sub2 = self.subject2_input.text()
        sub3 = self.subject3_input.text()
        sub3 = self.subject4_input.text()
        sub4 = self.subject5_input.text()
        # sub5 = self.subject5_input.text()
        add_student = True
        try:
            with open('user_data/students_marks.csv', 'a') as appendFile:
                writer=csv.writer(appendFile)
                list_append=[str(roll_no),str(name),str(branch),str(sem),str(sub1),str(sub2),str(sub3),str(sub4),str(sub5)]
                writer.writerow(list_append)
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')
    
    def fillStudents(self):
        fill_roll=self.rollinput.text()
        # print(fill_roll)
        try:
            with open('user_data/students.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row==[]:
                        continue
                    elif str(row[0])==str(fill_roll):
                        self.nameinput.setText(str(row[1]))
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)

        self.namehinput = QLineEdit()
        self.namehinput.setPlaceholderText("Name")
        layout.addWidget(self.namehinput)
        
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchroll = ""
        searchname = ""
        searchroll = self.searchinput.text()
        searchname = self.namehinput.text()
        try:
            with open('user_data/students.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row==[]:
                        continue
                    elif str(row[0])==str(searchroll) or str(row[1])==str(searchname):
                        # print("user exist")
                        serachresult = "Rollno : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Branch : "+str(row[2])+'\n'+"Sem : "+str(row[3])+'\n'+"Address : "+str(row[4])
                        QMessageBox.information(QMessageBox(), 'Successful', serachresult)
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')
        
class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):

        delrol = ""
        delrol = self.deleteinput.text()
        lines = list()
        no_user=True
        
        try:
            with open('user_data/students.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row==[]:
                        continue
                    elif str(row[0])==str(delrol):
                        # print("user Deleted ")
                        continue
                        # QMessageBox.information(QMessageBox(), 'Error')
                    else:
                        lines.append(row)
            
            with open('user_data/students.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')
        
class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(150)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Enter Password.")

        self.userinput = QLineEdit()
        # self.userinput.setEchoMode()
        self.userinput.setPlaceholderText("Usename.")
        
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")
        self.setWindowTitle('Login')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.userinput)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        global login_user
        if(self.passinput.text() == "vbc@pune7262"):
            self.accept()
            login_user="Pritam Khopde"
        elif(self.passinput.text() == "san@456"):
            self.accept()
            login_user="Sandeep Enpure"
        elif(self.passinput.text() == "Sati@123"):
            self.accept()
            login_user="Satish Mane"
        elif(self.passinput.text() == "MeAjunSingleAhe#911"):
            self.accept()
            login_user="Admin"
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')

class PrintDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(PrintDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Print")

        self.setWindowTitle("Print recipt")
        self.setFixedWidth(600)
        self.setFixedHeight(450)

        self.QBtn.clicked.connect(self.printstudent)

        layout = QVBoxLayout()

        title = QLabel("Roll NO")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.rollinput = QLineEdit()
        self.rollinput.setPlaceholderText("Roll no")
        layout.addWidget(self.rollinput)
        self.rollinput.textChanged.connect(self.fillStudents)
        
        # self.MyInput.textChanged.connect(self.doSomething)

        title = QLabel("Name")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)
        # self.nameinput.textChanged.connect(self.fillStudents)


        title = QLabel("standard")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.branchinput = QComboBox()
        self.branchinput.addItem("5 Th")
        self.branchinput.addItem("6 Th")
        self.branchinput.addItem("7 Th")
        self.branchinput.addItem("8 Th")
        self.branchinput.addItem("9 Th")
        self.branchinput.addItem("10 Th")
        self.branchinput.addItem("11 Th")
        self.branchinput.addItem("12 Th")
        layout.addWidget(self.branchinput)


        title = QLabel("Batch")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)

        global login_user
        title = QLabel("Fees collected By")
        font = title.font()
        # title.setReadOnly(True)
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.admininput = QLineEdit()
        self.admininput.setPlaceholderText(login_user)
        self.admininput.setEnabled(False)
        layout.addWidget(self.admininput)
        
        title = QLabel("Total fees")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.total_fees_input = QLineEdit()
        self.total_fees_input.setPlaceholderText("Total fees ")
        layout.addWidget(self.total_fees_input)

        
        title = QLabel("Fees Paid")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.paid_fees_input = QLineEdit()
        self.paid_fees_input.setPlaceholderText("Fees paid ")
        layout.addWidget(self.paid_fees_input)


        title = QLabel("Fees remaning ")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.pending_fees_input = QLineEdit()
        self.pending_fees_input.setPlaceholderText("Pending Fees ")
        layout.addWidget(self.pending_fees_input)


        title = QLabel("Mobile")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        layout.addWidget(self.mobileinput)

        
        title = QLabel("Address")
        font = title.font()
        # font.setPointSize(16)
        title.setFont(font)
        layout.addWidget(title)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def fillStudents(self):
        fill_roll=self.rollinput.text()
        # print(fill_roll)
        try:
            with open('user_data/students.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row==[]:
                        continue
                    elif str(row[0])==str(fill_roll):
                        # print("user found ")
                        self.nameinput.setText(str(row[1]))
                        total_feees=int(row[4])
                        paid_feees=int(row[5])
                        self.total_fees_input.setText(str(total_feees))
                        self.paid_fees_input.setText(str(paid_feees))
                        self.mobileinput.setText(str(row[6]))
                        self.addressinput.setText(str(row[7]))
                        self.seminput.SelectedItem = "3"
                         
                        pending_feees=total_feees-paid_feees
                        self.pending_fees_input.setText(str(pending_feees))
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error')


    def printstudent(self):
        pdf= FPDF(orientation="L",format="A4")
        pdf.add_page()

        # pdf.image(name="asset/images/vidyabhushan logo (1).png", x = 150, y = 4, w = 55, h = 30, type = 'PNG')

        pdf.set_font("Times",style="B",size=32)
        pdf.cell(65)
        pdf.cell(35,12,"Vidyabhushan Coaching Classes",ln=1)

        pdf.cell(50)
        pdf.set_font("Times",size=20)
        pdf.cell(35,12,"Success",ln=1)
        pdf.cell(w=0,h=10,ln=1)

        pdf.set_font("Times",size=21)
        string1="Student Name : "+self.nameinput.text()
        pdf.cell(w=40,h=9,txt=string1,ln=1)

        string2="Phone Number : "+self.mobileinput.text()
        pdf.cell(w=60,h=9,txt=string2,ln=1)

        string3="Email ID : "+self.mobileinput.text()
        pdf.cell(w=60,h=9,txt=string3,ln=1)

        string4="Course : "+self.branchinput.itemText(self.branchinput.currentIndex())
        pdf.cell(w=60,h=9,txt=string4,ln=1)

        string5="Total Fees : "+str(self.total_fees_input.text())
        pdf.cell(w=60,h=9,txt=string5,ln=1)

        string6="Paid Fees : "+str(self.paid_fees_input.text())
        pdf.cell(w=60,h=9,txt=string6,ln=1)

        string7="Remaining Fees : "+str(self.pending_fees_input.text())
        pdf.cell(w=60,h=9,txt=string7,ln=1)

        today = date.today()
        string8="Date and Time : "+str(today)
        pdf.cell(w=60,h=9,txt=string8,ln=1)

        global login_user
        string9="Collected By : "+login_user
        pdf.cell(w=60,h=9,txt=string9,ln=1)

        pdf.cell(w=0,h=3,ln=1)
        pdf.cell(40)
        pdf.set_font("Times",size=13)
        pdf.cell(0,8,"Shop No. 32, Near Dharmveer Ganapati Temple Trimurthi Chowk | Contact - 9850424170 ",ln=1)
        
        pdf.output("Recipts/"+self.rollinput.text()+" "+self.nameinput.text()+".pdf")
        pdf.output("asset/Invoice/"+ self.rollinput.text()+" "+self.nameinput.text()+".pdf")

        month = datetime.now().month
        year = datetime.now().year

        try:
            with open('user_data/DATA/'+str(month)+' '+str(year)+'.csv', 'w') as appendFile:
                writer=csv.writer(appendFile)
                list_append=[str(string1),str(string2),str(string3),str(string4),str(string5),str(string6),str(string7),str(string8),str(string9)]
                writer.writerow(list_append)
                QMessageBox.information(QMessageBox(), 'Sucqess',"Fees Paid Sucessfully ")
        except:
            # print()
            QMessageBox.information(QMessageBox(), 'Error',"Error is Here")

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Vidyabhushan Coaching Classes")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)        
        layout.addWidget(title)


        title2 = QLabel("Product Design By :")
        font = title2.font()
        font.setPointSize(9)
        title2.setFont(font)        
        layout.addWidget(title2)
        
        user1 = QLabel("ANIL KOLI ")
        font = user1.font()
        font.setPointSize(10)
        user1.setFont(font)        
        layout.addWidget(user1)

        layout.addWidget(QLabel("&"))

        user2 = QLabel("PRATHMESH NAMDAS")
        font = user2.font()
        font.setPointSize(10)
        user2.setFont(font)        
        layout.addWidget(user2)
        # labelpic = QLabel()
        # pixmap = QPixmap('icon/logo.png')
        # pixmap = pixmap.scaledToWidth(275)
        # labelpic.setPixmap(pixmap)
        # labelpic.setFixedHeight(150)
        # layout.addWidget(labelpic)
        
        layout.addWidget(QLabel("Version 1"))
        layout.addWidget(QLabel("Copyright 2021 SKYLINE SOFT SOLUTIONS."))

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

class FeesData(QDialog):
    def __init__(self, *args, **kwargs):
        super(FeesData, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        # layout.addWidget(self.buttonBox)

        self.setLayout(layout)

        self.marksWidget = QTableWidget()
        # self.setCentralWidget(self.marksWidget)
        self.marksWidget.setAlternatingRowColors(True)
        self.marksWidget.setColumnCount(8)
        self.marksWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.marksWidget.horizontalHeader().setSortIndicatorShown(False)
        self.marksWidget.horizontalHeader().setStretchLastSection(True)
        self.marksWidget.verticalHeader().setVisible(False)
        self.marksWidget.verticalHeader().setCascadingSectionResizes(False)
        self.marksWidget.verticalHeader().setStretchLastSection(False)
        self.marksWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Subject 1", "Subject 2", "Subject 3","Subject 4"))
        
        row_number=1
        self.marksWidget.clearContents()
        with open("user_data/students_marks.csv","r") as readfile:
            read=csv.reader(readfile)
            for row in read:
                row_number=row_number+1
                self.marksWidget.removeRow(row_number)
        
        self.marksWidget.insertRow(row_number)
        with open("user_data/students_marks.csv","r") as readfile:
            read=csv.reader(readfile)
            for row_number, row_data in enumerate(read):
                self.marksWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if row_data==[]:
                        continue
                    else:
                        self.marksWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
       


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        file_menu = self.menuBar().addMenu("&Student")

        show_menu = self.menuBar().addMenu("&Show")

        help_menu = self.menuBar().addMenu("&About")
        
        self.setWindowTitle("Vidyabhushan Coaching Classes")

        self.setMinimumSize(800, 600)

        # self.tableWidget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        # self.tableWidget.setAlternatingRowColors(True)
        # self.tableWidget.setColumnCount(8)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        # self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        # self.tableWidget.verticalHeader().setStretchLastSection(False)
        # self.tableWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Total Fees", "Fees Paid", "Mobile","Address"))

        # self.marksWidget = QTableWidget()
        # self.setCentralWidget(self.marksWidget)
        # self.marksWidget.setAlternatingRowColors(True)
        # self.marksWidget.setColumnCount(8)
        # self.marksWidget.horizontalHeader().setCascadingSectionResizes(False)
        # self.marksWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.marksWidget.horizontalHeader().setStretchLastSection(True)
        # self.marksWidget.verticalHeader().setVisible(False)
        # self.marksWidget.verticalHeader().setCascadingSectionResizes(False)
        # self.marksWidget.verticalHeader().setStretchLastSection(False)
        # self.marksWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Subject 1", "Subject 2", "Subject 3","Subject 4"))
        


        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Add Student", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/trash.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)

        btn_ac_print = QAction(QIcon("icon/print.png"), "Print", self)
        btn_ac_print.triggered.connect(self.print)
        btn_ac_print.setStatusTip("Print recipt")
        toolbar.addAction(btn_ac_print)


        global login_user
        if login_user == "Pritam Khopde":    
            btn_ac_print = QAction(QIcon("icon/print.png"), "Fees data", self)
            btn_ac_print.triggered.connect(self.fees)
            btn_ac_print.setStatusTip("Fees recipt")
            toolbar.addAction(btn_ac_print)

        adduser_action = QAction(QIcon("icon/add.png"),"Insert Student", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        adduser_action = QAction(QIcon("icon/add_marks.png"),"Insert Report", self)
        adduser_action.triggered.connect(self.marks)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("icon/search.png"), "Search Student", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("icon/trash.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

        printuser_action = QAction(QIcon("icon/print.png"), "Print ", self)
        printuser_action.triggered.connect(self.print)
        file_menu.addAction(printuser_action)

        show_students = QAction(QIcon("icon/add.png"),"Show Students", self)
        show_students.triggered.connect(self.loaddata)
        show_menu.addAction(show_students)

        show_students_marks = QAction(QIcon("icon/add_marks.png"),"Show Reports", self)
        show_students_marks.triggered.connect(self.loadmarks)
        show_menu.addAction(show_students_marks)

        
        about_action = QAction(QIcon("icon/info.png"),"Developer", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Total Fees", "Fees Paid", "Mobile","Address"))
        
        row_number=1
        self.tableWidget.clearContents()
        with open("user_data/students.csv","r") as readfile:
            read=csv.reader(readfile)
            for row in read:
                row_number=row_number+1
                self.tableWidget.removeRow(row_number)
        
        self.tableWidget.insertRow(row_number)
        with open("user_data/students.csv","r") as readfile:
            read=csv.reader(readfile)
            for row_number, row_data in enumerate(read):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if row_data==[]:
                        continue
                    else:
                        self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
       
    def loadmarks(self):

        self.marksWidget = QTableWidget()
        self.setCentralWidget(self.marksWidget)
        self.marksWidget.setAlternatingRowColors(True)
        self.marksWidget.setColumnCount(8)
        self.marksWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.marksWidget.horizontalHeader().setSortIndicatorShown(False)
        self.marksWidget.horizontalHeader().setStretchLastSection(True)
        self.marksWidget.verticalHeader().setVisible(False)
        self.marksWidget.verticalHeader().setCascadingSectionResizes(False)
        self.marksWidget.verticalHeader().setStretchLastSection(False)
        self.marksWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Subject 1", "Subject 2", "Subject 3","Subject 4"))
        
        row_number=1
        self.marksWidget.clearContents()
        with open("user_data/students_marks.csv","r") as readfile:
            read=csv.reader(readfile)
            for row in read:
                row_number=row_number+1
                self.marksWidget.removeRow(row_number)
        
        self.marksWidget.insertRow(row_number)
        with open("user_data/students_marks.csv","r") as readfile:
            read=csv.reader(readfile)
            for row_number, row_data in enumerate(read):
                self.marksWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if row_data==[]:
                        continue
                    else:
                        self.marksWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
       
                         
    # def handlePaintRequest(self, printer):
    #     document = QTextDocument()
    #     cursor = QTextCursor(document)
    #     model = self.table.model()
    #     table = cursor.insertTable(
    #         model.rowCount(), model.columnCount())
    #     for row in range(table.rows()):
    #         for column in range(table.columns()):
    #             cursor.insertText(model.item(row, column).text())
    #             cursor.movePosition(QTextCursor.NextCell)
    #     document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()
    
    def print(self):
        dlg = PrintDialog()
        dlg.exec_()

    def fees(self):
        dlg = FeesData()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def marks(self):
        dlg = AddMarksDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()


app = QApplication(sys.argv)
passdlg = LoginDialog()
if(passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())