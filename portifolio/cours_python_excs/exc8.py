#this exc is about adiction some values and has been
#chagend and improving and some fun, i think

num = float(input('enter some number to multiplication table: '))

def line():
    print('-'*20)

for cont in range(10):
    line()
    print(f'{num} X {cont} = {num * cont:.2f}')
    line()
    if num * cont % 2 == 0:
        print(f'Is even: {num}')
    else:
        print(f'Is odd: {num}')