


working = True

number = 1 

print "!!!!!FIZZ BUZZ!!! "

while working:
    inp = raw_input("number = {0} - choose answer: ".format(number))
    #print inp
    if not (inp in ('o', 'f', 'b')):
        print "incorrect response"
        break
    if (number % 5) == 0 and (inp != 'f'):
        print " FIZZ"
        break
    if (number % 7) == 0 and (inp != 'b'):
        print " BUZZ"
        break
    number += 1
#    working = False
print "GAME OVER"
