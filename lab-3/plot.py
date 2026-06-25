import matplotlib.pyplot as plt


def build_plot(x, y, title, xlabel, ylabel, png, color='blue'):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, '-o', color=color, markersize=8, label='Измерения')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=150, bbox_inches='tight')
    plt.show()


Ib_no_load = [0, 0.06, 0.28, 0.4, 0.5, 0.6]
Ic_no_load = [0, 14, 35, 50, 76, 99]

build_plot(
    Ib_no_load,
    Ic_no_load,
    "Характеристика прямой передачи",
    "Ток базы, $I_б$ (мА)",
    "Ток коллектора, $I_к$ (мА)",
    "_assets/bjt_transfer_no_load.png",
    color='blue'
)

Ib_load = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
Ic_load = [0, 12,  22,  36,  41,  42,  42,  42,  42,  42]

build_plot(
    Ib_load,
    Ic_load,
    "Характеристика прямой передачи с нагрузкой ($R_к = 150$ Ом)",
    "Ток базы, $I_б$ (мА)",
    "Ток коллектора, $I_к$ (мА)",
    "_assets/bjt_transfer_load.png",
    color='red'
)