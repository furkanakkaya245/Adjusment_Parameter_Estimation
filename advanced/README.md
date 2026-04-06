# Adjustment and Parameter Estimation (Advanced Geodesy)

This repository provides a comprehensive suite of Python tools for Geodetic Adjustment and Parameter Estimation. It covers the entire spectrum of adjustment calculus, from classical least squares to dynamic state estimation.

## Key Components
* **General Adjustment Models:** Implementation of Parametric, Conditional, and Combined adjustment models.
* **Parameter Estimation:** Advanced estimation techniques including Weighted Least Squares and Bayesian approaches.
* **The `paramDic_2` Library:** A custom-built internal library designed to manage geodetic parameters, dictionary-based data structures, and matrix transformations efficiently across different scripts.
* **Recursive Estimation:** Dynamic system analysis featuring Kalman Filtering (Standard and Extended versions).

## Repository Structure
* **Core Scripts:** Main execution files for adjustment problems (Conformal transformations, Trilateration, Triangulation).
* **`paramDic_2.py`:** The backbone library for data handling and parameter dictionary management.
* **Exam Solutions:** Detailed algorithmic solutions for Adjustment II exams (2023-2025), focusing on "Dengeleme-II" curriculum.

## Technical Stack & Optimization
* **Language:** Python 3.12+
* **Performance:** Optimized for matrix algebra using NumPy.
* **Clean Code:** Utilizes `.gitignore` to maintain a professional environment by excluding temporary files like `__pycache__`.

## Usage
The scripts are designed to be modular. You can import `paramDic_2` for custom geodetic calculations:
```python
from paramDic_2 import your_function_name
