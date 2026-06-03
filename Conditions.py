Math=int(input("Enter your Math score: "))
Science=int(input("Enter ur Science score: "))
Eng=int(input("Enter your English score: "))
Social=int(input("Enter your social score: "))
Tam=int(input("Enter your Tamil score: "))
Avg=(Math+Science+Eng+Social+Tam)/5

if Math<=40 or Science<=40 or Eng<=40 or Social<=40 or Tam<=40:
    print("you failed")
else:
    print(f"Your Average:   {Avg}")
    if(Avg>=90):
        grade= "A"
    elif(Avg>=80):
        grade= "B"
    elif(Avg>=70):
        grade= "C"
    else:
        grade= "D"
    print(f"Grade:{grade}" )


    

    

