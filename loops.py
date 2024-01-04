x = 7
y = 7

i = j = 0

user = int(input('Введіть цифру від 1 до 10 для вибору фігури: '))

if user == 1:
    while i < y:
        while j < x:
            if i <= j:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 2:
    while i < y:
        while j < x:
            if i >= j:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 3:
    while i < y:
        while j < x:
            if i + j >= x:
                print(end=' ')
            elif i <= j:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 4:
    while i < y:
        while j < x:
            if i + j < x - 1:
                print(end='   ')
            elif i >= j:
                print('*', end='  ')
            else:
                print(end='  ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 5:
    while i < y:
        while j < x:
            if i <= j and i + j < x:
                print('*', end='  ')
            elif i >= j and i + j >= x-1:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 6:
    while i < y:
        while j < x:
            if i < j and i + j < x - 1:
                print(end='   ')
            elif i > j and i + j >= x:
                print(end='   ')
            else:
                print('*', end='  ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 7:
    while i < y:
        while j < x:
            if j > i:
                print(end='   ')
            elif i + j < x:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 8:
    while i < y:
        while j < x:
            if j > i:
                print(end='   ')
            elif i + j >= x-1:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 9:
    while i < y:
        while j < x:
            if j + i < x:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1

elif user == 10:
    while i < y:
        while j < x:
            if j + i >= x-1:
                print('*', end='  ')
            else:
                print(end='   ')
            j += 1
        print()
        j = 0
        i += 1