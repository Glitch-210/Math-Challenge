import random
import time

op = ["+","-","*"]
min = 3 
max = 12
total_problems = 10
def gen_prb():
    left = random.randint(min,max) 
    right = random.randint(min,max)
    operator = random.choice(op) #randomly select op from the list

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0 
input("Press Enter to start!")
print("---------------------")

start = time.time()
for i in range(total_problems):
    expr,ans = gen_prb()
    while True:
        guess = input("Problem # " + str(i + 1) + " : "+ expr + " = ")
        if(guess == str(ans)):
            break  
        wrong += 1

end_time = time.time()
total_time = round(end_time - start)

print("---------------------")
print(f"Nice Work,You Finished this quiz in {total_time} seconds!")