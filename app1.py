import streamlit as st
from transformers import pipeline

# Load the text generation pipeline
@st.cache_resource
def load_pipeline():
    return pipeline("text-generation", model="krushnakant27/Gpt2_Text_Generation")

text_generator = load_pipeline()

# Streamlit App UI
st.title("Text Generation with GPT-2")
st.subheader("On Custom Dataset: 'HuggingFaceH4 ultrachat_200k' Used model: 'openai-community gpt2' ")

# Input prompt from the user
prompt = st.text_input("Enter a prompt:", placeholder="Type something like 'Once upon a time...'")

# Additional options for customization
max_length = st.slider("Max Length", min_value=20, max_value=200, value=50, step=10)
temperature = st.slider("Temperature", min_value=0.1, max_value=1.5, value=0.7, step=0.1)
# num_return_sequences = st.number_input("Number of Outputs", min_value=1, max_value=5, value=1, step=1)

# Generate text when the user clicks the button
if st.button("Generate Text"):
    if prompt.strip():
        st.write("Generating text...")
        outputs = text_generator(
            prompt,
            max_length=max_length,
            # num_return_sequences=num_return_sequences,
            temperature=temperature
        )

        for i, output in enumerate(outputs):
            st.write(f"**Generated Text {i+1}:** {output['generated_text']}")
    else:
        st.error("Please enter a prompt to generate text.")
