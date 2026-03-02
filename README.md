# 🧠 Hybrid Intelligence Lab

An interactive AI system demonstrating hybrid architecture where
classical NLP, deterministic state logic, and LLM conditioning
work together in a controlled reactive pipeline.

Live Demo:
https://ai-playground-nobodiez.streamlit.app/

---

## 🔥 Module 1 — Emotion Amplification Engine

A state-driven emotional modulation system that dynamically
conditions LLM responses based on deterministic sentiment analysis.

### Processing Pipeline
```text
User Input  
↓  
Sentiment Scoring (VADER)  
↓  
Deterministic Intensity Scaling  
↓  
LLM Prompt Conditioning  
↓  
State Update + UI Rendering  
```
### What This Demonstrates

- Hybrid ML + LLM orchestration
- Stateful reactive system design
- Controlled prompt engineering
- Deterministic influence over generative outputs
- Modular system architecture

---

## 😊 Module 2 — Sentiment Analysis Engine

Standalone lexicon-based sentiment analysis using VADER.

Features:
- Real-time polarity detection
- Confidence scoring
- Fully local deterministic processing

---

## 📊 Module 3 — Data Intelligence Toolkit

Upload a CSV file to:

- Inspect dataset structure
- View summary statistics
- Generate basic visualizations

Demonstrates:
- File ingestion pipelines
- Data exploration workflows
- Interactive visualization in Streamlit

---

## 🏗 Project Structure
```text
ai_playground/
│
├── app.py
├── requirements.txt
│
└── utils/
    ├── chaos.py
    └── sentiment.py
```
---

## ⚙️ Technologies Used

- Python
- Streamlit
- OpenAI API
- VADER Sentiment Analysis
- Pandas
- Matplotlib

---

## 🧠 Design Philosophy

The system follows a layered architecture:

- **UI Layer**
  Streamlit page modules under `/pages/` handle layout, interaction, and session state.

- **Logic Layer**
  Reusable AI components under `/utils/`, including:
  - `sentiment.py` — deterministic sentiment scoring
  - `ll_engine.py` — LLM prompt conditioning and response generation

- **Presentation Layer**
  Shared styling utilities (`style.py`) isolate visual concerns from business logic.

This separation enforces modularity, clarity of responsibility,
and controlled interaction between deterministic ML and generative AI.

---

## 🚀 Future Improvements

- Intensity decay mechanism
- Emotion-style response switching
- Conversation summarization memory
- Enhanced data visualization
- Persistent session storage

---

## 👤 Author

Built as part of hands-on experimentation with applied AI
system design and Streamlit interface engineering.