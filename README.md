# MSCS532 Final Project – Optimization in High-Performance Computing

##  Project Overview
This project demonstrates **data-locality optimization**, **vectorization**, and **preallocation** for improving computational performance in High-Performance Computing (HPC) contexts. 

---

##  Repository Contents
- **FinalProjectPresentation.pptx** – PowerPoint slides summarizing the project.
- **FinalProjectReport.docx / FinalProjectReport.pdf** – APA-formatted report describing the technique, implementation, results, and conclusions.
- **HighPerformanceComputingBenchmark.py** – Python script containing baseline and optimized implementations with benchmarking logic.
- **performance_comparison.png** – Graph comparing execution time for baseline vs optimized approaches.
- **performance_results.csv** – Table of benchmark results (execution time, memory usage, speedup).
- **README.md** – This documentation file.

---

##  Optimization Technique
The project applies:
1. **Data-locality optimization** – Using contiguous NumPy arrays instead of Python lists to improve cache performance.
2. **Vectorization** – Replacing nested loops with NumPy broadcasting to leverage SIMD-optimized routines.
3. **Preallocation** – Allocating output arrays once before computation to avoid dynamic resizing overhead.

---

##  How to Run
### Prerequisites
Install the required Python packages:
```bash
pip install numpy matplotlib pandas
python HighPerformanceComputingBenchmark.py
```
##  Presentation Link
[Powerpoint Presentation](https://go.screenpal.com/watch/cTj33Cn2knt)
