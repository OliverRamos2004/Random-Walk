# Random Walk Simulation

## Description
This Python script simulates a **2D random walk** and visualizes the results using `matplotlib`. The script:
- Generates **1000 random steps** from an initial point `(0,0)`.
- Computes the **step sizes** and **distance from the origin** at each step.
- Produces three visualizations:
  1. **2D Random Walk Path** - A plot of the walk's trajectory.
  2. **Distance from Origin** - A line plot showing the distance from the origin at each step.
  3. **Step Size Distribution** - A histogram displaying the frequency of step sizes.

## Installation
Make sure you have the required libraries installed:
```bash
pip install numpy matplotlib
```

## Usage
Run the script using:
```bash
python Random_walk.py
```

## Output
The script generates a figure with three plots:
1. A **2D plot of the random walk path**.
2. A **line graph showing the distance from the origin over time**.
3. A **histogram of step sizes**.

## Example Visualization
_The script will display a figure similar to this:_
```
+-------------------+--------------------+
| 2D Random Walk   | Distance from Origin |
| (x, y) Path      | vs. Step Number     |
+-------------------+--------------------+
| Step Size Histogram |
+-------------------+
```

## Author
- **Oliver Ramos**
