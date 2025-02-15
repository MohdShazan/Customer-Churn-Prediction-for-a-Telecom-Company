# 📡 Telecom Customer Churn Prediction

This project predicts whether a telecom customer is likely to **churn (leave the company)** based on their details like **tenure, services, contract type, payment method, and charges**. It uses **machine learning models** and is deployed as an interactive **Streamlit web app**.

## 🚀 Demo  
![app - Google Chrome 15-02-2025 19_06_49](https://github.com/user-attachments/assets/541c6242-21d6-4cd5-9ef2-cb04d09bc316)
![app - Google Chrome 15-02-2025 19_07_01](https://github.com/user-attachments/assets/98109378-6cb8-473c-b647-f45c86a7a32a)
![app - Google Chrome 15-02-2025 19_07_11](https://github.com/user-attachments/assets/e4f588e5-a21f-4770-899e-948a96b7b4ec)
![app - Google Chrome 15-02-2025 19_07_19](https://github.com/user-attachments/assets/ba7a0ee2-f89f-48a2-b19b-5598ac44fb95) 

---

## 📊 Dataset Overview  
- **📂 Dataset**: `WA_Fn-UseC_-Telco-Customer-Churn.xlsx`
- **🧑‍💻 Rows**: 7,043 (each row = one customer)
- **📊 Features**: 20 input features + 1 target variable (`Churn`)

### 🔹 **Key Features**  
| Feature | Description |
|---|---|
| **tenure** | How many months the customer has been with the company |
| **PhoneService** | Has phone service (Yes/No) |
| **InternetService** | DSL, Fiber optic, or No internet |
| **Contract** | Month-to-month, One year, Two year |
| **PaymentMethod** | Electronic check, Mailed check, etc. |
| **MonthlyCharges** | How much the customer pays per month |
| **TotalCharges** | Total amount paid |
| **Churn** (Target) | 1 = Churned, 0 = Stayed |

---

## ⚙️ Steps in the Project  
### **1️⃣ Data Preprocessing**
✅ Removed extra spaces in column names  
✅ Converted categorical data into numbers (One-Hot Encoding)  
✅ Handled missing values (`TotalCharges`)  
✅ Standardized numerical features  

### **2️⃣ Model Training & Evaluation**
We trained multiple models and compared their performance:  

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| **Logistic Regression** | `78%` | `70%` | `55%` | `62%` |
| **Random Forest** | `85%` | `80%` | `60%` | `69%` |
| **XGBoost** | `87%` | `82%` | `65%` | `72%` |

✅ **Best Model:** **XGBoost (87% Accuracy)**  

### **3️⃣ Deployment with Streamlit**
We deployed the trained model into a **Streamlit Web App** that allows users to:  
✅ Enter customer details  
✅ Click **"Predict Churn"**  
✅ See whether the customer **is likely to churn**  

---

## 🎯 Business Insights & Recommendations  
📌 **Who is most likely to churn?**  
- Customers on **month-to-month contracts**  
- Customers with **low tenure (<12 months)**  
- Customers paying via **Electronic check**  
- Customers with **high monthly charges**  

📌 **How to Reduce Churn?**  
✔ Offer **discounts** or **loyalty benefits** to month-to-month customers.  
✔ Provide **better support** to customers with **low tenure**.  
✔ Encourage **long-term contracts** (1-year, 2-year) with discounts.  
✔ Provide incentives to switch from **Electronic Check to Bank Transfer**.  

---

## 🛠️ How to Run This Project Locally  
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/Telecom-Customer-Churn-Prediction.git
cd Telecom-Customer-Churn-Prediction
