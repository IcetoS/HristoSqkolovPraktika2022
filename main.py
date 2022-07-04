# Христо Сяколов, XIГ-клас
#Zad1
print("Христо Иванов Сяколов от 11Г")
#Zad2
print("%" * 11)
#Zad3
name = 'Христо Сяколов'
print(name)
клас = "11Г"
print(клас)
Номер = 24
print(Номер)
число_is_passed = True
print(число_is_passed)
инава_в_XII_ти = True
print(инава_в_XII_ти)
#Zad4
name = input('Как се казваш?')
print('Здравей!' + name)
#Zad5
любим_цвят = input('Кой е любимият ти цвят?')
print(name + " харесва" + любим_цвят )
#Zad6
дата_на_раждане = input('дата на раждане')
възраст = 2022 - int(дата_на_раждане)
print(възраст)
#Zad7
teglo_kilogrami = input('Teglo(kilogrami)')
teglo_poundove = int(teglo_kilogrami) / 0.45
print(teglo_poundove)
#Zad8
string_1 = "ПГЕЕ'Производствена практика 2022'"
string_2 = 'ПГЕЕ "Производствена практика" 2022 8.1'
print(string_1 + string_2)
#Zad9
print(string_1[0])
print(string_1[-1])
print(string_1[-2])
print(string_1[0:5])
print(string_1[5:])
print(string_1[:5])
print(string_1[:])
#Zad10
ime_res = 'Hristo'
familno_res = 'Sqkolov'
msg = ime_res + ' ' + familno_res + ' e programist'
print(msg)
str1 = 'ПГЕЕ Производствена практика 2022'
print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1.find('ПГЕЕ'))
print(str1.replace('2022', '2021/2022' ))
#Zad11
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 4)
print(10 // 4)
print(10 % 5)
print(10 ** 5)
Eq1 = (11 + 4) * 2 ** 2
print(Eq1)
Eq2 = 3.9
print(round(Eq2))
print(abs(-2.9))
#Zad12
import math
print(math.ceil(3.9))
print(math.floor(3.9))
  #Функцията ceil() на Python закръгля число до най-близкото цяло число или цяло число. Python floor() закръгля десетичните знаци надолу до най-близкото цяло число
#Zad13
studeno_e = True
toplo_e = False

if toplo_e:
    print("Topul den e")
    print("Consumirai poveche voda")
elif studeno_e:
    print("Denqt e studen")
    print("Nosi debeli drehi")
else:
    print("Dobur den e!")

print('Pojelavam vi priten den; ')

cena = 10000
dobur_chovek = False

if dobur_chovek:
    namalenie = 0.1 * cena
else:
    namalenie = 0.2 * cena
print(f"Namalenie: ${namalenie}")


