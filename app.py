import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import streamlit.components.v1 as components

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

# --- SESSION STORAGE & SETTINGS SIDEBAR ---
st.sidebar.title("⚙️ Settings")

# Initialize session state for API key
if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = ""

# JavaScript bridge to sync Streamlit input with browser sessionStorage
session_storage_bridge = """
<script>
const doc = window.parent.document;

function initSessionStorageSync() {
    const apiKeyInput = doc.querySelector('input[aria-label="Gemini API Key"]');
    if (!apiKeyInput) {
        setTimeout(initSessionStorageSync, 100);
        return;
    }

    // Load existing session storage value if input is empty
    const storedKey = sessionStorage.getItem("gemini_api_key");
    if (storedKey && !apiKeyInput.value) {
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.parent.HTMLInputElement.prototype, "value").set;
        nativeInputValueSetter.call(apiKeyInput, storedKey);
        apiKeyInput.dispatchEvent(new Event('input', { bubbles: true }));
    }

    // Save to session storage on change
    apiKeyInput.addEventListener('input', (e) => {
        sessionStorage.setItem("gemini_api_key", e.target.value);
    });
}

initSessionStorageSync();
</script>
"""

# Render the JavaScript bridge component (hidden)
components.html(session_storage_bridge, height=0)

# Render a sidebar text input for the API key
api_key_input = st.sidebar.text_input(
    "Gemini API Key",
    value=st.session_state.gemini_api_key,
    type="password",
    placeholder="Enter your AI Studio API key",
    help="Your key is stored only in your browser session storage."
)

if api_key_input:
    st.session_state.gemini_api_key = api_key_input

# App functionality
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

st.title("Resume Analyzer")

# Check if API key is provided
if not st.session_state.gemini_api_key:
    st.warning("⚠️ Please enter your Gemini API Key in the sidebar settings (⚙️) to proceed.")
else:
    # Configure Gemini with the user-provided key
    genai.configure(api_key=st.session_state.gemini_api_key)
    model = genai.GenerativeModel("gemini-3.5-flash")

    resume = st.file_uploader("Upload your resume (PDF)", type="pdf")
    jd = st.text_area("Paste the job description")

    if st.button("Analyze") and resume and jd:
        text = extract_text(resume)
        prompt = f"""You are an expert recruiter. Compare this resume to the job description.
Give: 1) a match score out of 100, 2) missing skills, 3) five specific suggestions.

RESUME:
{text}

JOB DESCRIPTION:
{jd}"""
        with st.spinner("Analyzing..."):
            try:
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")