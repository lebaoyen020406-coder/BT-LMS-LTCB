import random
money=100
win_count=0
lose_count=0

while money>0:
    print("Computer thinks a number from 1 to 100")
    comp_number=random.randint(1,100)
    level=int(input("Choose your level [1,2,3]? "))
    times=10 if level==1 else 5 if level == 2 else 3
    is_win=False
    money-=5

    for time in range(times):
        your_num=int(input("Enter your guessing number #"+str(time+1)+":"))
        if your_num == comp_number:
            is_win=True
            print("You are Genius!!!!")
            win_count+=1
            break
        else:
            if your_num < comp_number:
                print("Too low!")
            else:
                print("Too high!")
    if not is_win:
        print("Game Over! The number was:",comp_number)
        lose_count+=1

    print("---------------------")
    print("Wins:",win_count,"| Loses:",lose_count)
    print("Money left:",money)

    if money<=0:
        print("Game over!")
        break

    cont=input("Do you want to play again? [y/n]:")
    if cont.lower()=="n":
        break


print("Final report:")
print("Wins:",win_count)
print("Loses:",lose_count)
print("Money left:",money)

