# -*- coding: CP1251 -*-

upLimit = 100000;
lowLimit = 0;
print("��������� ����� �� %d �� %d."%(upLimit, lowLimit));
while upLimit != lowLimit:
    currentNumber = int((upLimit + lowLimit) / 2);
    print("���������� ����� ������ %d (Y/N)?"%currentNumber);
    while 1:
        answer = input();
        if ((answer == 'Y') or (answer == 'y')):
            lowLimit = currentNumber+1;
            break;
        else: 
            if ((answer == 'N') or (answer == 'n')):
                upLimit = currentNumber;
                break;

print("���������� ����� ��� %d (Y/N)?"%lowLimit);
while 1:
    answer = input();
    if ((answer == 'Y') or (answer == 'y')):
        print("���������� ����� �������.");
        break;
    else:
        if ((answer == 'N') or (answer == 'n')):
            print("������ ������������ �������������.");
            break;
