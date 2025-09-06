
# 🚀 Startup Funding Analysis Dashboard

An **interactive data analysis dashboard** built with **Streamlit, Pandas, and Matplotlib** to explore Indian startup funding trends. The app provides insights into **Investors, Startups, and Overall Funding** with interactive filters and visualizations.

---

## 📊 Features

* **Investor Analysis**

  * View most recent investments by a selected investor
  * Top 5 biggest investments (bar chart visualization)

* **Startup Analysis**

  * Explore funding details for a chosen startup
  * Insights into funding rounds and investor distribution

* **Overall Analysis**

  * High-level view of startup funding trends

---

## 🛠️ Tech Stack

* **Python** – Data manipulation & backend logic
* **Pandas** – Data cleaning & analysis
* **Streamlit** – Interactive dashboard UI
* **Matplotlib** – Data visualization

---

## ▶️ How to Run

1. Clone the repo

   ```bash
   git clone https://github.com/Ashwin268/startup-funding-dashboard.git
   cd startup-funding-dashboard
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app

   ```bash
   streamlit run app.py
   ```
4. Open in browser at **[http://localhost:8501](http://localhost:8501)**

---

## 📂 Dataset

The dataset (`startup_cleaned.csv`) contains information about:

* Date of funding
* Startup name
* Industry vertical
* City
* Funding round
* Investor(s)
* Amount in Cr

---

## 💡 Future Improvements

* Add time-series analysis for funding trends
* Investor network graph visualization
* Export insights to Excel/CSV
