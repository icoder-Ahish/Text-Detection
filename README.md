# Text-Detection

## Import Required Modules

    import requests
    import streamlit as st

    st.title("Language Detection")

# Get the user input
    input_text = st.text_input("Enter text to detect the language:")

    if input_text:
        # Define API parameters
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
        payload = f"q={input_text}"

# Define API headers
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "Your_api_key",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

# Make API request
         response = requests.post(url, data=payload, headers=headers)

# Get the detected language from the response
      language = response.json()["data"]["detections"][0][0]["language"]

# Display the detected language in Streamlit
      st.write(f"Detected language: {language}")
      
# Run Your application
      streamlit run GoogleTransletApi
