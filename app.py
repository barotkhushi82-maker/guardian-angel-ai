import streamlit as st
import google.genai as genai

# Page Setup
st.set_page_config(page_title="Guardian Angel AI", page_icon="🛡️")
st.title("🛡️ Guardian Angel AI")
st.subheader("Your Post-Leak Cybersecurity First Responder")

st.write("Simulate a GitLab repository push to see how the AI Agent performs a post-leak recovery plan.")

# Simple Code Input
code_input = st.text_area(
    "Sample Code with Exposed Token:", 
    value='''def connect_to_gitlab():\n    # Accidentally hardcoded access token\n    gitlab_token = "glpat-FakeToken12345XYZ"\n    print("Connected")''', 
    height=120
)

# Free API key collection
api_key = st.text_input("Enter your Free Gemini API Key to activate the Agent:", type="password")
st.caption("Don't have one? You can generate a free key in seconds at aistudio.google.com")

if st.button("Activate Incident Response Agent"):
    if not api_key:
        st.warning("Please input a Gemini API Key to run the agent live.")
    elif "glpat-" in code_input or "token" in code_input:
        st.error("🚨 CRITICAL: Leaked GitLab Credential Found!")
        
        # Initialize the free Gemini Client
        try:
            client = genai.Client(api_key=api_key)
            
            prompt = f"""
            You are Guardian Angel AI, an expert cybersecurity incident responder guiding a beginner developer through an emergency.
            They accidentally pushed a file with this leaked token to a GitLab repo:
            {code_input}
            
            Provide a response with:
            1. An empathetic message telling them to stay calm.
            2. The exact 'git filter-repo' or 'git filter-branch' commands they need to type to completely purge this secret from their git history.
            3. Explicit directions on how to revoke this token immediately inside GitLab settings.
            """
            
            with st.spinner("Agent running incident response strategy..."):
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Could not connect to agent: {e}")
    else:
        st.success("✅ Repository clean. No exposed tokens detected.")
