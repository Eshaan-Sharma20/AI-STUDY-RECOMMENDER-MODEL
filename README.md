# 🤖 AI Study Recommender System

A simple and practical AI-based project that helps students understand their performance and improve their study strategy. This system predicts a student’s level (weak, medium, strong) based on marks and provides personalized study recommendations.

---

## 📌 Project Overview

This project uses a Decision Tree Machine Learning model to analyze student scores in:
- Mathematics
- Physics
- DSA (Data Structures & Algorithms)

Based on the input, the model predicts the student’s performance level and suggests how they should study to improve or maintain their level.

---

## ⚙️ How It Works

1. The dataset is loaded from a CSV file  
2. The model is trained using the dataset  
3. User enters their marks  
4. The model predicts performance level  
5. A recommendation is generated based on the prediction  

---

## 📁 Project Structure

AI-Study-Recommender/
│
├── main.py
├── requirements.txt
│
├── data/
│   └── dataset.csv
│
└── src/
    ├── model.py
    └── recommend.py

---

## 🧠 Technologies Used

- Python  
- Pandas (data handling)  
- Scikit-learn (machine learning)  

---

## 🚀 How to Run the Project

Step 1: Clone the repository  
git clone <your-repo-link>  
cd AI-Study-Recommender  

Step 2: Install dependencies  
pip install -r requirements.txt  

Step 3: Run the program  
python main.py  

---

## 📥 Input

You will be asked to enter:
- Math score  
- Physics score  
- DSA score  

---

## 📤 Output

- Predicted Level: WEAK / MEDIUM / STRONG  
- Personalized Study Recommendation  

---

## ⚠️ Note

- The dataset contains some overlapping labels intentionally, so predictions may not always be perfect.  
- This project focuses on learning core ML concepts rather than achieving high accuracy.  

---

## 💡 Features

- Simple and beginner-friendly  
- Real-world application of AI  
- Instant prediction and recommendation  
- Clean and modular code structure  

---

## 🔮 Future Improvements

- Add a web or GUI interface  
- Improve dataset quality  
- Use advanced ML models  
- Add performance tracking  

---

## ✅ Conclusion

This project demonstrates how AI can be used in education to guide students in a smarter way. It may be simple, but it clearly shows how machine learning can take input data, make predictions, and provide meaningful suggestions. It’s a great starting point for building more advanced AI-based systems.
