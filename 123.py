import matplotlib.pyplot as plt

f = open('file.txt', 'r')

x = []
y = []
legend = []
L = []

for e in f:
    if e.split().__len__() == 2:
        e = e.split()
        x.append(float(e[0]))
        y.append(float(e[1]))
    elif e.split().__len__() == 1:
        e = e.split()
        legend.append(e[0])

# print(legend)
# for e in range(0,9000,500):
#     plt.step(x[e:e+500], y[e:e+500], label=str(legend[int(e/500)]))

for e in range(0,9000,10):
    y[e] = sum(y[e:e+10])
    plt.step(x[e:e+10], y[e:e+10])

plt.xlabel('MeV')
plt.ylabel('Count')
plt.yscale('log')
plt.title('grafik')
# plt.legend(loc='upper left')
plt.grid()
plt.show()

# Изменить диапазон - 10 точек
#Добавить погрешности - корень из величины (график - точки + погрешности, без линий)
