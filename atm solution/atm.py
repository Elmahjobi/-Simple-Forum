
def withDraw(money,request):
    paperValues=[100,50,10,5,1]
    assert request>0, "Invalid input"
    assert request<=money, "Balance Not Enough !"
    remaining=money-request
    
    print "*************"
    print "Delivering "+str(request)+"$ to client:"
    for x in paperValues:
        while (request>=x):
            print "give"+str(x)
            request-=x
    return remaining
    print "Done !"

#test any value here
balance=500
balance=withDraw(balance,200)
balance=withDraw(balance,119)
balance=withDraw(balance,181)
balance=withDraw(balance,1)
