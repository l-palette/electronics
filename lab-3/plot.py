import matplotlib.pyplot as plt


def build_plot(x, y, title, xlabel, ylabel, png, color='blue'):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'o', color=color, markersize=8, label='Измерения')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=150, bbox_inches='tight')
    plt.show()


Ib_no_load = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
Ic_no_load = [12, 23, 40, 54, 70, 84]

build_plot(
    Ib_no_load,
    Ic_no_load,
    "Характеристика прямой передачи без нагрузки",
    "Ток базы, $I_B$ (мА)",
    "Ток коллектора, $I_C$ (мА)",
    "_assets/bjt_transfer_no_load.png",
    color='blue'
)

Ib_load = [0, 0.02, 0.04, 0.08, 0.10, 0.14, 0.18, 0.20, 0.40, 0.60]
Ic_load = [0, 2, 4, 8, 10, 16, 20, 20, 20, 20]

build_plot(
    Ib_load,
    Ic_load,
    "Характеристика прямой передачи при наличии нагрузки",
    "Ток базы, $I_B$ (мА)",
    "Ток коллектора, $I_C$ (мА)",
    "_assets/bjt_transfer_load.png",
    color='red'
)