# import requests
#
# url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
#
# payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "9b1ceb7cf2msh9df58c1434776cep1bcbabjsnf62c5c60448e",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

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
        "X-RapidAPI-Key": "9b1ceb7cf2msh9df58c1434776cep1bcbabjsnf62c5c60448e",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    # Make API request
    response = requests.post(url, data=payload, headers=headers)

    # Get the detected language from the response
    language = response.json()["data"]["detections"][0][0]["language"]

    # Display the detected language in Streamlit
    st.write(f"Detected language: {language}")
