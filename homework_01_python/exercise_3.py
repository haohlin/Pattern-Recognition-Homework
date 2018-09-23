a = int(input('salary= '))
w = 100000
if a <= w:
    bonus = 0.1*a
elif a < 2*w:
    bonus = 0.1*w + (a-w)*0.075
elif a < 4*w:
    bonus = 0.1*w + 0.075*w + (a - 2*w)*0.05
elif a < 6*w:
    bonus = 0.1*w + 0.075*w + 2*w*0.05 + (a - 4*w)*0.03
elif a < 10*w:
    bonus = 0.1*w + 0.075*w + 2*w*0.05 + 2*w*0.03 + (a - 6*w)*0.015
else : bonus = 0.1*w + 0.075*w + 2*w*0.05 + 2*w*0.03 + 4*w*0.015 + (a - 10*w)*0.01
print(bonus)