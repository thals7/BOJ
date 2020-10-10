Word = list(str(input()))
Num = []
for i in Word:
    if ord(i)<=67:
        Num.append(3)
    elif ord(i)>= 68 and ord(i)<=70:
        Num.append(4)
    elif ord(i)>= 71 and ord(i)<=73:
        Num.append(5)
    elif ord(i)>= 74 and ord(i)<=76:
        Num.append(6)
    elif ord(i) >= 77 and ord(i) <= 79:
        Num.append(7)
    elif ord(i)>= 80 and ord(i)<=83:
        Num.append(8)
    elif ord(i)>= 84 and ord(i)<=86:
        Num.append(9)
    else:
        Num.append(10)
print(sum(Num))