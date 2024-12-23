#i = 10
#while i < 50:
#    print(i)
#    i += 10

#while True:
#    answer = input("Enter yes or no: ")
#    if answer == 'no':
#            break
    
import random
random_num = random.randint(1, 5)
while True: 
     num = int(input("Guess the number from 1 to 5: "))
     if num != random_num:
          print("Try again..")
          continue
     break
print("Congratulations!", random_num) 