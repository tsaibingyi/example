guess_me=7
number=1

while True:
    if number<guess_me:
        print(number, "too low")
    elif number==guess_me:
        print(number, "found it!")
        break
    else:
        print(number, "oops")
        break
    number+=1

    