import random
List2 = []
length2 = 100  #2000    #The number of indexes that are going to be used in Enc.cpp
system_random = random.SystemRandom()
while len(List2) < length2:
    IN = system_random.uniform(0, 10000)
    T = IN 
    while T > length2:
        IN3 = system_random.uniform(1, 129)
        T = T - IN3
    while T < 0:
        IN4 = system_random.uniform(1, 99)                      #Generating random numbers that can be used as indexes for KEY#2
        T = T + IN4
    while round(T) not in List2:
        List2.append(round(T))
for X in List2:
    print(X, end = " ")

