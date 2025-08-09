import numpy as np
import math, random, timeit
import tracemalloc
import matplotlib.pyplot as plt
import pandas as pd

# Baseline: Python lists + loops
def baseline_pairwise(n=1000):
    points = [(random.random(), random.random()) for _ in range(n)]
    distances = []
    for i in range(len(points)):
        row = []
        for j in range(len(points)):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            row.append(math.sqrt(dx*dx + dy*dy))
        distances.append(row)
    return distances

# Optimized: NumPy vectorization + preallocation
def optimized_pairwise(n=1000):
    points_np = np.random.rand(n, 2).astype(np.float32)
    distances_np = np.empty((n, n), dtype=np.float32)
    diffs = points_np[:, np.newaxis, :] - points_np[np.newaxis, :, :]
    distances_np[:] = np.sqrt(np.sum(diffs**2, axis=-1))
    return distances_np

# Helper: measure time and memory
def measure(func, *args, **kwargs):
    tracemalloc.start()
    start_time = timeit.default_timer()
    _ = func(*args, **kwargs)
    elapsed = timeit.default_timer() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed, peak / (1024*1024)  # seconds, MB

# Run experiments
sizes = [200, 400, 600, 800, 1000]
baseline_times, optimized_times = [], []
baseline_mem, optimized_mem = [], []

for n in sizes:
    print(f"Running baseline for n={n}...")
    t, m = measure(baseline_pairwise, n)
    baseline_times.append(t)
    baseline_mem.append(m)
    
    print(f"Running optimized for n={n}...")
    t, m = measure(optimized_pairwise, n)
    optimized_times.append(t)
    optimized_mem.append(m)

# Save results table
df = pd.DataFrame({
    "n": sizes,
    "Baseline Time (s)": baseline_times,
    "Optimized Time (s)": optimized_times,
    "Baseline Mem (MB)": baseline_mem,
    "Optimized Mem (MB)": optimized_mem,
    "Speedup (x)": [b/o for b, o in zip(baseline_times, optimized_times)]
})

df.to_csv("performance_results.csv", index=False)
print("\nSaved results table as performance_results.csv")

# Plot results
plt.figure(figsize=(8,5))
plt.plot(sizes, baseline_times, 'r-o', label="Baseline (lists)")
plt.plot(sizes, optimized_times, 'g-o', label="Optimized (NumPy)")
plt.xlabel("Number of Points (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Baseline vs Optimized Performance")
plt.legend()
plt.grid(True)
plt.savefig("performance_comparison.png")
print("Saved performance plot as performance_comparison.png")

# Display summary
print("\n\tBenchmark Summary")
print(df)
