def power_pow(y, d, n):
    z = 1
    while d>1:
        if d%2 == 1: 
            z = (z*y)%n
            d = d-1
        d = d // 2
        y = (y*y)%n
    return (y*z)%n