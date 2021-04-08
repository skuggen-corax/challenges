from pwn import remote, log, context

first_fibs = {0: 0, 1:1, 2:1}

i = 3
n1 = 1
n2 = 1 

while i <= 1000:
    first_fibs[i] = first_fibs[i-1] + first_fibs[i-2]

    i+=1

#print(first_fibs)

def fib(number):
    return first_fibs[number]

c = remote('fibonacci', 7600)

question = c.recve().decode()

answer = eval(question)

c.sendline(answer.encode())

#eval(r.text)

#print(fib(452))
