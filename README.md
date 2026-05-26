# 🔍 A* Pathfinding Visualizer | Python Maze Solver

## 📌 Overview

This project is a visual implementation of the **A* (A-Star) Pathfinding Algorithm** using Python and the `pyamaze` library.  
The program generates a maze and intelligently finds the shortest path from the start position to the goal using heuristic-based search.

### 🎯 The visualization shows:
- ✅ Complete search traversal
- ✅ Explored nodes
- ✅ Final shortest path
- ✅ Real-time moving agents with footprints

---

# 🚀 Features

- 🔹 A* shortest pathfinding algorithm
- 🔹 Dynamic maze generation
- 🔹 Animated path traversal
- 🔹 Multiple agents visualization
- 🔹 Manhattan Distance heuristic
- 🔹 Dark theme maze UI
- 🔹 Search path vs shortest path comparison

---

# 🛠 Tech Stack

- Python
- Priority Queue
- pyamaze
- A* Algorithm

---

# 📂 Project Structure

```bash
MazeSolving/
│
├── astar.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mahikaverse/internship_task1.git
```

## 2️⃣ Move into Project Folder

```bash
cd maze-solver-astar
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install pyamaze
```

---

# ▶️ Run Project

```bash
python astar.py
```

---

# 🧠 How A* Works

The A* algorithm combines:

- **g(n)** → Actual distance from start node
- **h(n)** → Heuristic estimated distance to goal

## 📌 Formula

```text
f(n) = g(n) + h(n)
```

## 📌 Manhattan Distance Heuristic

```text
h(x, y) = |x1 - x2| + |y1 - y2|
```

The algorithm always chooses the node with the lowest estimated total cost.

---

# 🎨 Visualization

## 🤖 Agents Used

| Agent Color | Purpose |
|-------------|----------|
| 🔴 Red | Search Traversal |
| 🔵 Blue | Reverse / Backtracking Path |
| 🟢 Green | Final Shortest Path |

---

# 📸 Output

The maze window displays:

- ✅ Generated maze
- ✅ Animated agents
- ✅ Path footprints
- ✅ Path length statistics

---

# 📚 Concepts Learned

- Pathfinding Algorithms
- Graph Traversal
- Heuristic Search
- Priority Queue
- AI Search Techniques
- Maze Solving Logic

---

# 🔥 Future Improvements

- Dijkstra Algorithm support
- BFS / DFS comparison
- Custom maze input
- Speed controls
- GUI controls
- Web version using Flask / React

---

# 👨‍💻 Author

## Mahika Chaurasiya

Engineering Student | MERN Developer | AI & Algorithms Enthusiast

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and support the project!
