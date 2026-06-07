"""Code Art Gallery - desktop version (tkinter). Run: python art_gallery.py"""

import random
import tkinter as tk

CANVAS_SIZE = 600
LINE_COLOR = "#1a1a1a"
MONDRIAN_FILLS = ["#FAFAF5", "#FAFAF5", "#FAFAF5", "#FAFAF5", "#D40920", "#1356A2", "#F7D117"]
KANDINSKY_PALETTE = ["#C0392B", "#E67E22", "#F1C40F", "#27AE60", "#2980B9",
                     "#8E44AD", "#16A085", "#D35400", "#2C3E50", "#C0A062"]


def reset(canvas, background="white"):
    canvas.delete("all")
    canvas.configure(background=background)


def blend(hex_a, hex_b, t):
    a = [int(hex_a[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(hex_b[i:i + 2], 16) for i in (1, 3, 5)]
    mixed = [round(ca + (cb - ca) * t) for ca, cb in zip(a, b)]
    return "#%02x%02x%02x" % tuple(mixed)


def soft_block(canvas, x1, y1, x2, y2, color, background):
    for i in range(8, 0, -1):
        glow = blend(color, background, i / 8)
        canvas.create_rectangle(x1 - i * 2, y1 - i * 2, x2 + i * 2, y2 + i * 2, fill="", outline=glow, width=4)
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


def draw_mondrian(canvas):
    reset(canvas, "#FAFAF5")
    canvas.create_rectangle(96, 0, CANVAS_SIZE, 480, fill="#D40920", outline="")
    canvas.create_rectangle(0, 480, 96, CANVAS_SIZE, fill="#1356A2", outline="")
    canvas.create_rectangle(510, 480, CANVAS_SIZE, CANVAS_SIZE, fill="#F7D117", outline="")
    w = 12
    canvas.create_line(96, 0, 96, CANVAS_SIZE, fill=LINE_COLOR, width=w)
    canvas.create_line(0, 480, CANVAS_SIZE, 480, fill=LINE_COLOR, width=w)
    canvas.create_line(0, 384, 96, 384, fill=LINE_COLOR, width=w)
    canvas.create_line(510, 480, 510, CANVAS_SIZE, fill=LINE_COLOR, width=w)
    canvas.create_rectangle(0, 0, CANVAS_SIZE, CANVAS_SIZE, outline=LINE_COLOR, width=w)


def draw_random_mondrian(canvas):
    reset(canvas, "#FAFAF5")
    xs = sorted([0, CANVAS_SIZE] + [random.randint(90, CANVAS_SIZE - 90) for _ in range(3)])
    ys = sorted([0, CANVAS_SIZE] + [random.randint(90, CANVAS_SIZE - 90) for _ in range(3)])
    for r in range(len(ys) - 1):
        for c in range(len(xs) - 1):
            canvas.create_rectangle(xs[c], ys[r], xs[c + 1], ys[r + 1], fill=random.choice(MONDRIAN_FILLS), outline="")
    w = 10
    for x in xs:
        canvas.create_line(x, 0, x, CANVAS_SIZE, fill=LINE_COLOR, width=w)
    for y in ys:
        canvas.create_line(0, y, CANVAS_SIZE, y, fill=LINE_COLOR, width=w)


def draw_rothko(canvas):
    ground = "#9E2B25"
    reset(canvas, ground)
    soft_block(canvas, 60, 60, CANVAS_SIZE - 60, 290, "#E8743B", ground)
    soft_block(canvas, 60, 330, CANVAS_SIZE - 60, CANVAS_SIZE - 60, "#F2C14E", ground)


def draw_kandinsky(canvas):
    reset(canvas, "#EDE6D6")
    cols, rows = 4, 3
    cell_w = CANVAS_SIZE / cols
    cell_h = CANVAS_SIZE / rows
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_w
            y1 = row * cell_h
            center_x = x1 + cell_w / 2
            center_y = y1 + cell_h / 2
            canvas.create_rectangle(x1 + 6, y1 + 6, x1 + cell_w - 6, y1 + cell_h - 6, fill=random.choice(KANDINSKY_PALETTE), outline="")
            n_circles = random.randint(4, 6)
            max_radius = min(cell_w, cell_h) / 2 - 14
            for k in range(n_circles):
                radius = max_radius * (1 - k / n_circles)
                canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill=random.choice(KANDINSKY_PALETTE), outline="")


def draw_albers(canvas):
    layers = ["#E4C441", "#D89B2A", "#B5651D", "#7A3E12"]
    reset(canvas, layers[0])
    step = CANVAS_SIZE / (2 * len(layers))
    for i in range(1, len(layers)):
        margin = step * i
        canvas.create_rectangle(margin, margin * 0.7, CANVAS_SIZE - margin, CANVAS_SIZE - margin * 1.3, fill=layers[i], outline="")


def draw_starry_night(canvas):
    reset(canvas, "#0B1A3A")
    canvas.create_oval(90, 90, 330, 330, fill="#2E5894", outline="")
    canvas.create_oval(170, 150, 290, 270, fill="#0B1A3A", outline="")
    canvas.create_oval(340, 70, 500, 230, fill="#2E5894", outline="")
    canvas.create_oval(380, 110, 460, 190, fill="#0B1A3A", outline="")
    canvas.create_oval(470, 60, 560, 150, fill="#F4D03F", outline="")
    canvas.create_oval(484, 74, 546, 136, fill="#FCF3CF", outline="")
    stars = [(80, 110), (300, 80), (540, 240), (170, 300), (360, 260), (510, 390), (130, 200)]
    for (x, y) in stars:
        canvas.create_oval(x - 14, y - 14, x + 14, y + 14, fill="#F4D03F", outline="")
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="#FCF3CF", outline="")
    canvas.create_oval(-150, 470, 320, 700, fill="#000000", outline="")
    canvas.create_oval(200, 480, 760, 700, fill="#000000", outline="")
    for x in range(220, 440, 46):
        canvas.create_rectangle(x, 470, x + 30, 508, fill="#10204A", outline="")
        canvas.create_rectangle(x + 10, 480, x + 22, 498, fill="#F4D03F", outline="")
    canvas.create_rectangle(370, 432, 392, 508, fill="#10204A", outline="")
    canvas.create_oval(40, 280, 120, 600, fill="#08231A", outline="")
    canvas.create_oval(54, 190, 106, 430, fill="#08231A", outline="")
    canvas.create_oval(64, 120, 96, 300, fill="#08231A", outline="")


def main():
    root = tk.Tk()
    root.title("Code Art Gallery")
    root.configure(padx=14, pady=14)
    title_var = tk.StringVar(value="Pick a painting below")
    tk.Label(root, textvariable=title_var, font=("Helvetica", 14, "italic")).pack(pady=(0, 8))
    canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, background="white", highlightthickness=0)
    canvas.pack()
    paintings = [
        ("Mondrian", draw_mondrian, "Piet Mondrian - Composition II (1930)"),
        ("Random Mondrian", draw_random_mondrian, "Mondrian - generated at random"),
        ("Rothko", draw_rothko, "Mark Rothko - color field"),
        ("Kandinsky", draw_kandinsky, "Wassily Kandinsky - Concentric Circles (1913)"),
        ("Albers", draw_albers, "Josef Albers - Homage to the Square"),
        ("Starry Night", draw_starry_night, "Vincent van Gogh - The Starry Night (1889)"),
    ]

    def show(draw_function, title):
        draw_function(canvas)
        title_var.set(title)

    def show_random():
        _, draw_function, title = random.choice(paintings)
        show(draw_function, title)

    bar = tk.Frame(root, pady=12)
    bar.pack()
    for label, draw_function, title in paintings:
        tk.Button(bar, text=label, width=14, pady=4, command=lambda f=draw_function, t=title: show(f, t)).pack(side="left", padx=2)
    tk.Button(bar, text="Surprise me", width=14, pady=4, command=show_random).pack(side="left", padx=2)
    show(draw_starry_night, paintings[5][2])
    root.mainloop()


if __name__ == "__main__":
    main()