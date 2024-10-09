assignmentone = int(input("What is your score in Assignment One?"))
assignmenttwo = int(input("What is your score in Assignment Two?"))
assignmentthree = int(input("What is your score in Assignment Three?"))
assignmentfour = int(input("What is your score in Assignment Four?"))
finalessay = int(input("What is your score in Final Essay?"))
finalscore = ((assignmentone*10 + assignmenttwo*15 + assignmentthree*20 + assignmentfour*5 + finalessay*50)/100)
finalscore = int(finalscore)
print("Your final score is: ",finalscore)
if finalscore >= 85:
    print("Congratulation. You get a Distinction.")
elif finalscore >= 70 and finalscore <=  84:
    print("Congratulation. You get an A.")
elif finalscore >= 60 and finalscore <= 69:
    print("Great. You get a B.")
elif finalscore >= 50 and finalscore <= 59:
    print("Not bad. You get a C")
elif finalscore <= 49:
    print("Fail")