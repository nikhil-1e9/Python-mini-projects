import random, sys
while True:     
     print("press r to (r)oll the dice or q to (q)uit")    
     user = input("what do you want to do\n")     
     if user == 'r':         
        number = random.randint(1,6)         
        print(number)     
     else:         
        sys.exit()
