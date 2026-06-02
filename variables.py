name=input("Enter the student name: ")
age=int(input("Enter the student age: "))
Math=int(input("Enter your Math score: "))
Science=int(input("Enter ur Science score: "))
Eng=int(input("Enter your English score: "))
Avg=(Math+Science+Eng)/3
print('='*30)
print(f'     STUDENT PROFILE     ')
print(f'Name:      {name}')
print(f'Age:       {age}')
print(f'Average:   {Avg}')
print('='*30)

