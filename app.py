import matplotlib.pyplot as plt
# verlet : x(t + delta t) = 2x(t) - x(t- delta t) + a(t) delta t^2

delta_t = 0.01
x0 = 2
v0 = 2
steps = 10**4


def a(x):
    k = 10
    m = 10
    return - k * x / m


def verlet_method(steps, delta_t, x0, v0):

    x1 = x0 + v0 * delta_t
    delta_t2 = delta_t * delta_t

    xt_old = x0
    xt = x1

    position = [x0, x1]
    velocity = [v0]
    time = [delta_t, 2*delta_t]

    for i in range(2, steps - 2):
        x_next = 2 * xt - xt_old + a(xt) * delta_t2
        vt = (x_next - xt_old) / (2 * delta_t)

        position.append(x_next)
        time.append(i * delta_t)
        velocity.append(vt)
        xt_old = xt
        xt = x_next

    vt = (x_next - xt_old) / (2 * delta_t)
    velocity.append(vt)

    return {"x": position, "t": time, "v": velocity}


verlet = verlet_method(steps, delta_t, x0, v0)

plt.plot(verlet["t"], verlet["x"])
plt.plot(verlet["t"], verlet["v"])
plt.show()
