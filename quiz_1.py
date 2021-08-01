seat = []
for i in range(1,21):
    seat.append("A{}".format(i))
    if i % 2 == 1 :
        print(seat[i-1], end = " ")
