# chatbot_openai

# WeCredit Virtual Assistant

WeCredit is a **virtual financial assistant** that helps users with queries related to **loans, credit scores, interest rates, and financial guidance**. This AI-powered chatbot is built using **OpenAI's GPT model** and deployed using **Streamlit**.

----
## 🌟 Features

✅ **AI-Powered Assistance:** Get real-time financial information powered by OpenAI's GPT-3.5 Turbo.  
✅ **Interactive Chat Interface:** Simple and easy-to-use UI built with **Streamlit**.  
✅ **Secure API Handling:** Secrets are stored securely using **Streamlit Secrets Manager**.  
✅ **Customizable & Scalable:** Modify responses and add new functionalities as needed.  


----

## 🛠️ Tech Stack

- **Python**: Backend logic
- **OpenAI API**: AI-powered responses
- **Streamlit**: Web-based UI
- **Streamlit Cloud**: Deployment

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
$ git clone  https://github.com/techfreakydeepak/chatbot_openai.git
$ cd Project_Chatbot_5
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
$ python -m venv financebot
$ source financebot/bin/activate  # On Mac/Linux
$ financebot\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4️⃣ Set Up Your OpenAI API Key

Since GitHub is open-source, **do NOT push your API key** to GitHub. Instead:

#### 🔹 **Local Development**
Create a `.streamlit/secrets.toml` file and add:
```toml
OPENAI_API_KEY="your-secret-api-key"
```
----
#### 🔹 **Streamlit Cloud Deployment**
1. Go to **Streamlit Cloud → Your App → Settings → Secrets**
2. Add your API key like this:
```
OPENAI_API_KEY="your-secret-api-key"
```

----
## 🎯 Project Structure

```
wecredit-virtual-assistant/
│── chatbot.py       # Handles AI responses from OpenAI API
│── app.py           # Streamlit UI
│── requirements.txt # Project dependencies
│── README.md        # Documentation
└── .streamlit/
    └── secrets.toml # (Not pushed to GitHub) Secure API key storage
```
----

## 🏗️ Running the Project

### 🔹 Local Development
```bash
$ streamlit run app.py
```

### 🔹 Deploying on Streamlit Cloud
1. Push your code to GitHub.
2. Go to **Streamlit Cloud** → Create a new app.
3. Connect your GitHub repository.
4. Add API key in **Settings → Secrets**.
5. Click **Deploy**!

Your WeCredit Virtual Assistant is now live! 🎉

----

---

## 🛡️ Security Measures

🔒 **DO NOT expose your API key in GitHub.** Use **Streamlit Secrets** to store it securely.  
🔒 **Add `.streamlit/secrets.toml` to `.gitignore`** to prevent accidental leaks.

---

## 🤝 Contributing

Want to improve WeCredit? Contributions are welcome! ✨

1. **Fork** the repository.
2. Create a **new branch** (`git checkout -b feature-new`).
3. **Commit your changes** (`git commit -m 'Add new feature'`).
4. **Push** the branch (`git push origin feature-new`).
5. Open a **Pull Request**.

---
## 📞 Contact or Support
**Developer:** Deepak  
📧 Email: [itsdeepaksingh00@gmail.com](mailto:itsdeepaksingh00@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/deepak-singh](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)  
For any issues, create an [issue]( https://github.com/techfreakydeepak/chatbot_openai.git.issue) on GitHub or reach out via email.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🌟 Acknowledgments
Thanks to **OpenAI** and **Streamlit** for making AI-powered applications accessible!


