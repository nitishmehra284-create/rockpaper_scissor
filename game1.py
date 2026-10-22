import random

computer=random.randint(1,99)
tries=0
while True:
    tries=tries+1
    human=int(input("guess your number between 1-99:"))
    
    if human<1 or human >99:
        print("choose number bewteen range")
        continue
    if human == computer:
        print(f"congretulaton you won 🎉🎊 in tries{tries}")
        break
        
    elif human>computer:
        print("sorry wrong guess go lower")
    elif human<computer:
        print("sorry wrong guess go higher ")
        
    
    