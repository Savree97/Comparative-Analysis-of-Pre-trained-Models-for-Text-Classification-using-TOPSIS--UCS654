# 🧠 Comparative Analysis of Pre-trained Models for Text Classification using TOPSIS  

---

## 📌 Project Objective

The objective of this assignment is to determine the **best pre-trained transformer model for Text Classification** using a structured multi-criteria decision-making technique:

> 🧮 **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**

Instead of relying on a single metric like accuracy, we evaluate models across multiple performance and efficiency criteria and rank them scientifically.

---

## 🚀 Project Overview

This project performs:

- ✅ Text Classification using multiple transformer models  
- ✅ Multi-domain evaluation  
- ✅ Performance metric computation  
- ✅ Decision matrix construction  
- ✅ TOPSIS-based ranking  
- ✅ Final model selection  

The evaluation is performed **domain-wise** to analyze how different models behave across different types of text data.

---

## 📰 Text Domains Considered

Each domain is treated as an independent case study:

- 🏛 Politics  
- ⚽ Sports  
- 🏥 Medicine  

This allows us to understand domain sensitivity of transformer models.

---

## 📂 Dataset Source

Datasets are sourced from **HuggingFace**, which provides publicly available NLP datasets.

Examples:
- News datasets for Politics & Sports  
- Medical text datasets for the Medicine domain  

Dataset loading implementation:

```
code/load_dataset.py
```

---

## 🤖 Pre-trained Models Compared

The following transformer-based models are evaluated:

| Model        | Architecture Type            |
|--------------|-----------------------------|
| BERT         | Bidirectional Encoder       |
| RoBERTa      | Optimized BERT Variant      |
| DistilBERT   | Lightweight Distilled Model |
| ALBERT       | Parameter-efficient BERT    |

Each model is trained and evaluated independently for every domain.

---

## 📊 Evaluation Criteria (Decision Parameters)

For each model, the following metrics are used to construct the decision matrix:

| Parameter | Description      | Type      |
|-----------|------------------|-----------|
| P1        | Accuracy         | Maximize  |
| P2        | Precision        | Maximize  |
| P3        | Recall           | Maximize  |
| P4        | F1-Score         | Maximize  |
| P5        | Inference Time   | Minimize  |
| P6        | Model Size       | Minimize  |

These parameters form the basis of the **TOPSIS ranking process**.

---

## 🧮 Methodology

The workflow followed in this project:

1. Perform text classification for each domain using all models  
2. Compute evaluation metrics  
3. Construct the decision matrix  
4. Normalize the matrix  
5. Apply weighted scoring  
6. Compute Ideal Best & Ideal Worst  
7. Calculate TOPSIS score  
8. Rank models based on closeness coefficient  

Implementation files:

```
code/classification_domainwise.py
code/topsis.py
```

---

## 📈 Results

All results are stored in CSV format inside the `results/` directory.

---

### 🏛 Politics Domain

#### 📊 Metrics
<img width="1089" height="273" alt="image" src="https://github.com/user-attachments/assets/afabc2a2-a116-4885-9b84-bb9a40fa4013" />

#### 🏆 TOPSIS Ranking
<img width="1331" height="255" alt="image" src="https://github.com/user-attachments/assets/bb55e6f5-0217-4ee1-8a7a-b273aac0863d" />

---

### ⚽ Sports Domain

#### 📊 Metrics
<img width="1088" height="259" alt="image" src="https://github.com/user-attachments/assets/e51bf04a-f3c3-449f-88e7-092383fd9320" />

#### 🏆 TOPSIS Ranking
<img width="1334" height="278" alt="image" src="https://github.com/user-attachments/assets/1b0a17f6-eca1-4ec2-a4d9-7dcc85febbaa" />

---

### 🏥 Medicine Domain

#### 📊 Metrics
<img width="1057" height="277" alt="image" src="https://github.com/user-attachments/assets/e3268408-ca8d-4c77-b775-b28b842c7073" />

#### 🏆 TOPSIS Ranking
<img width="1312" height="267" alt="image" src="https://github.com/user-attachments/assets/6c5c75e6-4641-47fc-8f92-18781190ec74" />

---

## 🏅 Final Summary of Best Models

| Domain   | Best Performing Model |
|----------|----------------------|
| Politics | Model ranked 1 in politics_topsis.csv |
| Sports   | Model ranked 1 in sports_topsis.csv |
| Medicine | Model ranked 1 in medicine_topsis.csv |

📌 **Observation:**

> No single model performs best across all domains.  
> This highlights the importance of domain-specific evaluation.

---

## 🛠 How to Run the Project

### 🔹 Step 1: Install Dependencies

```
pip install -r requirements.txt
```

### 🔹 Step 2: Run Classification

```
python code/classification_domainwise.py
```

### 🔹 Step 3: Apply TOPSIS

```
python code/topsis.py
```

---

## 📂 Repository Structure

```
Text-Classification-TOPSIS/
│
├── code/
│   ├── load_dataset.py
│   ├── classification_domainwise.py
│   └── topsis.py
│
├── results/
│   ├── politics_metrics.csv
│   ├── politics_topsis.csv
│   ├── sports_metrics.csv
│   ├── sports_topsis.csv
│   ├── medicine_metrics.csv
│   └── medicine_topsis.csv
│
└── README.md
```

---

## ✨ Key Highlights

✔ Domain-wise model evaluation  
✔ Multi-criteria decision analysis  
✔ Transformer-based classification  
✔ Structured ranking using TOPSIS  
✔ Scientific model selection approach  

---

## 🎯 Conclusion

This project successfully demonstrates how **TOPSIS** can be applied to NLP model evaluation.

Rather than selecting models based solely on accuracy, we incorporate multiple performance and efficiency parameters to make a balanced, data-driven decision.

The results confirm that:

> 🔍 Model performance varies across domains  
> 📊 Multi-criteria evaluation provides deeper insight  
> 🧮 TOPSIS is an effective ranking technique for ML model selection  

---

## 👩‍💻 Author

**Savree Dohar**  
**Roll Number: 102317097**  
UCS761 – Deep Learning
