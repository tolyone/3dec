import matplotlib.pyplot as plt

f = open('file.txt', 'r')

L = []
x = []
y = []
legend = []

for e in f:
    L.append(e)


for e in L:
    if e.__len__() > 5:
        e = e.split()
        # print('e = ', e)
        # print('e[0] = ', e[0])
        # print('e[1] = ', e[1])
        x.append(float(e[0]))
        y.append(float(e[1]))
    elif 3 < e.__len__() < 6:
        e = e.split()
        if e.__len__() == 1:
            legend.append(e[0])
            # x.append(e[0] + '\t')
            # y.append(e[0] + '\t')

#8985

for e in range(0,8985,500):
    plt.plot(x[e:e+499], y[e:e+499])

# plt.plot(x[:500], y[:500])
plt.xlabel('MeV')
# plt.xscale('log')
plt.yscale('log')
plt.show()
