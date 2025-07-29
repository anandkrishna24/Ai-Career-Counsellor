# 🎓 AI Virtual Career Counsellor

This is an intelligent virtual chatbot built using **Python**, **Rasa**, **NLTK**, and **Streamlit**, integrated with **Gemini 1.5 Flash API** to recommend personalized career paths based on user interests and queries.

---

## 📌 Objective

To guide students and users in selecting suitable career options by understanding their skills, interests, and preferences through natural language conversations.

---

## 🧰 Tools & Technologies

* **Python** for backend logic
* **Rasa** for intent classification & NLU pipeline
* **NLTK** for text preprocessing
* **Streamlit** for interactive web UI
* **Google Gemini API** for AI-based dynamic response generation
* **VS Code** for development

---

## 📁 Folder Structure

```
ai_career_counsellor/
├── .rasa/                  # Rasa internal files
├── actions/               # Custom Python actions
├── data/                  # NLU training data (intents)
├── models/                # Rasa trained models
├── streamlit_app/         # Streamlit UI frontend
├── tests/                 # Rasa testing files
├── config.yml             # Rasa pipeline & policies
├── credentials.yml        # Rasa/Gemini config
├── domain.yml             # Intents, entities, slots, responses
├── endpoints.yml          # Action endpoints
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
```

---

## 🧪 How to Run Locally

### 1️⃣ Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Train the Rasa Model

```bash
rasa train
```

### 3️⃣ Run Rasa Action Server

```bash
rasa run actions
```

### 4️⃣ Launch the Streamlit Frontend

Navigate to the streamlit folder if needed:

```bash
streamlit run app.py
```

Ensure you have added your Gemini API key in `app.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## 🌐 Deploy to Streamlit Cloud

1. Push this project to GitHub (excluding `venv/`, `__pycache__`, etc.)
2. Login to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Set the main file as `streamlit_app/app.py`
5. Add your `GOOGLE_API_KEY` in Secrets tab if needed

---

## 🎯 Features to Include in Final Project

* [x] Predefined intents for domain-specific career paths (tech, commerce, arts, etc.)
* [x] Real-time conversation with contextual memory
* [x] Gemini API integration for knowledge-rich responses
* [x] Interactive and clean Streamlit UI
* [x] Custom actions for dynamic replies and links
* [x] Response history with user and assistant messages
* [ ] Optional: Upload resume and get career suggestion

---

## 📹 Deliverables

* ✅ Rasa project folder
* ✅ Frontend UI (`streamlit_app/`)
* ✅ `requirements.txt` and `README.md`
* ✅ GitHub repo
* ✅ 📽️ Demo video

---

## 🔗 Example Questions to Try

* "What careers are good for someone good at math and logic?"
* "I’m interested in art and creativity, what should I pursue?"
* "Suggest tech careers without a college degree"
* "What skills do I need for data science?"

---

## 🧠 Credits

Built as a final year AI/ML project to demonstrate NLP, LLMs, and chatbot UI integration.

---

## 📌 License

MIT License.
