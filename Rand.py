import random
import time
List = []
Alpd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symb = ['!', '+', "=", '?', "/", "@", '#', '$', '%', '&', '*', '(', ')', '-', '~']
Alpu = []
for al in Alpd:
    Alpu.append(al.upper())
N = 0
length = 100  #2500               #Select the length for KEY#2
while len(List) < length:
    system_random = random.SystemRandom()
    R1 = system_random.uniform(1000000000, 120000000000000000000000000000)                                       #Initialize random numbers START
    RP = system_random.uniform(2, 60)
    def wait():
        RT = system_random.uniform(0, 0.5)
        time.sleep(RT)
    R5 = system_random.uniform(10000000, 900000000000000000000000000000)
    R6 = system_random.uniform(10000000, 1000000000000000000000000000000)
    R7 = system_random.uniform(1000000, 340000000000000000000000000000000)
    #wait()                                                                             UNCOMMENTING WILL +SECURITY +TIME
    R8 = system_random.uniform(1000000, 1000000000000000000000000000)
    R9 = system_random.uniform(100000, 1000000000000000000000000000)
    R10 = system_random.uniform(1000000, 30000000000000000000000000000)
    R11 = system_random.uniform(1000000, 10000000000000000000000000)
    R12 = system_random.uniform(1000000, 100000000000000000000000000)
    R13 = system_random.uniform(1000000, 100000000000000000000000000)
    #wait()
    R14 = system_random.uniform(100000, 200000000000000000000000000)
    R15 = system_random.uniform(1000000, 40000000000000000000000000)
    R16 = system_random.uniform(1000000, 300000000000000000000000000)
    R17 = system_random.uniform(1000000, 60000000000000000000000000)
    R18 = system_random.uniform(1000000, 100000000000000000000000000)
    R19 = system_random.uniform(1000000, 7000000000000000000000000000)
    R20 = system_random.uniform(1000000, 10000000000000000000000000)
    R21 = system_random.uniform(1000000, 1000000000000000000000000000)
    R22 = system_random.uniform(10000000, 10000000000000000000000000)
    #wait()
    R23 = system_random.uniform(1000000, 10000000000000000000000)
    R24 = system_random.uniform(100000, 70000000000000000000000000000)
    R25 = system_random.uniform(1000000, 9000000000000000000000000)
    R26 = system_random.uniform(1000000, 1914940200000000000000000000)
    R27 = system_random.uniform(1000000, 129464000000000000000000000)
    R2 = system_random.uniform(10000000, 100000000000000000000000000)
    R28 = system_random.uniform(2000000, 10000000000000000000000000000)
    #wait()
    R29 = system_random.uniform(1000000, 10000000000000000000000000000000)
    R30 = system_random.uniform(3000000, 10000000000000000000000000)
    R31 = system_random.uniform(1, 105)
    R33 = system_random.uniform(1000000, 1000000000000000000000000000)
    R34 = system_random.uniform(1000000, 1000000000000000000000000)
    R35 = system_random.uniform(1000000, 2000000000000000000000000000)
    R36 =system_random.uniform(2, 60)
    R37 =system_random.uniform(2, 60)
    R38 =system_random.uniform(1000000, 9000000000000000000000000000)
    R39 = system_random.uniform(1000000, 80000000000000000000000000000)
    RL = round(system_random.uniform(100, 400))                                                 #INITIALIZATION END
    #RL2 = round(system_random.uniform(4, 25))
    value = R1 + R2 * R5 + R6 * R7 * R8 / (R9 + R10) * R11 + R12 / R13 % R28 * R14 * (R15 + R16) / R17 * R18 + R19 % R20 * R23 * R24 % R25 * R26 * R27 % R29 / R30 * R31**RP + (R33 * R34)* R35 * R36**R37 - R38 - R39   
    #PLUG THEM IN THIS FORMULA
    while value > length:
        R4 = system_random.uniform(1, 100000)
        R3 = system_random.uniform(0, R4)
        value = value / R3
    value = round(value)
    while value not in List:
        List.append(value)
    while N < RL: 
        RI = round(system_random.uniform(0, 25))                            #ADD SYMBOLS AND LETTERS FROM THE INITIALIZED LISTS
        RI2 = round(system_random.uniform(0, 25))
        RI200 = round(system_random.uniform(0,14))
        RN = Alpd[RI]
        RN2 = Alpu[RI2]
        RN3 = symb[RI200]
        List.append(RN + RN2 + RN3)
        N += 1
#print(List)
for X in List:
   print(X, end = '')                       #OUTPUT
print("")
