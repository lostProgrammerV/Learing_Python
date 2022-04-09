days = float(input('How many days do you intend to rent the car: '))
km = float(input('How many Km driven'))

paid_out =  (days * 60) + (km * 0.15)

print(f'The total to pay is {paid_out:.2f}')