import sys
import math

MAX_DENOM = 1000000
EPSILON = 0.000001

def getFraction(d):
    numer = 0
    denom = 0

    low = [0, 1]
    mid = [1, 1]
    high = [1, 1]

    while mid[1] < MAX_DENOM:
        if math.fabs(mid[0] / mid[1] - d) < EPSILON:
            return mid
        elif math.fabs(low[0] / low[1] - d) < EPSILON:
            return low
        elif math.fabs(high[0] / high[1] - d) < EPSILON:
            return high

        # Skip this for first iteration
        if mid[0] == high[0] and mid[1] == high[1]:
            mid[0] = low[0] + high[0]
            mid[1] = low[1] + high[1]
            continue

        if d * mid[1] < mid[0]:
            high[0] = low[0] + mid[0]
            high[1] = low[1] + mid[1]
        else:
            low[0] = mid[0] + high[0]
            low[1] = mid[1] + high[1]
        mid[0] = low[0] + high[0]
        mid[1] = low[1] + high[1]

    return mid

def main():
    s = input('Enter a number: ')
    if '/' in s:
        frac = s.split('/')
        n = str(int(frac[0]) / int(frac[1]))
        num = n.split('.')
    else:
        num = s.split('.')

    if len(num) == 1:
        print(num[0])
    elif len(num) == 2:
        i = int('0' + num[0])
        d = float('0.' + num[1])

        f = getFraction(d)

        print(i  * f[1] + f[0], end=' / ')
        print(f[1])
    else:
        print("Nope")
        sys.exit()

if __name__ == '__main__':
    main()
