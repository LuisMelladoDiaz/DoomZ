def clip(value, cap):
    if value < 1:
        return 1
    if value > (cap - 1):
        return cap - 1
    return value

def clip_behind_player(x1, y1, z1, x2, y2, z2):
    d = y1 - y2
    if(d==0): d = 1

    s = y1/d

    x1 = x1 + s*(x2-(x1))
    y1 = y1 + s*(y2-(y1))
    z1 = z1 + s*(z2-(z1))
    if(y1==0): y1 = 1

    return x1, y1, z1
