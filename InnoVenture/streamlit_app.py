# streamlit_app.py
import sys
import os


# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import streamlit as st
from innoventure.crew import InnoventureCrew
# Page Configuration
st.set_page_config(page_title="InnoVenture - Startup Evaluation Tool", page_icon="🚀", layout="centered")

# Custom CSS styling for a navy blue and bronze/gold theme
st.markdown("""
    <style>
        /* Centered and styled title text */
        .center-text {
            text-align: center;
            color: #D4AF37; /* Bronze/Gold color for headers */
        }

        /* Main container styling for input fields */
        .main-container {
            background-color: #001f3f; /* Navy blue background */
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            color: #D4AF37; /* Bronze/Gold text color for general text */
        }

        /* Button styling */
        .stButton>button {
            background-color: #D4AF37; /* Bronze/Gold button */
            color: #001f3f; /* Navy text color */
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #b8962e; /* Darker shade for hover effect */
        }
        
        /* Input box styling */
        input {
            border: 1px solid #D4AF37 !important;
            border-radius: 5px !important;
            padding: 10px;
            background-color: #001f3f;
            color: #D4AF37;
        }

        /* Divider styling */
        .divider {
            height: 2px;
            background-color: #D4AF37;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
        }

        /* Adjust text color for page */
        body {
            background-color: #001f3f; /* Navy blue background */
            color: #D4AF37; /* Bronze/Gold text color */
        }

        /* Styling headings */
        h1, h2 {
            color: #D4AF37; /* Bronze/Gold headings */
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # Title and Introduction
    st.markdown("<h1 class='center-text'>InnoVenture</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='center-text'>Startup Evaluation Tool</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="main-container">
        <p>Welcome to <strong>InnoVenture</strong>! This tool assists venture capitalists and analysts in evaluating startups using business metrics, industry trends, and social media sentiment.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Input Section
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Startup Evaluation Form")

    # Collect Inputs
    topic = st.text_input("Startup Name", placeholder="Enter the name of the startup")
    industry = st.text_input("Industry", placeholder="Enter the industry of the startup")
    year_month = st.text_input("Research Start Month (MM/YYYY)", placeholder="e.g., 10/2023")

    # Run button to kickoff evaluation
    if st.button("Run Evaluation"):
        inputs = {
            'topic': topic,
            'industry': industry,
            'date': year_month
        }
        # Execute crew kickoff
        st.write("Running evaluation...")
        try:
            InnoventureCrew().crew().kickoff(inputs=inputs)
            st.success("Evaluation complete! Check console or logs for detailed results.")
        except Exception as e:
            st.error(f"An error occurred during the evaluation: {e}")

    # Additional Training Options
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Training and Testing Options")

    # Training Section
    n_iterations = st.number_input("Number of Training Iterations", min_value=1, value=10, step=1)
    filename = st.text_input("Filename to Save Training Data", placeholder="e.g., training_data.json")
    
    if st.button("Start Training"):
        try:
            InnoventureCrew().crew().train(n_iterations=int(n_iterations), filename=filename, inputs={'topic': topic, 'industry': industry, 'date': year_month})
            st.success("Training complete!")
        except Exception as e:
            st.error(f"An error occurred during training: {e}")

    # Replay Section
    task_id = st.text_input("Task ID for Replay", placeholder="Enter the task ID")
    if st.button("Replay Task"):
        try:
            InnoventureCrew().crew().replay(task_id=task_id)
            st.success("Replay executed successfully!")
        except Exception as e:
            st.error(f"An error occurred during replay: {e}")

    # Test Section
    test_iterations = st.number_input("Number of Test Iterations", min_value=1, value=5, step=1)
    model_name = st.text_input("OpenAI Model Name for Testing", placeholder="e.g., gpt-4")
    
    if st.button("Run Test"):
        try:
            InnoventureCrew().crew().test(n_iterations=int(test_iterations), openai_model_name=model_name, inputs={'topic': topic, 'industry': industry, 'date': year_month})
            st.success("Testing complete!")
        except Exception as e:
            st.error(f"An error occurred during testing: {e}")

if __name__ == "__main__":
    main()
