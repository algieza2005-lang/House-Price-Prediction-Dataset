import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# ==============================
# 1. LOAD DATASET
# ==============================
df = pd.read_csv("House Price Prediction Dataset.csv")

# ==============================
# 2. PILIH FITUR & TARGET
# ==============================
X = df[["Area", "Bedrooms", "Bathrooms"]]
y = df["Price"]

# ==============================
# 3. HANDLE DATA KOSONG
# ==============================
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# ==============================
# 4. SPLIT DATA
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 5. TRAIN MODEL
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)

# ==============================
# 6. SIMPAN MODEL
# ==============================
joblib.dump(model, "house_price_model.pkl")

print("Model berhasil disimpan sebagai house_price_model.pkl")
