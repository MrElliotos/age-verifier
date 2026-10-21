while True:
    try :  
     age = int(input("How old are you bro? "))
    except ValueError:
        print("write numbers, not letters")
        print("-"*30)
        continue
    if age == 0 or age == -1:
        print("can't be")
        break
    if age == 18:
        print("you were on the verge, come on in")
    elif age >= 19:
        print("come in")
   
    else :
        print("Get lost, you little runt") 
    print("-" * 30)    