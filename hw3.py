from cmath import sqrt


class hw3:

    def PrintWeather(self):
        day = 25
        month ='Июнь'
        temp = 15
        if(temp<0):
            print('Холодно,лучше остаться дома')
        print('Сегодня {mnth} {d}-го  На улице {tmp} градусов'.format(mnth=month,d=day,tmp = temp))

    def CalculateSpeed(self):
        speed_kmh = 1079252848.8
        speed_kms = speed_kmh/3600.0
        print('Скорость света равна {speed}'.format(speed = int(speed_kms)))

    def ProductsList(self):
        list = ['Чай','Сахар','Хлеб','Молоко']
        count = 0
        for _ in list:
            count+=1
        print('У тебя {0} продуктов,где {0} - значение переменной count'.format(count))
        return list

    def PrintProducts(self,list):
        print('Вывод продуктов: ')
        for pr in list:
            print('\t',pr)


    def EvenCount(self,list):
        res = []
        for pr in list:
            if(len(pr)%2==0):
                res.append(pr)
        return res

    def Prime(self,number):
        for x in range(2,number//2+1):
            if(number%x==0):
                print('Составное')
                return
        print('Простое')

    def Fib(self,n):
        fib1 = 1
        fib2 = 1
        i = 0
        while i < n - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i +=1
        return fib2
        
    
   






hw = hw3()
#1
hw.PrintWeather()
#2
hw.CalculateSpeed()
#3
list = hw.ProductsList()
#4
hw.PrintProducts(list)
#5
print(hw.EvenCount(list))
#6
hw.Prime(17)
hw.Prime(100)
#7
print(hw.Fib(6))