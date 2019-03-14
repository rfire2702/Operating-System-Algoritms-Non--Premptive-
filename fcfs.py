# FCFS
# author = Siddhant Chandra Kulshrestha

def fcfs():
    l = []
    n = int(input('Enter number of processes:- '))
    print('Enter process no., arrival time and burst time')
    for i in range(n):
        x = list(map(int, input().split()))
        l.append(x)

    l.sort(key = lambda l: l[1])

    for i in range(n):
        y = 0
        for j in range(i + 1):
            if( j == 0 ):
                y += l[j][2] + l[j][1]
            else:
                y += l[j][2]
        l[i].append(y)

    for i in range(n):
        y = l[i][3] - l[i][1]
        l[i].append(y)
        z = l[i][4] - l[i][2]
        l[i].append(z)

    for i in range(n):
        if l[i][5] < 0:
            x = abs(l[i][5])
            for j in range(i, n):
                l[j][3] += x
                l[j][4] += x
                l[j][5] += x


    atat1 = 0
    awt1 = 0
    for i in range(n):
        atat1 += l[i][4]
        awt1 += l[i][5]
    atat = atat1 / n
    awt = awt1 / n

    process = []
    for i in range(n):
        if i == 0 and l[i][1] != 0:
            process.append(('idle',0,l[i][1]))
            process.append((l[i][0],l[i][1],l[i][3]))
        elif l[i][1] > l[i-1][3]:
            process.append(('idle',l[i-1][3],l[i][1]))
            process.append((l[i][0],l[i][1],l[i][3]))
        else:
            process.append((l[i][0],l[i][1],l[i][3]))

    s = "|"
    for i in range(len(process)):
        s += "  " + str(process[i][0]) + "  |" 
    s1 = "0"
    for i in range(len(process)):
        if process[i][0] == 'idle':
            s1 += "        " + str(process[i][2])
        else:
            s1 += "     " + str(process[i][2])     


    l.sort()

    print("\nGantt Chart:")

    for i in range(len(s)):
        print("-", end = '')
    print(end = '\n')
    print(s)
    for i in range(len(s)):
        print("-", end = '')
    print(end = '\n')
    print(s1)

    print("\nTable:\n")

    print('Process No.\tArrival Time\tBurst time\tCompletion Time\t\tTurn Around Time\tWaiting Time \t')
    for i in range(n):
        print(l[i][0] ,'\t\t', l[i][1] ,'\t\t',l[i][2] ,'\t\t', l[i][3],'\t\t\t', l[i][4] ,'\t\t\t',l[i][5])
    print('\nAverage Waiting Time =', awt)
    print('Average Turn Around Time =', atat)

fcfs()
