# Game-of-Life Editor ★ Processing.py

**Interactive Conway’s Game of Life playground** powered by **Processing 3 (Python mode)** and **ControlP5**.  
Paint patterns, zoom, rotate, mirror, time-travel through generations and export your creations—all in one window.

[![YouTube demo](https://img.youtube.com/vi/4Upv88OFJC8/0.jpg)](https://youtu.be/4Upv88OFJC8)

---

## ✨ Key Features

| Category | Highlights |
|----------|------------|
| **Editor** | • Drag-&-drop pattern placement<br>• Live overlay showing pattern footprint & grid coordinates<br>• Middle-click to mark the geometric centre of any figure |
| **Transforms** | • **Rotate ± 90°** & **mirror X / Y** a pattern before stamping<br>• Unlimited undo/redo across the timeline (← / → or buttons) |
| **Simulation** | • Play / pause toggle and single-step (<<< / >>>)<br>• Two evolution engines — **`actualize`** (straightforward) & **`actualize_bis`** (neighbour cache) — switchable for speed tests |
| **Zoom & Pan** | • Smooth zoom in/out in fixed steps (`+`, `-`) with automatic padding<br>• Visual zoom indicator |
| **Analytics** | • Live counter of living cells<br>• **Get Figure** button converts any selection into relative coordinates printed to console |
| **Export** | • One-click export to **`export.txt`** (Python list literal) for reuse or unit tests |
| **Pattern Library** | 60 + classic and exotic patterns defined in **`data.py`**—automatically rendered as palette buttons |

---

## 📦 Installation

| Requirement          | Recommended version |
|----------------------|---------------------|
| **Processing 3.x**   | ≥ 3.5.4 |
| **Python Mode**      | install via *Contribution Manager* |
| **ControlP5**        | install via *Libraries* tab |
| **Java**             | JDK 8 or 11 |

```bash
# 1. Clone the repo
git clone https://github.com/Skyxo/Jeu-de-la-Vie-Processing.py.git
cd Jeu-de-la-Vie-Processing.py

# 2. Open Processing, switch to Python mode
# 3. Load  jeu_de_la_vie.pyde  and press ▶ Run
````

### CLI / Headless option

```bash
pip install processing-py      # cross-platform Processing CLI
processing-py run jeu_de_la_vie.pyde
```

---

## 🎮 Controls Reference

| Action                     | Button            | Hotkey                   |
| -------------------------- | ----------------- | ------------------------ |
| Play / Pause               | **Start/Stop**    | *Space*                  |
| Next / Previous generation | **>>> / <<<**     | → / ←                    |
| Zoom in / out              | **+ / -**         | + / -                    |
| Rotate pattern             | **+90 / -90**     | —                        |
| Mirror pattern             | **Sym X / Sym Y** | —                        |
| Place / erase cells        | —                 | L-click / R-click & drag |
| Mark figure centre         | —                 | Middle-click             |
| Cell count (console)       | **Cellules**      | C                        |
| Export grid                | **Export**        | E                        |
| Dump pattern coordinates   | **Get Figure**    | G                        |

---

## 🚀 Quick Start Walk-through

1. **Pick a pattern** from the right-hand palette.
2. **Draw**: left-drag stamps the pattern; right-drag erases cells.
3. Hit **Start** to animate; use **>>>** to fast-forward or arrow keys to time travel.
4. Press **Export** when you’re happy—`export.txt` appears next to the sketch.

---

## 🏗 Project Structure

```
├── jeu_de_la_vie.pyde   # GUI, event loop & ControlP5 hooks
├── jdlv.py              # Core algorithms, maths helpers & IO
├── data.py              # Pre-defined pattern coordinates
├── export.txt           # Auto-generated export file
└── sketch.properties    # Processing metadata (Python mode)
```

---

## ⚙️ Algorithm Notes

* `actualize()` implements a naive neighbour scan—easy to read, slower on large grids.
* `actualize_bis()` pre-checks inner cells via `getNeighbors()` and skips borders, yielding \~2× speed-up on ≥ 200×200 grids.
* Switch engine by replacing the call in **`Next()`** (line ≈ 150) if you wish to benchmark.

---

## 🛣 Roadmap

* [ ] Box selection & copy-paste
* [ ] JSON save / load of entire projects
* [ ] Multi-state cells (color & rules editor)
* [ ] GPU shader pipeline for ultra-large boards
* [ ] Automated unit tests (PyTest) & CI badge

---

## 🤝 Contributing

1. **Fork** ➜ `git checkout -b feat/your-feature`
2. Run linters / tests (`black`, `pytest` soon)
3. Open a descriptive **Pull Request**—screenshots welcome!

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for full text.

---

## 🙏 Acknowledgements

* [ControlP5](http://www.sojamo.de/libraries/controlP5/) for the slick GUI toolkit
* The Processing & Python-mode communities
* Conway, for the timeless game that started it all
