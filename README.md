
# 📤 UploadDaily — App to Automatically Upload Files to GitHub

Welcome! This project allows you to upload a `readme.txt` file to your GitHub repository through a very simple web app made with Flask, and also automate this upload to happen once a day without your intervention.

Ideal for learning how to integrate Python + GitHub + automation.

---

## 🎯 What does this app do?

- Shows a web page where you can upload a `.txt` file.
- The file is automatically uploaded to the `txt/` folder of your GitHub repository.
- If the file already exists, it updates it.
- Includes an automatic script to perform the upload **once a day** without opening the browser.

---

## 🧰 Requirements

Make sure you have installed on your computer:

- ✅ [Python 3.12+](https://www.python.org/downloads/)
- ✅ Working `pip`
- ✅ Your own GitHub repository (for example: `UploadDaily`)
- ✅ A **personal GitHub token** with access permissions to that repository (classic token with `repo` permission)

---

## 🛠 Step-by-step installation

## 📝 Summary

| Step                 | Command / Action                                  |
|----------------------|-------------------------------------------------|
| Clone repo           | `git clone https://github.com/Pepehige/UploadDaily.git` |
| Install dependencies | `pip install flask PyGithub schedule`            |
| Run web app          | `python app.py`                                  |
| Run daily upload     | `python auto_upload.py`                          |
| Auto start on Windows| Create a `.bat` file and copy it to the `shell:startup` folder |

