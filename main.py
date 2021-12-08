from random import randint


n = int(input("Введіть розмір массиву: "))


def main(lst):
    negative = sum(filter(lambda x: x < 0, lst)) / 2
    end = list(map(lambda x: x + negative, lst))
    summa = "Сума елементів: " + str(sum(end))
    avarage = "Середнє арифметичне: " + str(sum(end)/len(end))
    end.insert(0, summa)
    end.insert(1, avarage)
    return end


print(main([randint(-50, 50) for i in range(n)]))
