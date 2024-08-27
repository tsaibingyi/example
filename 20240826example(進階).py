payment=int(input("付款="))
price=int(input("售價="))
change_type=[1,5,10,50,100,500,1000]

def make_change(pay,pri):
    change=[]
    change_left=pay-pri
    if change_left<0:
        print("付的錢不夠")
    else:
        for i in sorted(change_type, reverse=True):
            while change_left>=i:
                change.append(i)
                change_left-=i
        print(change)

make_change(payment,price)