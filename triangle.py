from line import line


def topTriangle(yBase, x1Base, x2Base, x1Top, y1Top):
    pts = []
    if x1Base > x1Top:
        border1 = line(x1Base, yBase, x1Top, y1Top)
    else:
        border1 = line(x1Base, yBase, x1Top, y1Top)[::-1]
    if x2Base > x1Top:
        border2 = line(x2Base, yBase, x1Top, y1Top)
    else:
        border2 = line(x2Base, yBase, x1Top, y1Top)[::-1]
    i1 = i2 = 0
    print border1, border2, y1Top, yBase
    for y in range(y1Top, yBase + 1):
        while border1[i1][1] != y:
            i1 += 1
        while border2[i2][1] != y:
            i2 += 1
        for x in range(border1[i1][0], border2[i2][0] + 1):
            pts.append((x, y))
    return pts

def botTriangle(yBase, x1Base, x2Base, x1Bot, y1Bot):
    pts = []
    if x1Base > x1Bot:
        border1 = line(x1Base, yBase, x1Bot, y1Bot)[::-1]
    else:
        border1 = line(x1Base, yBase, x1Bot, y1Bot)
    if x2Base > x1Bot:
        border2 = line(x2Base, yBase, x1Bot, y1Bot)[::-1]
    else:
        border2 = line(x2Base, yBase, x1Bot, y1Bot)
    i1 = i2 = 0
    print border1, border2, y1Bot, yBase
    for y in range(yBase, y1Bot + 1):
        while border1[i1][1] != y:
            i1 += 1
        while border2[i2][1] != y:
            i2 += 1
        for x in range(border1[i1][0], border2[i2][0] + 1):
            pts.append((x, y))
    return pts

def triangle(x1, y1, x2, y2, x3, y3):
    xs = [x1, x2, x3]
    ys = [y1, y2, y3]
    for i in range(3):
        if ys[i] == max(ys) || ys[i] == min(ys):
            continue

if __name__ == '__main__':
    print 'top tests'
    print topTriangle(10, 0, 5, 4, 6)
    print topTriangle(10, -2, 3, 4, 6)
    print topTriangle(10, 8, 13, 4, 6)
    print 'bot tests'
    print botTriangle(10, 0, 5, 4, 14)
    print botTriangle(10, -2, 3, 4, 14)
    print botTriangle(10, 8, 13, 4, 14)