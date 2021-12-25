time = int(input("Duration: "))
d = 86400
h = 3600
m = 60
s = 1
if time >= d:
    print((time // d) , "day")
    if time >= h:
        print((time % d // h) , "hour")
        if time >= m:
            print((time % d % h // m) , "min")
            if time >= s:
                print ((time % d % h % m) , "sec")




