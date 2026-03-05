# 🧮 Quick-Calc

Quick-Calc is a simple desktop calculator application built with Python and Tkinter.
The calculator supports parentheses and handles invalid expressions by displaying an error message.

---

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* ( ) Parentheses support
* 🧹 Clear button to reset the calculation
* 🖥️ Simple graphical user interface

---

## ▶️ How to Run

1. Make sure **Python** is installed on your computer.
2. Clone this repository:

```
git clone https://github.com/SofiiaBardakovaa/swe-testing-assignment.git
```

3. Navigate to the project folder.

4. Run the program:

```
python main.py
```
## Screenshot

<img width="247" height="260" alt="image" src="https://github.com/user-attachments/assets/9b202400-eda0-448c-8571-fff5ddd2a943" />

---

## 🧪 Example

Example calculation:

```
(2 + 3) * 4 = 20
```

---

## Running Tests

Install **pytest** if it is not installed: 
```
pip install pytest
```

Run all unit tests with: 
```
pytest
```

---

## 🚀 Testing Framework Research

Two of the most widely used testing frameworks in Python are Unittest and Pytest. **The unittest framework** is included in Python’s standard library and follows the xUnit testing style, which organizes tests into classes and methods. This structure provides a clear and consistent way to organize tests, and because it is built into Python, it does not require any additional installation. However, writing tests with unittest often requires more boilerplate code and more complex syntax compared to newer frameworks.

**Pytest** is a popular third-party testing framework known for its simplicity and flexibility. It allows developers to write tests using simple functions and standard assert statements instead of complex class structures. Pytest also automatically discovers test files and provides useful features such as fixtures, parameterized tests, and detailed error reports. These capabilities make it easier to write, organize, and maintain test cases in Python projects.

For this project, Pytest was selected as the testing framework because it requires less boilerplate code and offers more readable syntax. Its automatic test discovery and powerful features make it especially suitable for small projects like our while still supporting more advanced testing if the project grows in the future.

Resource: **https://www.browserstack.com/guide/pytest-vs-unittest**
