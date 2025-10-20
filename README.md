# 🚚 Delivery Route Optimizer (Graph + Greedy)

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent **package delivery route planner** that finds the *shortest delivery path* using **Dijkstra’s Algorithm** and a **Greedy Heuristic**.  
Visualized with an **interactive Kepler.gl map** to show optimized delivery routes in real-world coordinates.

---

## ✨ Features

- 🧭 **Shortest Path Calculation** – Uses Dijkstra’s Algorithm to find minimum-distance routes.  
- ⚡ **Greedy Route Optimization** – Approximates a multi-stop delivery path efficiently.  
- 🌍 **Interactive Visualization** – View routes on a 3D Kepler.gl map (HTML export).  
- 🧠 **Applied DSA** – Real-world demonstration of graph algorithms for logistics.

---

## 📂 Project Structure

```text
delivery-route-optimizer/
│
├── data/
│ └── locations.csv # Sample locations (latitude, longitude)
│
├── src/
│ ├── main.py # Main entry point
│ ├── graph_utils.py # Graph + Dijkstra’s logic
│ ├── greedy_optimizer.py # Multi-stop route optimization
│ └── visualize.py # Kepler.gl visualization
│
├── maps/
│ └── optimized_route_map.html # Interactive map output
│
├── requirements.txt
└── README.md
```


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shabbirbasha-dev/delivery-route-optimizer.git
cd delivery-route-optimizer
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the project
```bash
python src/main.py
```
---

## 🧾 Example Output

```bash
✅ Loaded 5 locations.
✅ Graph built with 5 nodes and 10 edges.

📦 Shortest Path 1 → 5: [1, 5] (4.92 km)

🚚 Running Greedy Route Optimization...
✅ Greedy route complete: [1, 5, 4, 2, 3]
🧭 Total Distance: 11.64 km
🗺️  Route map saved to: optimized_route_map.html

```

---

## 🌍 Visualization

After running main.py, an interactive map is generated:
```bash
maps/optimized_route_map.html
```
### Each dot represents a delivery point
### The line shows the optimized delivery route order

---

## 🧠 Algorithms Used

### Dijkstra’s Algorithm – Calculates shortest path between locations.

### Greedy Heuristic (Nearest Neighbor) – Builds an efficient delivery sequence.

### Graph Data Structure – Models real-world delivery nodes and edges.

---

## 🚀 Future Improvements

### Integrate real road distances using OpenRouteService API

### Add multiple delivery vehicles and time windows

### Use A* or Genetic Algorithms for advanced optimization

### Host live map dashboards using Streamlit or Dash

--- 

## 👤 Author

**Shabbir Basha Shaik** 
🔗 [GitHub](https://github.com/shabbirbasha-dev) • [LinkedIn](https://linkedin.com/in/shabbirbasha-dev)

---

## 📜 License

### This project is licensed under the MIT License – feel free to use and modify it.
