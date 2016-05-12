# -*- coding: CP1251 -*-

upLimit = 100000;
lowLimit = 0;
print("Загадайте число от %d до %d."%(upLimit, lowLimit));
while upLimit != lowLimit:
    currentNumber = int((upLimit + lowLimit) / 2);
    print("Загаданное число больше %d (Y/N)?"%currentNumber);
    while 1:
        answer = input();
        if ((answer == 'Y') or (answer == 'y')):
            lowLimit = currentNumber+1;
            break;
        else: 
            if ((answer == 'N') or (answer == 'n')):
                upLimit = currentNumber;
                break;

print("Загаданное число это %d (Y/N)?"%lowLimit);
while 1:
    answer = input();
    if ((answer == 'Y') or (answer == 'y')):
        print("Загаданное число угадано.");
        break;
    else:
        if ((answer == 'N') or (answer == 'n')):
            print("Ответы пользователя противоречивы.");
            break;
