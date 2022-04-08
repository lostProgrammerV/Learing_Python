#this exc is about adiction some values and has been
#chagend and improving and some fun, i think

money = float(input('How much money do you have: '))
while money < 0:
    money = float(input('Money cannot be negative retype: '))

brazilianReal = money * 4.70
yen =  money * 124.39
canadianDollar = money * 1.26

choose = str(input('Choose an option - Brazilian Real (1), Yen (2) and Canadian Dollar (3) or "All": '))

if choose == '1' or choose == 'Brazilian Realbrazilian' or choose == 'brBr' or choose == '$' or choose == 'real':
    print(f'{money} Dollar to BR$ is {brazilianReal:.2f}')
elif choose == '2' or choose == 'Yenyen' or choose == 'JPYjpy' or choose == '¥' or choose == '円' or choose == '圓':
    print(f'{money} Dollar to ¥ is {yen:.2f}')
elif choose == '3' or choose == 'Canadian Dollarcanadian' or choose == 'c$C$' or choose == 'CADcad':
    print(f'{money} Dollar to C$ is {canadianDollar:.2f}')
else:
    print('ascending order')
    print(f'{money} Dollar to C$ is {canadianDollar:.2f}')
    print(f'{money} Dollar to BR$ is {brazilianReal:.2f}')
    print(f'{money} Dollar to ¥ is {yen:.2f}')