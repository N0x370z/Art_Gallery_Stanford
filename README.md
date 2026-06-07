# Code Art Gallery

An interactive desktop app that recreates famous paintings using nothing but
geometric shapes drawn with Python's built-in `tkinter` library.

Built as my final project for **Stanford Code in Place**.

**Author:** Ivan Luna — [github.com/N0x370z](https://github.com/N0x370z)

## Paintings

| Button | Inspiration |
| --- | --- |
| Mondrian | Piet Mondrian, *Composition II in Red, Blue and Yellow* (1930) |
| Random Mondrian | A new Mondrian-style grid generated at random on every click |
| Rothko | Mark Rothko, color-field style with soft, glowing blocks |
| Kandinsky | Wassily Kandinsky, *Color Study: Squares with Concentric Circles* (1913) |
| Albers | Josef Albers, *Homage to the Square* style |
| Starry Night | Vincent van Gogh, *The Starry Night* (1889) |
| Surprise me | Picks one of the paintings at random |

## Two versions

This repo contains the same project written for two different environments,
because they support different graphics libraries:

| File | Where it runs | Library |
| --- | --- | --- |
| `art_gallery.py` | On your computer (desktop) | `tkinter` (built into Python) |
| `art_gallery_codeinplace.py` | The Code in Place online IDE (browser) | the course's `graphics` library |

The desktop version uses clickable buttons and is the main one. The Code in
Place version uses a console menu, since the browser IDE can't run `tkinter`.

## How to run (desktop version)

```bash
python art_gallery.py
```

Requires **Python 3**. `tkinter` is included with most standard Python
installations. On some Linux distributions you may need to install it first:

```bash
sudo apt install python3-tk
```

To run the Code in Place version, paste `art_gallery_codeinplace.py` into the
Code in Place online IDE and press Run.

## How it works

Each painting is a function that receives the canvas and draws the artwork
from rectangles, lines and ovals:

- **Mondrian** places colored blocks and thick black grid lines by hand.
- **Random Mondrian** picks random grid lines, then fills each cell with a
  random color (weighted toward white, like the real compositions).
- **Rothko** stacks color blocks and fakes the soft, glowing edges by layering
  faint outlines that fade toward the background color.
- **Kandinsky** loops over a 4x3 grid and draws several concentric circles in
  each cell, over a colored square background.
- **Albers** draws nested squares, shifted upward so the bottom band is wider.
- **Starry Night** builds a night scene from ovals (swirling sky, moon, glowing
  stars, a cypress tree) and small rectangles (the village).

A row of buttons at the bottom redraws the canvas instantly. The canvas is
fully cleared before each painting, so nothing slows down over time.

## Concepts used

Functions and parameters, lists, loops (including nested loops), the `random`
library, simple color math, and event-driven GUI programming with `tkinter`.

## Possible next steps

- Add more painters (Malevich, Klee, Hokusai's *Great Wave*).
- Let the user save the current canvas as an image.
- Add sliders to control the number of cells or the palette.
