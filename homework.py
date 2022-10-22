
def home_work(begemot):
    lst=begemot.split()
    big_string=0
    for small_begemot in lst:
        big_letter= 0 
        small_letter=0 
        for smollest_begemot in small_begemot:
            if smollest_begemot.isupper():
                  big_letter+=1
            elif smollest_begemot.islower():
              small_letter+=1   
            else:
             small_letter+=1
        if big_letter>small_letter:
            big_string+=1
    return str(big_string/len(lst)*100)+'%'

print(home_work(' AJd akd AKd ФОА '))
