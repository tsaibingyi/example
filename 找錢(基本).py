payment=int(input("付款="))
price=int(input("售價="))

def make_change(pay,pri):
    change=[]
    change_left=pay-pri
    while change_left>=50:
        change.append(50)
        change_left-=50
    while change_left>=10:
        change.append(10)
        change_left-=10
    while change_left>=5:
        change.append(5)
        change_left-=5
    while change_left>=1:
        change.append(1)
        change_left-=1
    print(change)

make_change(payment,price)