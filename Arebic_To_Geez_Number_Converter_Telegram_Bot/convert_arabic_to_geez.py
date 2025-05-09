def convert_to_geez(num):
    geez = ""
    # ten_tho = ""
    # hun = ""
    # tho = ""
    # ten = ""
    # uni = ""
    rem = 0

    def number(num):
        if num == 1:
            return "፩"
        if num == 2:
            return "፪"
        if num == 3:
            return "፫"
        if num == 4:
            return "፬"
        if num == 5:
            return "፭"
        if num == 6:
            return "፮"
        if num == 7:
            return "፯"
        if num == 8:
            return "፰"
        if num == 9:
            return "፱"
        if num == 10:
            return "፲"
        if num == 20:
            return "፳"
        if num == 30:
            return "፴"
        if num == 40:
            return "፵"
        if num == 50:
            return "፶"
        if num == 60:
            return "፷"
        if num == 70:
            return "፸"
        if num == 80:
            return "፹"
        if num == 90:
            return "፺"
        if num == 100:
            return "፻"
        return ""

    def ten_thousend(num):
        ten_tho = ""
        if num == 10000:
            ten_tho += number(num / 100)
            ten_tho += number(num / 100)
            return ten_tho
        else:
            rem = num / 100
            ten_tho += number(num / rem)
            num = rem
            rem = num / 100
            ten_tho += number(num / rem)
            ten_tho += number(rem)
            return ten_tho

    def thousend(num):
        tho = ""
        rem = num / 100
        tho += number(rem)
        tho += number(num / rem)
        return tho

    def hundred(num):
        hun = ""
        if num == 100:
            hun += number(num)
        else:
            rem = num / 100
            hun += number(rem)
            hun += number(num / rem)
        return hun

    def tenth(num):
        ten = ""
        rem = num % 100
        ten += number(rem)
        return ten

    def unit(num):
        uni = ""
        rem = num % 10
        uni += number(rem)
        return uni

    def unit_with_0(num):
        uni = ""
        rem = num % 10
        uni += number(rem)
        return uni

    if len(str(num)) == 1:
        geez += number(num)
        return geez
    elif len(str(num)) == 2:
        if num % 10 == 0:
            print(number(num))
        else:
            rem = num % 10
        geez += number(rem)
        geez += number(num - rem)
        geez = geez[::-1]
        return geez
    elif len(str(num)) == 3:
        if num == 100:
            return number(num)
        elif num % 100 == 0:
            return hundred(num)
        elif num % 10 == 0:
            geez += tenth(num)
            num = num - num % 100
            geez += hundred(num)[::-1]
            geez = geez[::-1]
            return geez
        elif num % 10 != 0 and str(num)[1] == "0":
            geez += unit_with_0(num)
            num = num - num % 10
            geez += hundred(num)[::-1]
            geez = geez[::-1]
            return geez
        else:
            geez += unit(num)
            num = num - num % 10
            geez += tenth(num)
            num = num - num % 100
            geez += hundred(num)[::-1]
            geez = geez[::-1]
            return geez
    elif len(str(num)) == 4:
        if num % 1000 == 0:
            geez += thousend(num)
            return geez
        elif num % 100 == 0:
            geez += hundred(num % 1000)[::-1]
            num -= num % 1000
            geez += thousend(num)
            geez = geez[::-1]
            return geez[1 : len(geez)]
        elif num % 10 == 0:
            if str(num)[-3] != "0":
                geez += number(num % 100)
                num -= num % 100
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num)
                geez = geez[::-1]
                return geez[1 : len(geez)]
            else:
                geez += number(num % 100)
                num -= num % 100
                geez += thousend(num)[::-1]
                geez = geez[::-1]
                return geez

        else:
            if "0" not in str(num):
                geez += unit(num)
                num = num - num % 10
                geez += tenth(num)
                num = num - num % 100
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num)
                geez = geez[::-1]
                return geez[1 : len(geez)]
            elif str(num)[-2] == "0" and str(num)[-3] != "0":
                geez += unit(num)
                num = num - num % 10
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num)
                geez = geez[::-1]
                return geez[1 : len(geez)]
            elif str(num)[-3] == "0" and str(num)[-2] != "0":
                geez += unit(num)
                num = num - num % 10
                geez += tenth(num)
                num = num - num % 100
                geez += thousend(num)[::-1]
                geez = geez[::-1]
                return geez
            elif str(num)[-2] == "0" and str(num)[-3] == "0":
                geez += unit(num)
                num = num - num % 10
                geez += thousend(num)[::-1]
                geez = geez[::-1]
                return geez
    elif len(str(num)) == 5:
        if num % 10000 == 0:
            geez += ten_thousend(num)
            geez = geez[::-1]
            return geez
        elif num % 1000 == 0:
            geez += thousend(num % 10000)[::-1]
            num -= num % 10000
            geez += ten_thousend(num)
            geez = geez[::-1]
            return geez
        elif num % 100 == 0:
            if str(num)[1] != "0":
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                if geez[3] == "፻":
                    geez = geez[:3] + geez[4:]
                else:
                    geez = geez[:4] + geez[5:]
                return geez
            else:
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
        elif num % 10 == 0:
            if "0" not in str(num)[:4]:
                geez += number(num % 100)
                num -= num % 100
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                if geez[3] == "፻":
                    geez = geez[:3] + geez[4:]
                else:
                    geez = geez[:4] + geez[5:]
                return geez
            elif str(num)[-3] == "0" and str(num)[-4] == "0":
                geez += number(num % 100)
                num -= num % 100
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            else:
                geez += number(num % 100)
                num -= num % 100
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
        else:
            if "0" not in str(num):
                geez += unit(num)
                num = num - num % 10
                geez += number(num % 100)
                num -= num % 100
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                if geez[3] == "፻":
                    geez = geez[:3] + geez[4:]
                else:
                    geez = geez[:4] + geez[5:]
                return geez
            elif str(num)[1:4] == "000":
                geez += unit(num)
                num = num - num % 10
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            elif str(num)[1:3] == "00":
                geez += unit(num)
                num = num - num % 10
                geez += number(num % 100)
                num -= num % 100
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            elif str(num)[2:4] == "00":
                geez += unit(num)
                num = num - num % 10
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            elif str(num)[1] == "0":
                geez += unit(num)
                num = num - num % 10
                geez += number(num % 100)
                num -= num % 100
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            elif str(num)[2] == "0":
                geez += unit(num)
                num = num - num % 10
                geez += number(num % 100)
                num -= num % 100
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                return geez
            elif str(num)[3] == "0":
                geez += unit(num)
                num = num - num % 10
                geez += hundred(num % 1000)[::-1]
                num -= num % 1000
                geez += thousend(num % 10000)[::-1]
                num -= num % 10000
                geez += ten_thousend(num)
                geez = geez[::-1]
                if geez[3] == "፻":
                    geez = geez[:3] + geez[4:]
                else:
                    geez = geez[:4] + geez[5:]
                return geez
    elif len(str(num)) == 6:
        if num == 100000:
            rem = num / 100
            geez += number(num / rem)
            geez += thousend(rem)[::-1]
            geez = geez[::-1]
            return geez

    else:
        print("!!!!!!!!!for now it is enough,wait!!!!!!!!!!!!!")


num = int(input("enter a arebic number to be changed to GEEZ number:   "))
print(convert_to_geez(num))
