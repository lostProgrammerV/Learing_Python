class Quiz:
    @classmethod
    def quiz_anwsers(anwser):
        anwser = str(input("What does CPU stand for ?"))
        if anwser == "Central processing unit":
            print("Correct")
        else:
            print("Incorrect")

    @classmethod
    def playing(anwser):
        anwser = str(input("Do you want a play ?"))
        if anwser != "yes":
            quit()
        print("Let's play :)") 
  
    







