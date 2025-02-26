from random import *

#Ül 1

count_integers = 0
i = 0
while i < 15:
    num = float(input(f"Sisestage number {i + 1}: "))

    if num == int(num):
        count_integers += 1

    i += 1
print("\ntäisarvude arv:", count_integers)

#Ül 2

A = int(input("Sisestage number A: "))

if A > 0:
    total_sum = 0
    i = 1

    while i <= A:
        total_sum += i
        i += 1

    print("Füüsiliste arvude summa vahemikus 1 kuni", A, "võrdub", total_sum)
else:
    print("Sisestage loomulik number (A > 0).")

#Ül 3

product = 1

i = 0
while i < 8:
    num = int(input(f"Sisestage arv {i+1}: "))
    if num > 0:
        product *= num
    i += 1
print("Positiivsete arvude korrutis:", product)

#Ül 4

num = 10
while num <= 20:
    print(f"Arvu {num} ruut on {num**2}")
    num += 1

#Ül 5

N = int(input("Sisestage arvude kogus: "))
negative_sum = 0
i = 0
while i < N:
    num = int(input("Sisestage arv: "))
    if num < 0:
        negative_sum += num
    i += 1
print("Negatiivsete arvude summa:", negative_sum)

#Ül 6
N = int(input("Sisestage numbrite arv (N): "))
count_positive = 0
count_negative = 0
count_zero = 0

i = 0
while i < N:
    num = float(input(f"Sisestage number {i + 1}: "))

    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    else:
        count_zero += 1

    i += 1
print("\nTulemused:")
print("Positiivsete arvude arv:", count_positive)
print("Negatiivsete arvude arv:", count_negative)
print("Nullide arv:", count_zero)

#Ül 7

A = int(input("Sisestage intervalli algus A: "))
B = int(input("Sisestage intervalli B lõpp: "))
K = int(input("Sisestage number K (korrutis): "))
num = A
while num <= B:
    if num % K == 0:
        print(num)
    num += 1

#Ül 8
a = 0
while a < 10:
    print(f"Пара {a + 1}:")
    try:
        num1 = float(input("Sisestage esimene number: "))
        num2 = float(input("Sisestage teine number: "))

        if num1 > num2:
            print("Suurem arv:", num1)
        elif num2 > num1:
            print("Suurem arv:", num2)
        else:
            print("Numbrid on võrdsed")

    except ValueError:
        print("Viga: Sisestage numbriline väärtus!")

    print()
    a += 1

#Ül 9
rand_num = random.randint(1, 9)
print("Random number:", rand_num)

product = 1
found = False
for num in range(11, 100, 2):
    if num % rand_num == 0:
        product *= num
        found = True

if found:
    print("Numbrite korrutis:", product)
else:
    print("Ei ole olemas kahekohalisi paarituid numbreid, mis oleksid jagatavad arvuga", rand_num)


#Ül 10
N = int(input("Sisestage heinategijate arv (N): "))
m = float(input("Sisestage esimese heinaküünla tööaeg (m tundi): "))
step = 1 / 6  

total_hours = 0
i = 0

while i < N:
    total_hours += m + i * step
    i += 1

print(f"Kogu meeskonna kogutööaeg: {round(total_hours, 2)} tundi")

#Ül 11
import random

K = random.randint(1, 50)
print(f"Genereeritud number: {K}")

product = 1

for num in range(11, 100, 2):
    if num % K == 0:
        product *= num

if product>1:
    print(f"Kahekohaliste paaritute arvude korrutis, mis on jagatavad {K}: {product}")
else:
    print(f"Ei ole kahekohalisi paarituid numbreid, mis on jagatavad {K}.")

#Ül 12
N = int(input("Sisestage heinategijate arv: "))
m = int(input("Sisestage esimese heinaküünla tööaeg (tundid): "))

total_hours = 0
for i in range(N):
    total_hours = m + (i * 10 / 60)

print(f"Kogu meeskond töötas {round(total_hours)} tundi.")

#Ül 13
count = 0
total_sum = 0

for number in range(100, 1001):
    if number % 7 == 0:
        count += 1
        total_sum += number
print(f"jagatavate arvude arv: {count}")
print(f"jagatavate arvude summa: {total_sum}")

#Ül 14
import random
N = random.randint(1, 20)
product = 1

for i in range(1, N + 1):
    product *= i

print(f"Juhuslik number N: {N}")
print(f"Numbrite 1 kuni {N}: {product}")


#Ül 15
for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print()

#Ül 16
n = 9
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i:
            print(i, end=' ')
        else:
            print(0, end=' ')
    print()

#Ül 17
for i in range(1, 10):
    print(f"2*{i}={2 * i}")

#Ül 18
for num in range(20, 51):
    if num % 3 == 0 and num % 5 != 0:
        print(num)

#Ül 19
for num in range(35, 88):
    if num % 7 in {1, 2, 5}:
        print(num)

#Ül 20
total = 0
for num in range(1, 51):
    if num % 5 == 0 or num % 7 == 0:
        total += num
print("Summa:", total)
