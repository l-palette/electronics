import matplotlib.pyplot as plt


def build_plot(x, y, title, xlabel, ylabel, png, color='blue', label='Измерения'):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'o-', color=color, linewidth=2, markersize=8, label=label)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=150, bbox_inches='tight')
    plt.show()


E_avg = 10.25
Rb = 150
Ust_nom = 6.8

U_load = [0, E_avg]
I_load = [E_avg / Rb * 1000, 0]

U_work = Ust_nom
I_work = (E_avg - Ust_nom) / Rb * 1000

plt.figure(figsize=(8, 5))

plt.plot(
    U_load,
    I_load,
    'o-',
    color='blue',
    linewidth=2,
    markersize=8,
    label='Линия нагрузки'
)

plt.plot(
    U_work,
    I_work,
    'ro',
    markersize=9,
    label='Рабочая точка'
)

plt.xlabel('Напряжение на стабилитроне, $U_{ст}$ (В)', fontsize=12)
plt.ylabel('Ток через балластный резистор, $I_{б}$ (мА)', fontsize=12)
plt.title('Линия нагрузки параметрического стабилизатора', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('_assets/load_line_stabilizer.png', dpi=150, bbox_inches='tight')
plt.show()


E_no_load = [0, 3.12, 5.86, 7.13, 7.45, 7.78, 8.09, 9.07, 10.10, 10.90, 11.90]
Ust_no_load = [0, 3.22, 6.08, 7.20, 7.22, 7.24, 7.26, 7.30, 7.35, 7.40, 7.44]
Ib_no_load = [0, 0, 0, 2, 4, 6, 8, 14, 20, 24, 30]

build_plot(
    E_no_load,
    Ust_no_load,
    "Зависимость $U_{ст}=f(E)$ без нагрузки",
    "Напряжение питания, $E$ (В)",
    "Выходное напряжение, $U_{ст}$ (В)",
    "_assets/stabilizer_no_load_voltage.png",
    color='green',
    label='$U_{ст}=f(E)$'
)

build_plot(
    E_no_load,
    Ib_no_load,
    "Зависимость $I_{б}=f(E)$ без нагрузки",
    "Напряжение питания, $E$ (В)",
    "Ток через балластный резистор, $I_{б}$ (мА)",
    "_assets/stabilizer_no_load_current.png",
    color='purple',
    label='$I_{б}=f(E)$'
)


E_load = [10.00, 8.63, 7.95, 6.88, 6.00, 4.96, 4.44, 4.00, 3.64, 3.03, 2.32, 1.78, 1.51, 0.84]
Un_load = [7.19, 6.25, 5.76, 4.99, 4.35, 3.60, 3.21, 2.89, 2.63, 2.19, 1.68, 1.28, 1.10, 0.61]

E_load_sorted, Un_load_sorted = zip(*sorted(zip(E_load, Un_load)))

build_plot(
    E_load_sorted,
    Un_load_sorted,
    "Зависимость $U_{н}=f(E)$ при наличии нагрузки",
    "Напряжение питания, $E$ (В)",
    "Выходное напряжение, $U_{н}$ (В)",
    "_assets/stabilizer_load_voltage.png",
    color='red',
    label='$U_{н}=f(E)$'
)


plt.figure(figsize=(8, 5))

plt.plot(
    E_no_load,
    Ust_no_load,
    'o-',
    color='green',
    linewidth=2,
    markersize=8,
    label='Без нагрузки'
)

plt.plot(
    E_load_sorted,
    Un_load_sorted,
    'o-',
    color='red',
    linewidth=2,
    markersize=8,
    label='С нагрузкой'
)

plt.xlabel('Напряжение питания, $E$ (В)', fontsize=12)
plt.ylabel('Выходное напряжение, $U$ (В)', fontsize=12)
plt.title('Сравнение зависимостей $U=f(E)$ без нагрузки и с нагрузкой', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('_assets/stabilizer_compare_voltage.png', dpi=150, bbox_inches='tight')
plt.show()

