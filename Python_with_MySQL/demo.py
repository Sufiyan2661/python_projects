import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Admin",database="student_management")


cursor = mydb.cursor()

cursor.execute("SELECT s.student_id,s.roll_number,s.name,s.class,a.attendance_id,a.date,a.status FROM students s LEFT JOIN attendance a ON s.student_id = a.student_id ")
for data in cursor.fetchall():
    print(data)
    
    
mydb.close()

