"""Code Art Gallery - Code in Place edition (paste into the online IDE)."""

from graphics import Canvas
import random

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

LINE_COLOR = 'black'
MONDRIAN_FILLS = ['white', 'white', 'white', 'white', 'red', 'yellow', 'blue']
KANDINSKY_PALETTE = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown']


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    paintings = [draw_mondrian, draw_random_mondrian, draw_rothko,
                 draw_kandinsky, draw_albers, draw_starry_night]
    print("Code Art Gallery")
    while True:
        print()
        print("Choose a painting:")
        print("  1 - Mondrian: Composition (1930)")
        print("  2 - Random Mondrian")
        print("  3 - Rothko: color field")
        print("  4 - Kandinsky: concentric circles")
        print("  5 - Albers: Homage to the Square")
        print("  6 - Van Gogh: The Starry Night")
        print("  7 - Surprise me")
        print("  q - Quit")
        choice = input("Your choice: ")
        if choice == 'q':
            print("Thanks for visiting the gallery!")
            break
        elif choice == '1':
            draw_mondrian(canvas)
            print("Showing: Piet Mondrian - Composition (1930)")
        elif choice == '2':
            draw_random_mondrian(canvas)
            print("Showing: a Mondrian generated at random")
        elif choice == '3':
            draw_rothko(canvas)
            print("Showing: Mark Rothko - color field")
        elif choice == '4':
            draw_kandinsky(canvas)
            print("Showing: Wassily Kandinsky - concentric circles")
        elif choice == '5':
            draw_albers(canvas)
            print("Showing: Josef Albers - Homage to the Square")
        elif choice == '6':
            draw_starry_night(canvas)
            print("Showing: Vincent van Gogh - The Starry Night (1889)")
        elif choice == '7':
            random.choice(paintings)(canvas)
            print("Showing a painting at random...")
        else:
            print("Invalid option, try again.")


def reset(canvas, background):
    try:
        canvas.clear()
    except Exception:
        pass
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, background)


def draw_mondrian(canvas):
    reset(canvas, 'white')
    canvas.create_rectangle(110, 0, CANVAS_WIDTH, 400, 'red')
    canvas.create_rectangle(0, 400, 110, CANVAS_HEIGHT, 'blue')
    canvas.create_rectangle(430, 400, CANVAS_WIDTH, CANVAS_HEIGHT, 'yellow')
    canvas.create_rectangle(105, 0, 115, CANVAS_HEIGHT, LINE_COLOR)
    canvas.create_rectangle(0, 395, CANVAS_WIDTH, 405, LINE_COLOR)
    canvas.create_rectangle(0, 295, 110, 305, LINE_COLOR)
    canvas.create_rectangle(425, 400, 435, CANVAS_HEIGHT, LINE_COLOR)


def draw_random_mondrian(canvas):
    reset(canvas, 'white')
    xs = [0, CANVAS_WIDTH]
    ys = [0, CANVAS_HEIGHT]
    for i in range(2):
        xs.append(random.randint(100, CANVAS_WIDTH - 100))
        ys.append(random.randint(100, CANVAS_HEIGHT - 100))
    xs.sort()
    ys.sort()
    for r in range(len(ys) - 1):
        for c in range(len(xs) - 1):
            canvas.create_rectangle(xs[c], ys[r], xs[c + 1], ys[r + 1], random.choice(MONDRIAN_FILLS))
    for x in xs:
        canvas.create_rectangle(x - 5, 0, x + 5, CANVAS_HEIGHT, LINE_COLOR)
    for y in ys:
        canvas.create_rectangle(0, y - 5, CANVAS_WIDTH, y + 5, LINE_COLOR)


def draw_rothko(canvas):
    reset(canvas, 'maroon')
    canvas.create_rectangle(45, 45, CANVAS_WIDTH - 45, 245, 'red')
    canvas.create_rectangle(60, 60, CANVAS_WIDTH - 60, 230, 'orange')
    canvas.create_rectangle(45, 285, CANVAS_WIDTH - 45, CANVAS_HEIGHT - 45, 'orange')
    canvas.create_rectangle(60, 300, CANVAS_WIDTH - 60, CANVAS_HEIGHT - 60, 'yellow')


def draw_kandinsky(canvas):
    reset(canvas, 'beige')
    cols = 3
    rows = 3
    cell_w = CANVAS_WIDTH / cols
    cell_h = CANVAS_HEIGHT / rows
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_w
            y1 = row * cell_h
            cx = x1 + cell_w / 2
            cy = y1 + cell_h / 2
            canvas.create_rectangle(x1 + 6, y1 + 6, x1 + cell_w - 6, y1 + cell_h - 6, random.choice(KANDINSKY_PALETTE))
            max_radius = min(cell_w, cell_h) / 2 - 12
            for k in range(3):
                radius = max_radius * (1 - k / 3)
                canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, random.choice(KANDINSKY_PALETTE))


def draw_albers(canvas):
    layers = ['yellow', 'orange', 'brown', 'black']
    reset(canvas, layers[0])
    step = CANVAS_WIDTH / (2 * len(layers))
    for i in range(1, len(layers)):
        m = step * i
        canvas.create_rectangle(m, m * 0.7, CANVAS_WIDTH - m, CANVAS_HEIGHT - m * 1.3, layers[i])


def draw_starry_night(canvas):
    reset(canvas, 'navy')
    canvas.create_oval(80, 80, 300, 300, 'royalblue')
    canvas.create_oval(150, 120, 270, 240, 'navy')
    canvas.create_oval(300, 60, 440, 200, 'royalblue')
    canvas.create_oval(335, 95, 405, 165, 'navy')
    canvas.create_oval(400, 50, 470, 120, 'gold')
    canvas.create_oval(410, 60, 460, 110, 'lightyellow')
    stars = [(70, 90), (250, 70), (470, 200), (150, 250), (300, 230), (430, 320)]
    for (x, y) in stars:
        canvas.create_oval(x - 11, y - 11, x + 11, y + 11, 'gold')
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, 'lightyellow')
    canvas.create_oval(-120, 440, 260, 620, 'black')
    canvas.create_oval(160, 450, 540, 620, 'black')
    for x in [190, 230, 270, 310]:
        canvas.create_rectangle(x, 440, x + 26, 470, 'navy')
        canvas.create_rectangle(x + 9, 448, x + 17, 462, 'gold')
    canvas.create_rectangle(300, 412, 316, 470, 'navy')
    canvas.create_oval(35, 250, 105, 500, 'darkgreen')
    canvas.create_oval(45, 170, 95, 380, 'darkgreen')
    canvas.create_oval(52, 110, 88, 260, 'darkgreen')


if __name__ == '__main__':
    main()