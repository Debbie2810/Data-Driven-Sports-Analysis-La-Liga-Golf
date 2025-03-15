# 📊 Statistics for Machine Learning Project

This project analyzes **La Liga team performance** and **Golf ball driving distances** using statistical methods. It includes data preprocessing, exploratory analysis, hypothesis testing, and confidence interval calculations.

## 🔹 Project Overview
- **La Liga Analysis:**
  - Identify teams that started between 1930-1980.
  - Find the top 5 teams based on total points.
  - Compute winning percentages and find the top 5 teams.
  - Conduct a hypothesis test to check if teams with a best position of 1-3 have a significantly higher winning percentage than teams ranked 4-7.
- **Golf Analysis:**
  - Compare driving distances between current and new golf ball models.
  - Perform a hypothesis test to determine if there is a significant difference.
  - Compute 95% confidence intervals for mean driving distances.

## 📂 Files Included
- `Statistics_ML_Project.ipynb` - Jupyter Notebook with full analysis.
- `Laliga.csv` - Dataset for La Liga teams.
- `Golf.csv` - Dataset for Golf ball distances.
- `README.md` - Project documentation.

## 🔬 Key Findings
### 🏆 La Liga Analysis
- **Teams that started between 1930 and 1980** include Valencia, Sevilla, Real Betis, etc.
- **Top 5 Teams by Points:**
  1. Real Madrid (4385 points)
  2. Barcelona (4262 points)
  3. Atletico Madrid (3442 points)
  4. Valencia (3386 points)
  5. Athletic Bilbao (3368 points)
- **Top 5 Teams by Winning Percentage:**
  1. Real Madrid (59.63%)
  2. Barcelona (57.24%)
  3. Atletico Madrid (47.48%)
  4. Valencia (44.56%)
  5. Athletic Bilbao (43.77%)
- **Hypothesis Test:** There is a significant difference in winning percentage (p-value ≈ 0.00001536).

### ⛳ Golf Hypothesis Testing
- **T-test Results:** No significant difference in mean driving distances (p-value ≈ 0.188).
- **95% Confidence Intervals:**
  - Current model: (267.48, 273.07) yards
  - New model: (264.33, 270.67) yards
  - Difference in means: (-1.38, 6.93) yards

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/statistics-ml-project.git
   ```
2. Navigate to the project folder:
   ```bash
   cd statistics-ml-project
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Statistics_ML_Project.ipynb
   ```
4. Run all cells to execute the analysis.

## 📌 Conclusion
This project demonstrates statistical analysis techniques using **Python, Pandas, SciPy, and Seaborn**. It applies **hypothesis testing, confidence intervals, and data visualization** to real-world datasets in sports analytics.



