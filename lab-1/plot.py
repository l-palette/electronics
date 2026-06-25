import matplotlib.pyplot as plt

def build_plot(x, y, title, xlabel, ylabel, png, color='blue'):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'o-', color=color, linewidth=2, markersize=8, label='Измерения')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=150, bbox_inches='tight')
    plt.show()

Ua_vd1_f = [0, 0.68, 0.70, 0.74, 0.76, 0.77, 0.78, 0.79, 0.80]
Ia_vd1_f = [0, 10.0, 12.0, 26.0, 40.0, 52.0, 62.0, 80.0, 94.0]
build_plot(Ua_vd1_f, Ia_vd1_f,
           "ВАХ выпрямительного диода (VD1) – прямая ветвь",
           "Анодное напряжение, $U_a$ (В)",
           "Анодный ток, $I_a$ (мА)",
           "_assets/vac_1.png")

Ua_vd2 = [0, 0.25, 0.27, 0.29, 0.30, 0.31, 0.32, 0.33, 0.34]
Ia_vd2 = [0, 8.0, 14.0, 24.0, 32.0, 50.0, 60.0, 80.0, 100.0]
build_plot(Ua_vd2, Ia_vd2,
           "ВАХ диода Шоттки (VD2) – прямая ветвь",
           "Анодное напряжение, $U_a$ (В)",
           "Анодный ток, $I_a$ (мА)",
           "_assets/vac_2.png")

Ua_vd3 = [0, 1.97, 2.04, 2.13, 2.17, 2.89]
Ia_vd3 = [0, 4.0, 10.0, 16.0, 20.0, 50.0]
build_plot(Ua_vd3, Ia_vd3,
           "ВАХ светодиода (VD3) – прямая ветвь",
           "Анодное напряжение, $U_a$ (В)",
           "Анодный ток, $I_a$ (мА)",
           "_assets/vac_3.png")

Ua_vd4_f = [0, 0.74, 0.80, 0.82, 0.84, 0.85, 0.86, 0.87]
Ia_vd4_f = [0, 2.0, 10.0, 16.0, 20.0, 36.0, 46.0, 50.0]
build_plot(Ua_vd4_f, Ia_vd4_f,
           "ВАХ стабилитрона (VD4) – прямая ветвь",
           "Анодное напряжение, $U_a$ (В)",
           "Анодный ток, $I_a$ (мА)",
           "_assets/vac_4.png")

Ua_vd1_r = [0, -0.1, -0.2, -0.3, -0.4, ]
Ia_vd1_r = [0, -2.8, -5.9, -9.13, -11.6]
build_plot(Ua_vd1_r, Ia_vd1_r,
           "ВАХ выпрямительного диода (VD1) – обратная ветвь",
           "Анодное напряжение (обратное), $U_a$ (В)",
           "Анодный ток (обратный), $I_a$ (мА)",
           "_assets/vac_1_reverse.png",
           color='red')

Ua_vd4_r = [0, -0.10, -0.90, -6.00, -7.16, -7.25]
Ia_vd4_r = [0, -2.90, -6.99, -7.09, -10.00, -20.00]
build_plot(Ua_vd4_r, Ia_vd4_r,
           "ВАХ стабилитрона (VD4) – обратная ветвь",
           "Анодное напряжение (обратное), $U_a$ (В)",
           "Анодный ток (обратный), $I_a$ (мА)",
           "_assets/vac_4_reverse.png",
           color='red')