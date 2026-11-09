# 📄 Resume Analyzer

A simple, secure Streamlit web application that uses Google's Gemini AI to analyze a candidate's resume against a specific job description. It provides a match score, identifies missing skills, and offers actionable suggestions for improvement.

## 🚀 Features

- **PDF Text Extraction:** Extracts text from uploaded resume PDF files using `pypdf`.
- **Gemini-Powered Analysis:** Leverages Google's Gemini AI model (`gemini-3.5-flash`) via Google AI Studio to evaluate candidate suitability.
- **Secure API Key Handling:** Allows users to enter their Gemini API key directly into the sidebar using session storage for privacy.

---

## 🛠️ Installation & Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/akshh-bot/Resume_Analyzer.git
cd Resume_Analyzer
```

### 2. Create a Virtual Environment (Recommended)

Create an isolated Python environment to manage project dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Requirements

Install all the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Running the Application

Once the installation is complete, follow these steps:

1. Make sure your virtual environment is activated.
2. Ensure your main Python script is named `app.py`.
3. Launch the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. Open the local URL displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)) in your web browser.

---

## 💡 How to Use

1. **Get an API Key:** Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. **Enter API Key:** Launch the application, expand the **⚙️ Settings** section in the sidebar, and paste your API key into the password field.
3. **Upload Resume:** Upload your resume in PDF format using the file uploader.
4. **Provide Job Description:** Paste the target job description into the designated text area.
5. **Analyze:** Click the **Analyze** button to generate your results, including:
   - Resume match score.
   - Missing or relevant skills.
   - Actionable recommendations for improving your resume.

---

## 📌 Tech Stack

- **Python** – Core programming language.
- **Streamlit** – Web application framework.
- **Google Gemini AI** – AI-powered resume analysis.
- **PyPDF** – PDF text extraction.

---

## 👨‍💻 Author

**Akshh-bot**

GitHub: [@akshh-bot](https://github.com/akshh-bot)
