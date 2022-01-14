#Python Projects for beginners
#Binary Search Algorithm
#https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs#binary-search-algorithm

import random
def createlist():
    k=list()
    for i in range(0,10):
        num = random.randrange(0,101,2)
        k.append(num)
    return k
def check():
    check=0 #reference to check whether the user choiced a number among the list
    if user<0:
        print "Negative numbers are rejected!"
    elif user>100:
            print "Remember the numbers range is [0:100]"
    else:
        for num in k:
            if user==num:
                check=1
                break
        if check==1:
            print "Your number is within the list .."
        elif check==0:
            print "Unfortunately, you picked a number out from the list."
    return check
def half():
    ind=0
    h1=list()
    h2=list()
    iterator=iter(k)
    for i in range(0,5):
        num=iterator.next()
        h1.append(num)
    for i in range(5,10):
        num=iterator.next()
        h2.append(num)
    return h1,h2
def wh(): #In which half the number is? wh=1:first half,wh=2:second half
    it=iter(k)
    if check==1:
        for num in h1:
            if user==num:
                print "Situated in the First half."
                wh=1
        for num in h2:
            if user==num:
                print "Situated in the Second half."
                wh=2
    elif check==0:
        wh=0
    return wh
def apphalf(): #Maintaining just the half of list where situated the choiced number.
    if wh==1:
        apphalf=h1
        print "The New lists content:",apphalf
    elif wh==2:
        apphalf=h2
        print "The New lists content:",apphalf
    else:
        apphalf=k
    return apphalf    
#MAIN PROGRAM            
k=createlist()
print k #Showing the list generated randomly
user=int(input("Type a number from 0 to 100 : "))
check=check()
half()
h1,h2=half()
wh=wh() 
k=apphalf()