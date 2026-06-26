import matplotlib.pyplot as plt

Ku = [5, 10, 15, 20]
f_upper = [1.52, 0.79, 0.54, 0.41]

plt.figure(figsize=(8, 5))

plt.plot(
    Ku,
    f_upper,
    '-o',
    linewidth=2,
    markersize=8,
    color='red'
)

plt.xlabel("Коэффициент усиления $K_u$")
plt.ylabel("Верхняя граничная частота $f_{в}$ (МГц)")
plt.title("Зависимость верхней граничной частоты от коэффициента усиления")

plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig("_assets/img_10.png", dpi=200, bbox_inches="tight")
plt.show()