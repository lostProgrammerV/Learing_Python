distance = float(input('Enter your distance: '))

km = distance / 1000
hm = distance / 100
dam = distance / 10

dcm = distance * 10
cm = distance * 100
mm = distance * 1000

print(f'The distance converting of M to km, hm, dam, dcm, cm e mm:\n{km}km, {hm}hm, {dam}dam, {distance}m, {dcm}dcm, {cm}cm, {mm}mm')