# 🔍 A* Pathfinding Visualizer | Python Maze Solver
📌 Overview

This project is a visual implementation of the A (A-Star) Pathfinding Algorithm* using Python and the pyamaze library.
The program generates a maze and intelligently finds the shortest path from the start position to the goal using heuristic-based search.

The visualization shows:

Complete search traversal
Explored nodes
Final shortest path
Real-time moving agents with footprints

🚀 Features

A* shortest pathfinding algorithm
Dynamic maze generation
Animated path traversal
Multiple agents visualization
Manhattan Distance heuristic
Dark theme maze UI
Search path vs shortest path comparison

🛠 Tech Stack
Python
Priority Queue
pyamaze
A* Algorithm

📂 Project Structure
MazeSolving/
│
├── astar.py
├── README.md
└── requirements.txt

⚙️ Installation

1️⃣ Clone Repository

git clone https://github.com/mahikaverse/maze-solver-astar.git

2️⃣ Move into Project Folder

cd maze-solver-astar

3️⃣ Create Virtual Environment

python -m venv .venv

4️⃣ Activate Virtual Environment

Windows
.venv\Scripts\activate

Linux / Mac
source .venv/bin/activate

5️⃣ Install Dependencies

pip install pyamaze

▶️ Run Project

python astar.py


🧠 How A* Works

A* algorithm combines:

g(n) → actual distance from start node
h(n) → heuristic estimated distance to goal

Formula:

f(n)=g(n)+h(n)

This project uses Manhattan Distance Heuristic:
h(x, y) = abs(x1 - x2) + abs(y1 - y2)
  
The algorithm always chooses the node with the lowest estimated total cost.

🎨 Visualization
Agents Used
Agent Color	Purpose
🔴 Red	Search Traversal
🔵 Blue	Reverse/Backtracking Path
🟢 Green	Final Shortest Path
📸 Output

The maze window displays:

Generated maze
Animated agents
Path footprints
Path length statistics

📚 Concepts Learned
Pathfinding Algorithms
Graph Traversal
Heuristic Search
Priority Queue
AI Search Techniques
Maze Solving Logic

🔥 Future Improvements
Dijkstra Algorithm support
BFS / DFS comparison
Custom maze input
Speed controls
GUI controls
Web version using Flask/React

👨‍💻 Author

Mahika Chaurasiya
Engineering Student | MERN Developer | AI & Algorithms Enthusiast

⭐ If you like this project

Give it a star on GitHub ⭐
