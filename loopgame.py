from sys import exit

def eighteenbox_shot():
    print"Shoot ball.Here is your chance to score?"

    next= raw_input(">")
    if "0" in next or "5" in next:
        in_score=int(next)
    else:
        dead("Man you lost an open chance")

    if in_score<7:
        print "Goaaaal.Perfect short"
        exit(0)
    else:
        dead("Shot saved by keeper")

def mid_field():
    print"You're in the mid-field chasing dead the ball"
    print"The opponent has the ball.Get it"
    print"How are you going to tackle him?"
    ball_taken=False

    while True:
        next=raw_input(">")

        if next=="press zero": 
           dead("This is a foul.You get a red card")
        elif next=="press five" and not ball_taken:
             print"Ball taken and opponent left for dead"
             ball_taken= True    
        elif next== "press five"and ball_taken:
                 dead("The opponent was too strong for you.")
        elif next=="shoot ball":
              eighteenbox_shot()
        else:
             print"I dont know what to do with the ball"

def loop_ball():
                 print"You decide to loop the ball past goal-keeper"
                 print"If keeper make a glimpse on the ball it goes out.No goal"
                 print"Do you loop or place?"

                 next=raw_input(">")

                 if "loop" in next:
                      start()
                 elif "place" in next:
                           dead("Thats too easy for keeper!")
                 else:
                      loop_ball()
def dead(why):
                 why,"Good shot"
                 exit(0)

def start():
                 print"You have the ball in 18box yard"
                 print"You can either loop the ball or fire a shot"
                 print"Which one do you take?"

                 next=raw_input(">")
                 if next=="shoot":
                    eighteenbox_shot()
                 elif next=="loop":
                       loop_ball()
                 else:
                      dead("You stumble about and ball taken by the defender")


start()                 

