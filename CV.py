def summa_cisel(n):
    sum = 0

    while n > 0:
        dig = n % 10
        sum = sum+dig
        n = n//10
    return sum

def f_1(n_customers):
    massiv_1 = [0 for i in range(64)]
    for j in range (n_customers+1):
        sum_j = summa_cisel(j)
        massiv_1[sum_j]+=1
    return massiv_1

def f_2(m_customers,id_customers):
    massiv_1 = [0 for i in range(64)]
    for j in range(m_customers+ 1):
        index = id_customers+j
        sum_j = summa_cisel(index)
        massiv_1[sum_j] += 1
    return massiv_1

#n = int(input("n:"))
x = int(input("Kolicestvo klientov:"))  #
y = int(input("ID klienta:")) #
massiv_prosto = []
#massiv_prosto = f_1(n)
massiv_prosto = f_2(x,y)
for y in range (len(massiv_prosto)):
    print(f"Сумма чисел {y}: {massiv_prosto[y]}")

