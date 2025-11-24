# 🔐 Password Strength Checker – Statement Document

## 📘 Project Statement
This project is a simple Python-based tool designed to evaluate the **strength of a user-entered password**. It analyzes the password against several common security criteria and outputs whether the password is **Strong**, **Medium**, or **Weak**.

---

## 🎯 Purpose
The primary goal of this script is to:
- Help users understand the quality of their passwords  
- Provide a beginner-friendly demonstration of password validation logic  
- Showcase character checking, conditional logic, and user input handling in Python  

---

## 🧠 Password Evaluation Criteria
The password is checked for the following five conditions:

1. 🔤 Contains at least one **lowercase letter**  
2. 🔠 Contains at least one **uppercase letter**  
3. 🔢 Contains at least one **digit**  
4. 🔣 Contains at least one **special character**  
5. 📏 Is **longer than 7 characters**

---

## 📊 Output Classification
Based on how many conditions the password meets:

| Conditions Met | Strength |
|----------------|----------|
| 5              | 🟩 Strong |
| 3–4            | 🟧 Medium |
| 1–2            | 🟥 Weak |

---

## ▶️ How to Run
1. Save the Python script to a file (e.g., `password_checker.py`)  
2. Run it in your terminal or command prompt:
   ```
   python password_checker.py
   ```
3. Enter your password when prompted  
4. View the evaluated strength on screen  

---

## 🚀 Possible Enhancements
Future improvements to expand functionality:

- Add password score out of 5  
- Provide suggestions for improving weak passwords  
- Implement GUI or web interface  
- Replace `ord()` logic with more Pythonic methods  
- Add repeated attempts and input validation  

---

## 📄 Author Statement
This project was created to demonstrate foundational password-validation logic and help users understand the importance of strong password creation. It can be used as a learning resource or expanded into a more advanced security tool.