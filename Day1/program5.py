lst=[]
player1=int(input("Enter the scrore of ist player in 60 balls:"))
lst.append(player1)
player2=int(input("Enter the score of 2nd player in 60 balls:"))
lst.append(player2)
player3=int(input("Enter the score of 3rd player in 60 balls"))
lst.append(player3)
for i in range(0,3):
    print("strike rate of player:",i+1,"=",(lst[i]*100)/60)
for i in range(0,3):
    print("If played 60 ball more player",i+1,"will score",lst[i]*2)
for i in range(0,3):
    print("maximum no. of sixes player",i+1,"have hit=",lst[i]//6)
