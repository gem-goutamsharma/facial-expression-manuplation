import streamlit as st
import replicate
import os

# Set the Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_KfCI3rfZ64zUpvj5sCC9HurzRX8D1Qt3mnSHp"

# Streamlit app title
st.title("Facial Expression Manuplation")

# Input field for the image URL
image_url = st.text_input("Image URL", "https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

# Display the input image from the URL
if image_url:
    st.image(image_url, caption="Input Image", use_column_width=True)

if 'prompt' not in st.session_state:
    st.session_state.prompt = None

# Buttons for predefined prompts
if st.button("Smile"):
    print('smile')
    st.session_state.prompt = "Given the original image, modify the mouth corners to be upturned and add a hint of smile to the eyes, while keeping all other facial features and structure unchanged."
elif st.button("Sad"):
    print('sad')
    st.session_state.prompt = "Given the original image, modify the eyebrows to be slightly furrowed and the corners of the mouth to be downturned, while keeping all other facial features and structure unchanged. Additionally, consider adding a slight redness around the eyes to suggest sadness."
# Display the current prompt for user confirmation
if st.session_state.prompt==None:
    st.write(f"Selected Prompt: {st.session_state.prompt}")

# Input field for prompt strength and number of inference steps
prompt_strength = 0.55
num_inference_steps = 25

# Button to generate the output
if st.session_state.prompt and st.button("Generate"):
    with st.spinner("Generating..."):
        # Define the input for the replicate API
        input = {
            "image": image_url,
            "num_inference_steps": num_inference_steps,
            "prompt": st.session_state.prompt,
            "prompt_strength": prompt_strength
        }

        # Call the Replicate API
        output = replicate.run(
            "stability-ai/stable-diffusion-img2img:15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d",
            input=input
        )
        
        # Display the output image
        st.image(output[0], caption="Transformed Image")

# Additional message to guide the user
st.write("Select either 'Smile' or 'Sad' to apply the corresponding transformation before generating the image.")
