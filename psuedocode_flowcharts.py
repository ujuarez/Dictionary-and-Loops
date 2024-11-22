import student_data
students = student_data.students

# 1. Update a Student's Name
#Task: Update the first and last name of a student based on CPSID

id = int(input("Enter CPSID: "))

for student in students:
    if student['CPSID'] == id:
        new_FName = input("Enter the New FIRST NAME: ")
        new_LName = input("Enter the New LAST NAME: ")
        student['FName'] = new_FName
        student['LName'] = new_LName
        print(f"Updated Student: {student}")
        break     
else:
    if student['CPSID'] != id:
        print("Student not found")



# 2. Delete a Key-Value Pair
#Task: Delete the MName key for a student based on CPSID

id2 = int(input("Enter your CPSID: "))

for student in students:
    if student['CPSID'] == id2:
        del student ['MName']
        print(f"Updated Student: {student}")
        break
else:
    if student['CPSID'] != id2:
        print("CPSID Not Found")


          