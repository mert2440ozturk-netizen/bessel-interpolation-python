
def bessel():

    """
    Bessel's central difference interpolation formula.
    This implementation uses 4 equally-spaced points.
    """
    print("-----------------------------------------------")

    n = int(input("Enter the number of points : "))

    if n < 4:
        print("At least 4 points are required.")
        return

    print("-----------------------------------------------")

    x = []
    y = []

    for i in range(n):
        x.append(float(input(f"x[{i}]: ")))
        y.append(float(input(f"y[{i}]: ")))

    # Build the forward difference table
    differenceTable = [[0.0]*n for i in range(n)]
    # for y values
    for i in range(n):
        differenceTable[i][0] = y[i]
    # for △y, △²y ...
    for j in range(1,n):
        for i in range(n-j):
            differenceTable[i][j] = differenceTable[i+1][j-1] - differenceTable[i][j-1]

    print("-----------------------------------------------")

    for row in differenceTable:
        for value in row:
            print(f"{value:.4f}", end="\t")
        print()

    x_1 = float(input("Enter the x value to calculate: "))

    print("-----------------------------------------------")

    # Check equal spacing
    h = x[1] - x[0]
    rangeSuitable = True
    for i in range(1,n-1):
        if abs ((x[i+1] - x[i]) - h) > 1e-9:
            rangeSuitable = False
            break

    if not rangeSuitable:
        print("The x values are not equally spaced.")
        return

    p = (x_1 - x[1]) / h

    T0 = (differenceTable[1][0] + differenceTable[2][0]) / 2
    T1 = (p - 0.5) * differenceTable[1][1]
    T2 = (p * (p - 1) / 2) * ((differenceTable[0][2]) + differenceTable[1][2]) / 2
    T3 = (p * (p - 1) * (p - 0.5) / 6) * differenceTable[0][3]

    result = T0 + T1 + T2 + T3
    print(f"Result: {result:.6f}")

    print("-----------------------------------------------")

bessel()


