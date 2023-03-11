def moving_average(average,n,max,data):
    for i in range(max):
        avg = 0
        if i>=20:
            for j in range(n):
                avg = avg + data
                # print(data['Close'][j])
            avg = avg / n
            average.append(avg)
        else:
            average.append(0)