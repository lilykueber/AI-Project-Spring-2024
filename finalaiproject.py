animalGroup = ['cat','bunny','dog','snake', 'lizard']
foodGroup = ['pizza','pasta','donut','steak','carrot']
animalQuestions = ['Is it furry?(yes/no)', "Does it have legs(yes/no)",'Does it growl?(yes/no)'
                   , "Does it hop?(yes/no)"]
foodQuestions = ["Is it a grain?(yes/no)", "Is it a vegetable?(yes/no)",
                 "Can you eat it with your hands?(yes/no)","Is it sweet?(yes/no)"] 
def ai2():
    i = 0
    while i == 0:
        groupInput = input("Enter 1 to pick an animal or Enter 2 to pick a food: ")
        questionNum = 0
        if groupInput == "1":
            print("Choose an animal from this list: " + ', '.join(animalGroup))
            while questionNum != len(animalQuestions):
                q1 = input(animalQuestions[questionNum]).lower()
                if q1 == 'y' or q1 == 'yes':
                    q1 = True
                else:
                    q1 = False
                if q1:
                    questionNum += 2
                    q3 = input(animalQuestions[questionNum]).lower()
                    if q3 == 'y' or q3 == 'yes':
                        q3 = True
                    else:
                        q3 = False
                    if q3:
                        questionNum +=1
                        q4 = input(animalQuestions[questionNum]).lower()
                        if q4 == 'y' or q4 == 'yes':
                            q1 = True
                        else:
                            q4 = False
                        if q4:
                            print("bunny")
                            questionNum = len(animalQuestions)
                        else:
                            print("dog")
                            questionNum = len(animalQuestions)
                    else:
                        print("cat")
                        questionNum = len(animalQuestions)
                else:
                    questionNum += 1
                    q2 = input(animalQuestions[questionNum]).lower()
                    if q2 == 'y' or q2 == 'yes':
                        q2 = True
                    else:
                        q2 = False
                    if q2:
                        print("lizard")
                        questionNum = len(animalQuestions)

                    else:
                        print("snake")
                        questionNum = len(animalQuestions)
            i = 1
        elif groupInput == "2" or groupInput == "2 ":
            print("Choose a food from this list: " + ', '.join(foodGroup))
            while questionNum != len(foodQuestions):
                q1 = input(foodQuestions[questionNum]).lower()
                if q1 == 'y' or q1 == 'yes':
                    q1 = True
                else:
                    q1 = False
                if q1:
                    questionNum += 2
                    q3 = input(foodQuestions[questionNum]).lower()
                    if q3 == 'y' or q3 == 'yes':
                        q3 = True
                    else:
                        q3 = False
                    if q3:
                        questionNum +=1
                        q4 = input(foodQuestions[questionNum]).lower()
                        if q4 == 'y' or q4 == 'yes':
                            q1 = True
                        else:
                            q4 = False
                        if q4:
                            print("donut")
                            questionNum = len(foodQuestions)
                        else:
                            print("pizza")
                            questionNum = len(foodQuestions)
                    else:
                        print("pasta")
                        questionNum = len(foodQuestions)
                else:
                    questionNum += 1
                    q2 = input(foodQuestions[questionNum]).lower()
                    if q2 == 'y' or q2 == 'yes':
                        q2 = True
                    else:
                        q2 = False
                    if q2:
                        print("carrot")
                        questionNum = len(foodQuestions)

                    else:
                        print("steak")
                        questionNum = len(foodQuestions)
            i = 1

        else:
            print("Pick the number 1 or 2")

if __name__ == "__main__":
    ai2()
