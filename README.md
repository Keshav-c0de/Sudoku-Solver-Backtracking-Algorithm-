# Sudoku Solver & Game (Pygame)

A fully functional Sudoku game built with Python and Pygame. It features a manual play mode, an automated backtracking algorithm with live visualization, and a web scraper to fetch new puzzles.

## 🚀 Features
- **Live Solver:** Watch the backtracking algorithm solve any puzzle in real-time.
- **Manual Play:** Input numbers manually; the game highlights incorrect moves in red.
- **Web Scraping:** Automatically fetches fresh Sudoku puzzles from the web.
- **Timer:** Tracks your progress as you play.
- **Asset Management:** Built-in path handling for compatibility across macOS and Windows.

## Gameplay Screenshot
  <img width="400" height="600" alt="Screenshot 2026-01-11 at 4 11 06 AM" src="https://github.com/user-attachments/assets/f4e48bd6-003e-445d-8e81-904a8106d931" />

  <img width="400" height="600" alt="Screenshot 2026-01-11 at 4 14 46 AM" src="https://github.com/user-attachments/assets/b0925738-593b-48f5-afe7-afe4ea49a903" />



## 📂 Project Structure
* `interface.py` - The main entry point and Graphical User Interface (GUI).
* `suduko.py` - Contains the backtracking algorithm and board validation logic.
* `webscraping.py` - Handles fetching Sudoku data from external sources.
* `Assets/` - Folder containing UI icons (play, pause, reset, etc.).

## 🛠️ Installation

1. **Clone the repository:**
```
git clone [https://github.com/Keshav-c0de/Sudoku-Solver-Backtracking-Algorithm-.git](https://github.com/Keshav-c0de/Sudoku-Solver-Backtracking-Algorithm-.git)
cd Sudoku-Solver-Backtracking-Algorithm-
```
2. **Install Dependencies:**
```pip install pygame```

## 🎮 How to Play

  Run the game:
```python3 interface.py```

Controls:

 - Mouse Click: Select a cell.
 - Number Keys (1-9): Fill in a number
 - Backspace: Clear a cell.

Buttons:

  - 💡 Solve: Start the Auto-Solver.
  - 🔄 Reset: Clear the current board.
  - ➡️ Next: Fetch a new puzzle.

## 📦 Building the App (Mac)

To bundle this into a standalone .app file:
Bash

```pyinstaller --noconsole --onefile --name "Sudoku" --icon=sudoku.ico --add-data "Assets:Assets" interface.py```
