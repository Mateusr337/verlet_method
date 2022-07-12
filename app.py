import matplotlib.pyplot as plt
import numpy as np
# verlet : x(t + delta t) = 2x(t) - x(t- delta t) + a(t) delta t^2

delta_t = 0.01
x0 = 2
v0 = 2
t_max = 100


k = 10
m = 10


def a(x):
    return - k * x / m


def verlet_method(t_max, delta_t, x0, v0):

    delta_t2 = delta_t * delta_t
    x1 = x0 + v0 * delta_t + 0.5 * a(x0) * delta_t2

    xt_old = x0
    xt = x1

    position = [x0]
    velocity = [v0]
    time = [0]

    for t in np.arange(delta_t, 20, delta_t):
        x_next = 2 * xt - xt_old + a(xt) * delta_t2
        vt = (x_next - xt_old) / (2 * delta_t)

        position.append(xt)
        time.append(t)
        velocity.append(vt)
        xt_old = xt
        xt = x_next

    return {"x": position, "t": time, "v": velocity}


def Energy(v, x):
    energy = []

    for i in range(len(v)):
        Et = (0.5 * k * (x[i] ** 2)) + (0.5 * m * (v[i] ** 2))
        energy.append(Et)

    return energy


verlet = verlet_method(t_max, delta_t, x0, v0)
energy = Energy(verlet["v"], verlet["x"])

plt.plot(verlet["t"], verlet["x"])
plt.plot(verlet["t"], verlet["v"])
plt.plot(verlet["t"], energy)
plt.show()
