graph TD
  %% User
  U[🧍 You (Analyst/Builder)] --> A[🧬 Analysis]
  U --> L[🧫 Labs]
  U --> R[🔄 Reverse Engineering]
  U --> T[🧵 Threat Intelligence]
  U --> B[🟦 Blue Ops]
  U --> Rd[🟥 Red Ops]
  U --> P[🟣 Purple Ops]
  U --> F[👁️ Digital Forensics]
  U --> S[🧱 Infra Segmentation]

  %% Purple Doom usage zones
  L --> PD1{{☂️ Purple Doom ON}}
  R --> PD2{{☂️ Purple Doom ON}}
  Rd --> PD3{{☂️ Purple Doom ON}}
  T --> PD4{{☂️ Purple Doom *RECOMMENDED*}}
  F --> PD5{{☂️ Purple Doom *OPTIONAL*}}
  B --> PD6{{☂️ Internal — Not Always Needed}}

  %% Data flows
  A --> L
  L --> R
  R --> Rd
  Rd --> P
  P --> B
  T --> P
  T --> B
  Rd --> S
  B --> S
  F --> T

  %% Styles
  classDef module fill:#111827,stroke:#4b5563,color:#ffffff
  classDef user fill:#facc15,stroke:#ca8a04,color:#000000
  classDef doom fill:#9333ea,color:#ffffff,stroke:#7e22ce

  class U user
  class A,L,R,T,F,B,Rd,P,S module
  class PD1,PD2,PD3,PD4,PD5,PD6 doom

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

