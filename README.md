# 🏠 Housing Price Calculator

A machine learning-powered web application that predicts Boston housing prices using 13 key features from the famous Boston Housing Dataset. Built with Flask, scikit-learn, and deployed live using Render.

## 🚀 Live Demo

👉 [Try it out here](https://housing-price-calculator-1.onrender.com)  *(replace with your live link once deployed)*

---

## ✨ Features

- 📊 Predicts house prices based on:
  - Crime rate
  - Number of rooms
  - Accessibility to highways
  - Distance to employment centers
  - And more...
- 💡 Simple and clean web UI using HTML/CSS
- 📦 Model trained using `RandomForestRegressor`
- 🧠 Full 13-feature ML pipeline with preprocessing
- 🌐 Hosted free using Render for public access

---

## 🧠 Model Info

- Dataset: Boston Housing Dataset (from `sklearn.datasets`)
- Model: Random Forest Regressor
- RMSE: ~2.92 (on full 13-feature model)

---

## 🛠️ Tech Stack

| Layer           | Tools Used                  |
|----------------|-----------------------------|
| 💻 Frontend     | HTML, CSS (custom)          |
| 🧠 ML Model     | scikit-learn, pandas, numpy |
| 🔧 Backend      | Flask                       |
| 🚀 Deployment   | Render.com                  |
| 📦 Model File   | Pickle (`model.pkl`)        |

---

## 🏗️ How to Run Locally

1. **Clone the repo**:

```bash
git clone https://github.com/yourusername/housing-price-calculator.git
cd housing-price-calculator
