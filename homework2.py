def dinosavr(day, month, year):
    month_30day = [4, 6, 9, 11]
    month_31day = [1, 3, 5, 7, 8, 10, 12]
    if (year and month <= 12 and day <= 31) and (month > 0 and day > 0):
        if (year and month < 10) or (year and month == 10 and day <= 9):
            if day <= 30 and month in month_30day:
                return True
            elif day <= 31 and month in month_31day:
                return True
            elif month == 2:
                if (day <= 28) or (year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and day == 29):
                    return True
                else:
                    return False
    else:
        return False

print(dinosavr(1, 2, 8))