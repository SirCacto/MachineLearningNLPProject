#Here's my lovely little app. Enjoy!

import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import matplotlib.pyplot as plt


st.set_page_config(page_title="BBC News Classifier", page_icon="🗞️") #Page Config
st.title("🗞️ Welcome to the News Classifier!")
st.markdown("Please enter a news headline or article below to see which category it's determined as!")


@st.cache_resource
def load_model(): #Loads the cached model and tokenizer
    model_path = "SirCacto/NLPBERTDec25"
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

label_map = {0: "Entertainment", 1: "Business", 2: "Sport", 3: "Politics", 4: "Tech"} #Label map

user_input = st.text_area("Enter News Text Here:", placeholder="e.g., Congress just passed a new law. Here's what you need to know...") #Interface

if st.button("Determine News"):
    if user_input.strip() == "":
        st.warning("Please enter some text first! Please...?")
    else:
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        guess_idx = torch.argmax(probabilities).item()
        confidence = torch.max(probabilities).item() * 100
        
        st.success(f"**Prediction:** {label_map[guess_idx]}") #Display the result
        st.info(f"**Confidence Score:** {confidence:.2f}%")
        
        if confidence > 95: #Bonus points for good predictions :)
            st.balloons()