# 🏏 IPL 2025 Data Analysis & Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Pandas_Seaborn_Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-In_Development-yellow)

## 📖 Overview
This project involves a comprehensive Exploratory Data Analysis (EDA) of the **IPL 2025** season. It analyzes player performance (batters and bowlers) and team standings to derive meaningful insights using Python. The project aims to visualize key metrics like run rates, strike rates, wicket-taking abilities, and team dominance.

## 📊 Datasets
The analysis is based on the following datasets:

1.  **`pointtable.csv`**: Contains team standings, points, won/lost records, and Net Run Rate (NRR).
2.  **`IPL2025Batters.csv`**: detailed batting statistics including:
    * Runs, Matches, Innings, Not Outs
    * High Scores (HS), Averages (AVG), Strike Rates (SR)
    * Boundary counts (4s, 6s) and Milestones (50s, 100s)
3.  **`IPL2025Bowlers.csv`**: Detailed bowling statistics including:
    * Wickets (WKT), Overs (OVR), Runs Conceded
    * Economy (ECO), Bowling Average (AVG), Strike Rate (SR)
    * Best Bowling Figures (BBI), 4-wicket and 5-wicket hauls

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

## 🔎 Key Features & Analysis

### 1. Points Table Analysis
* Team rankings based on Points and NRR.
* Win/Loss analysis for all 10 teams.

### 2. Batting Analysis
* **Univariate Analysis:** Histograms for Runs, Strike Rates, and Boundary counts.
* **Bivariate Analysis:**
    * Runs vs. Strike Rate correlations.
    * Top Run Scorers sorted by team.
    * Comparison of 4s and 6s across teams.
* **Team-wise Split:** Dedicated visualizations for each franchise (CSK, MI, RCB, GT, etc.).

### 3. Bowling Analysis
* Distribution of Wickets, Economy Rates, and Bowling Averages.
* Scatter plots identifying top-performing bowlers.
* Team-wise contribution to total wickets and overs bowled.

### 4. Correlation Heatmaps
* Analysis of relationships between metrics (e.g., Batting Average vs. Strike Rate, Economy vs. Wickets).

## 🚀 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/samanthuday0339/ipl2025app.git](https://github.com/samanthuday0339/ipl2025app.git)
    cd ipl2025app
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```

3.  **Run the Analysis**
    * If using a Jupyter Notebook, open the `.ipynb` file and run all cells.
    * If using a Python script, execute:
        ```bash
        python analysis_script.py
        ```

## 📈 Sample Insights
* **Top Teams:** Ranking analysis based on the Points Table.
* **Power Hitters:** Identification of players with the highest 6s and Strike Rates.
* **Economy Kings:** Bowlers with the best Economy Rates in the tournament.

## 🤝 Contributing
Contributions are welcome!
1.  Fork the project.
2.  Create a new branch (`git checkout -b feature/NewAnalysis`).
3.  Commit your changes.
4.  Push to the branch and open a Pull Request.

## 📝 License
This project is open-source and available for educational and analytical purposes.
