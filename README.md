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
$ git clone  
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

