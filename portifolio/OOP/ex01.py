class Quiz:
    @classmethod
    def quiz_anwsers(anwser):
        anwser = str(input("What does CPU stand for ?"))
        if anwser == "Central processing unit":
            print("Correct")
        else:
            print("Incorrect")
        
        anwser = str(input("What does GPU stand for ?"))
        if anwser == "Graphics processing unit":
            print("Correct")
        else:
            print("Incorrect")

        anwser = str(input("What does RAM stand for ?"))
        if anwser == "Random access memory":
            print("Correct")
        else:
            print("Incorrect")

        anwser = str(input("What does PSU stand for ?"))
        if anwser == " ":
            print("Correct")
        else:
            print("Incorrect")

    @classmethod
    def playing(anwser):
        anwser = str(input("Do you want a play ?"))
        if anwser != "yes":
            quit()
        print("Let's play :)") 
  
    







