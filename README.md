# 🐍 13 - Programming Basics with Python

---

## 🚀 What Can You Build with Python?

- 🌐 Web applications (Django, Flask)
- 🔍 Web scraping (BeautifulSoup, Selenium)
- ⚙️ Automation & scripting (os, subprocess)
- 🤖 Machine Learning (scikit-learn, TensorFlow)
- 📊 Data Science (pandas, NumPy, matplotlib)
- 🧠 AI & NLP (spaCy, OpenAI, transformers)

---

## 🧠 Python Basics

### 🔤 Variable Types

Python supports various data types. Here are the most common ones you'll encounter:

- `str` – String (e.g., `"hello"`)
- `int` – Integer (e.g., `42`)
- `float` – Floating-point number (e.g., `3.14`)
- `bool` – Boolean (`True` / `False`)
- `list` – Ordered, mutable collection (e.g., `[1, 2, 3]`)
- `set` – Unordered, unique collection (e.g., `{1, 2, 3}`)
- `dict` – Key-value pairs (e.g., `{"name": "Arno"}`)

> ✅ Python has more types like `tuple`, `complex`, etc., but they aren't covered in this course.

---

## 🧾 Are Variables Objects in Python?

In Python, **everything is an object** — even primitive types.

- A **variable** is a **reference (pointer)** to an object in memory.
- This means variables can access the object’s methods and properties.
- Variables are **dynamically typed** and **overwritable**.
  - 👉 Unlike GoLang, where variable types and mutability are stricter.

---

## 🧪 Useful Functions & Methods

Here are some built-in tools you’ll often use:

| 🔧 Function / Method | 🔍 Description                        |
|----------------------|--------------------------------------|
| `type(x)`            | Get the data type of `x`             |
| `str(x)`             | Cast to string                       |
| `int(x)`             | Cast to integer                      |
| `set(x)`             | Convert to set (unique elements)     |
| `f"{x}"`             | String formatting                    |
| `x.isdigit()`        | Check if `x` (a string) is a digit   |
| `x.split()`          | Split string into list               |
| `list.append(x)`     | Add element to list                  |
| `set.add(x)`         | Add element to set                   |
| `set.remove(x)`      | Remove element from set              |

---

