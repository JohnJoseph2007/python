import tkinter as tk
import math
import random

W, H = 700, 700
MESSAGE = "for you, i would"

root = tk.Tk()
root.title("Fireworks")
canvas = tk.Canvas(root, width=W, height=H, bg="black", highlightthickness=0)
canvas.pack()

rockets = []
sparks = []

PINKS = [
    (255, 200, 221),  # blush
    (255, 160, 200),  # soft pink
    (255, 105, 180),  # hot pink
    (255, 70, 150),   # vivid
    (230, 40, 120),   # raspberry
    (200, 20, 100),   # deep rose
]


def rgb(r, g, b):
    r = max(0, min(255, int(r)))
    g = max(0, min(255, int(g)))
    b = max(0, min(255, int(b)))
    return "#%02x%02x%02x" % (r, g, b)


def launch(x=None, burst_y=None):
    rockets.append({
        "x": x if x is not None else random.randint(150, W - 150),
        "y": H,
        "vy": -random.uniform(7, 10),
        "burst_y": burst_y if burst_y is not None else random.randint(150, 350),
    })


def explode(cx, cy):
    base = random.choice(PINKS)
    n = 90
    for i in range(n):
        a = i / n * 2 * math.pi
        hx = 16 * math.sin(a) ** 3
        hy = (13 * math.cos(a) - 5 * math.cos(2 * a)
              - 2 * math.cos(3 * a) - math.cos(4 * a))
        speed = random.uniform(0.9, 1.1) * 0.22
        sparks.append({
            "x": cx, "y": cy,
            "vx": hx * speed,
            "vy": -hy * speed,  # minus: screen y points down
            "life": 1.0,
            "color": random.choice([base, random.choice(PINKS)]),
        })


def frame():
    canvas.delete("all")

    # occasionally launch a new rocket
    if random.random() < 0.03:
        launch()

    # rockets
    alive_rockets = []
    for rk in rockets:
        rk["y"] += rk["vy"]
        if rk["y"] <= rk["burst_y"]:
            explode(rk["x"], rk["y"])
        else:
            canvas.create_oval(rk["x"] - 2, rk["y"] - 2,
                               rk["x"] + 2, rk["y"] + 2,
                               fill="#ffd0e6", outline="")
            alive_rockets.append(rk)
    rockets[:] = alive_rockets

    # sparks
    alive_sparks = []
    for sp in sparks:
        sp["vx"] *= 0.985
        sp["vy"] = sp["vy"] * 0.985 + 0.04  # drag + gravity
        sp["x"] += sp["vx"]
        sp["y"] += sp["vy"]
        sp["life"] -= 0.012

        if sp["life"] <= 0:
            continue

        cr, cg, cb = sp["color"]
        life = sp["life"]
        colour = rgb(cr * life, cg * life, cb * life)
        if random.random() < 0.03:
            colour = "#ffffff"  # sparkle

        canvas.create_oval(sp["x"] - 2, sp["y"] - 2,
                           sp["x"] + 2, sp["y"] + 2,
                           fill=colour, outline="")
        alive_sparks.append(sp)
    sparks[:] = alive_sparks

    if MESSAGE:
        canvas.create_text(W // 2, H - 50, text=MESSAGE,
                           fill="#ff9ccc", font=("Helvetica", 28, "bold"))

    root.after(16, frame)


def finale(event=None):
    for _ in range(5):
        launch()


def click_burst(event):
    launch(x=event.x, burst_y=event.y)


root.bind("<space>", finale)
canvas.bind("<Button-1>", click_burst)

frame()
root.mainloop()