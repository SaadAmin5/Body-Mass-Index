#finding body mass index

def BMI (weight, height):
    formula=(weight / height)
    return formula

w=int(input('Enter your \'Weight\': '))
h=int(input('Enter your \'Height\': '))

a=BMI(weight=w, height=h)

print('\n')
print('Your Body Mass Index is: ', a)