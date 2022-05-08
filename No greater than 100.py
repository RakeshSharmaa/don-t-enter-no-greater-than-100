print('If you enter no greater than 100 code will stop')

while True:
    a = int(input())
    if a < 100:
        print('Enter again')
        continue
    else:
        print('Oops entered greater than 100')
    break
