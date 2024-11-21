import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image

# Initialize Hugging Face Inference Client
client = InferenceClient(
    "black-forest-labs/FLUX.1-schnell",
    token="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"
)

# App title
st.title("Text-to-Image Generator 🎨")
st.write("Enter a text prompt to generate an image using Hugging Face models.")

# User input
prompt = st.text_input("Enter a prompt:", placeholder="Astronaut riding a horse")

# Generate button
if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating image..."):
            try:
                # Generate image
                image = client.text_to_image(prompt)
                # Display the image
                st.image(image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid prompt!")



# from huggingface_hub import InferenceClient
# client = InferenceClient("black-forest-labs/FLUX.1-schnell", token="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")

# # output is a PIL.Image object
# image = client.text_to_image("girl writing in her diary")
# image.show()