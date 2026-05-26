import math
ocrug = 0

def so():
    try:
        global ocrug
        ocrug = int(input("До скольки вы хотите округлять?\nПримеры:\n Введите 1 если хотите такое округление: 14.8\n Введите 2 если хотите такое округление: 14.85 и т.д."))
        
    except ValueError:
        print("Вы ввели что то не так")

def cilindre():
    global ocrug
    try:
               
        print("Калькулятор объёма стакана, кружки или ведра")
        print("   (если верх шире низа — это сюда)")
        print("Просто введя больший, меньший диаметр и высоту цилиндра вы узнаете его объем")
        h = input("Введи высоту:\n")
        Rmax = input("Введи больший диаметр:\n")
        Rmin = input("Введи меньший диаметр:\n")
        
        h = float(h)
        Rmax = float(Rmax)
        Rmin = float(Rmin)
        Rmax = Rmax / 2
        Rmin = Rmin / 2
        if Rmin<=0 or Rmax<=0 or h<=0:
            print("Ошибка: Число должно быть больше нуля!")
            return
        result = 1/3 * math.pi * h *(Rmax ** 2 + Rmax * Rmin + Rmin ** 2)
        result = round(result, ocrug)
        print("Результат:", result)
    except ValueError:
        print("Вы ввели что то не так:(")
while (1):
    try:
        print("1.Узнать объем цилиндра")
        print("2.Настроить округление")
        comand = int(input("Введите порядковый номер: "))
    
        if comand == 1:
            cilindre()
        if comand == 2:
            so()
    except ValueError: 
        print("Вы ввели что то не так:(")