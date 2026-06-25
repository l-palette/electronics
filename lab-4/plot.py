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


def build_semilogx_plot(x, y, title, xlabel, ylabel, png, color='blue'):
    plt.figure(figsize=(8, 5))
    plt.semilogx(x, y, 'o', color=color, markersize=8, label='Измерения')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=150, bbox_inches='tight')
    plt.show()


Uin_pos = [0, 1, 2, 3, 4, 4.5, 5, 5.8, 9, 12]
Uout_pos = [0, -2, -4.2, -6.2, -8.3, -9.4, -10.2, -11.2, -11.2, -11.2]

Uin_neg = [0, -1, -2, -3, -4, -4.5, -5, -5.8, -9, -12]
Uout_neg = [0, 2, 4.1, 6.1, 8.2, 9.2, 10.4, 10.9, 10.9, 10.9]

Uin_inv = Uin_neg[::-1] + Uin_pos[1:]
Uout_inv = Uout_neg[::-1] + Uout_pos[1:]

build_plot(
    Uin_inv,
    Uout_inv,
    "АХ инвертирующего усилителя",
    "Входное напряжение, $U_{вх}$ (В)",
    "Выходное напряжение, $U_{вых}$ (В)",
    "_assets/opamp_inv_ax.png",
    color='blue'
)

f_inv = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
Uout_inv_freq = [18.4, 19.1, 19.5, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.7, 18.3, 11.4]

Uin_inv_freq = 9.8
Ku_inv_freq = [u / Uin_inv_freq for u in Uout_inv_freq]

build_semilogx_plot(
    f_inv,
    Ku_inv_freq,
    "АЧХ инвертирующего усилителя",
    "Частота, $f$ (Гц)",
    "Коэффициент усиления, $|K_u|$",
    "_assets/opamp_inv_freq.png",
    color='green'
)

Uin_pos_noninv = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 7, 12]
Uout_pos_noninv = [0, 1.6, 3.2, 4.8, 6.2, 7.7, 9.3, 10.8, 10.8, 10.8]

Uin_neg_noninv = [0, -0.5, -1, -1.5, -2, -2.5, -3, -3.5, -7, -12]
Uout_neg_noninv = [0, -1.5, -3, -4.6, -6, -7.5, -9, -11, -11, -11]

Uin_noninv = Uin_neg_noninv[::-1] + Uin_pos_noninv[1:]
Uout_noninv = Uout_neg_noninv[::-1] + Uout_pos_noninv[1:]

build_plot(
    Uin_noninv,
    Uout_noninv,
    "АХ неинвертирующего усилителя",
    "Входное напряжение, $U_{вх}$ (В)",
    "Выходное напряжение, $U_{вых}$ (В)",
    "_assets/opamp_noninv_ax.png",
    color='purple'
)

f_noninv = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
Uout_noninv_freq = [18.3, 18.8, 19.1, 19.2, 19.2, 19.2, 19.2, 19.6, 19.2, 19.2, 18.0, 17.0, 10.0]

Uin_noninv_freq = 6.4
Ku_noninv_freq = [u / Uin_noninv_freq for u in Uout_noninv_freq]

build_semilogx_plot(
    f_noninv,
    Ku_noninv_freq,
    "АЧХ неинвертирующего усилителя",
    "Частота, $f$ (Гц)",
    "Коэффициент усиления, $K_u$",
    "_assets/opamp_noninv_freq.png",
    color='orange'
)
