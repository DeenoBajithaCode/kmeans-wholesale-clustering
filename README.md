# 📦 KMeans Wholesale Clustering

This project demonstrates how to use **K-Means clustering** to segment wholesale customers based on their annual spending patterns. The workflow includes:

- Exploratory Data Analysis (EDA)  
- Preprocessing  
- Model building  
- Evaluation  
- Cluster labeling  

---

## 🗂️ Project Structure

```
kmeans-wholesale-clustering/
├── data/                    # Raw input data 
├── notebooks/              # Jupyter notebooks for experimentation 
├── src/                    # Source code modules 
├── Wholesale_Profile.html  # Auto-generated EDA report 
├── requirements.txt        # Python dependencies 
└── README.md               # Project documentation
```

---

## 📊 Dataset

- **Source:** [UCI Wholesale Customers Data Set](https://archive.ics.uci.edu/ml/datasets/wholesale+customers)
- **Features Used for Clustering:**
  - Fresh  
  - Milk  
  - Grocery  
  - Frozen  
  - Detergents_Paper  
  - Delicassen  
- **Excluded Columns:**
  - Channel  
  - Region  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/DeenoBajithaCode/kmeans-wholesale-clustering
cd kmeans-wholesale-clustering
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run EDA

```bash
python src/eda.py
```

This will generate an HTML report: `Wholesale_Profile.html`.

### 4. Run Clustering

Open the following notebook and run through all cells:

```bash
notebooks/kmeans_clustering.ipynb
```

---

## 🔍 Key Techniques

- 📊 **Data Profiling**: Using `ydata-profiling` for automated EDA  
- ⚖️ **Standardization**: `StandardScaler` from `sklearn.preprocessing`  
- 🔁 **Clustering**: KMeans from `sklearn.cluster`  
- 📈 **Evaluation**: Elbow method and Yellowbrick’s `KElbowVisualizer` to find the optimal number of clusters  

---

## 🛠️ Tech Stack

- Python  
- Jupyter Notebooks  
- Scikit-learn  
- Pandas & NumPy  
- ydata-profiling  
- Yellowbrick  

---

## 📌 Notes

- Make sure to exclude non-numerical or categorical columns like `Channel` and `Region` for meaningful clustering.  
- Experiment with different scaling methods or feature sets to improve clustering results.

---

## 📬 Contact

For issues or collaboration, feel free to open an issue or PR on the [GitHub repo](https://github.com/DeenoBajithaCode/kmeans-wholesale-clustering).

---

