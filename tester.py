from Tkinter import *
import tkFont
import MySQLdb
import serial
import StringIO
import csv

class App:

	def __init__(self, master):

		frame = Frame(master)
		frame.pack()
		
		arial18 = tkFont.Font(family='Arial', size=18, weight='bold')  # big font so we can read it in the shop

		self.button = Button(
		frame, text="QUIT", font=arial18, fg="red", command=frame.quit)
		self.button.grid(row=11, column=3)
		
		self.serial_value = Entry(frame, text="foo", font=arial18)
		self.serial_value.grid(row=0, column=1, columnspan=2)

		self.serial_label = Label(frame, text="UNIT:", font=arial18)
		self.serial_label.grid(row=0, column=0)
		
		self.pass_fail = StringVar()  # variable that shows if a test passed or failed
		self.pass_fail.set("FAIL")
		self.test_status = Label(frame, textvariable=self.pass_fail, font=arial18, fg="red")
		self.test_status.grid(row=0, column=3)
		
		self.cmd_string = "" # command we send the test unit
		self.rsp_string = "" # response we read back

		self.test_01 = Button(frame, text="Test 01", font=arial18, command=self.test01)
		self.test_01.grid(row=1, column=0)

		self.test_02 = Button(frame, text="Test 02", font=arial18, command=self.say_hi)
		self.test_02.grid(row=2, column=0)

		self.test_03 = Button(frame, text="Test 03", font=arial18, command=self.say_hi)
		self.test_03.grid(row=3, column=0)

		self.test_04 = Button(frame, text="Test 04", font=arial18, command=self.say_hi)
		self.test_04.grid(row=4, column=0)

		self.test_05 = Button(frame, text="Test 05", font=arial18, command=self.say_hi)
		self.test_05.grid(row=5, column=0)

		self.test_06 = Button(frame, text="Test 06", font=arial18, command=self.say_hi)
		self.test_06.grid(row=6, column=0)

		self.test_07 = Button(frame, text="Test 07", font=arial18, command=self.say_hi)
		self.test_07.grid(row=1, column=2)

		self.test_08 = Button(frame, text="Test 08", font=arial18, command=self.say_hi)
		self.test_08.grid(row=2, column=2)

		self.test_09 = Button(frame, text="Test 09", font=arial18, command=self.say_hi)
		self.test_09.grid(row=3, column=2)
		
		self.test_10 = Button(frame, text="Test 10", font=arial18, command=self.say_hi)
		self.test_10.grid(row=4, column=2)

		self.test_11 = Button(frame, text="Test 11", font=arial18, command=self.say_hi)
		self.test_11.grid(row=5, column=2)

		self.test_every = Button(frame, text="Run All", font=arial18, command=self.say_hi)
		self.test_every.grid(row=6, column=2)
		
	def say_hi(self):
		print "Testing cart - ", self.serial_value.get()
		self.pass_fail.set("PASS")
		self.test_status.configure(fg="green")
	
	def test01(self):
		self.cmd_string="RD 1?\n"
		print self.cmd_string
		self.rsp_string="1,1,ACW,Pass,1.60, 2.92, 60.0\n"
		
		if self.rsp_string.split(',')[3] == 'Pass':
			self.pass_fail.set("PASS")
			self.test_status.configure(fg="green")
		else:
			self.pass_fail.set("FAIL")
			self.test_status.configure(fg="red")
		
		#ser.write(self.cmd_string)  # send command to tester
		#self.rsp_string=ser.readline()  # get the response
		
		print "Returned:", self.rsp_string, "#"
		
		try:
			sql = "INSERT INTO tests (unit_serial, test_string, result_string) VALUES ('%s', '%s', '%s')" % (self.serial_value.get() or 'NONE', self.cmd_string, self.rsp_string)
			cursor.execute(sql)
			db.commit()
		
		except:
			print "Error: Couldn't insert into database"
			db.rollback()
		
root = Tk()

app = App(root)

serial_port = 2                  # which COM port to use (starts at 0, so 2 = COM3)

db = MySQLdb.connect("10.0.0.1", "user", "db", "table")
cursor = db.cursor()

# start the GUI
root.mainloop()

# cleanup code
ser.close()
db.close()

root.destroy()
