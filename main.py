import streamlit as st
import langchain_helper as lch

st.set_page_config(page_title="Pet Name Generator", layout="centered")

st.title("🐾 Pet Name Generator")
st.write("Generate cool pet names using Llama3 + LangChain + Ollama")

animal_type = st.text_input("Animal Type", placeholder="e.g. cow, dog, cat")
pet_colour = st.text_input("Pet Color", placeholder="e.g. black, white, brown")

if st.button("Generate Names"):
    if animal_type and pet_colour:
        with st.spinner("Generating names..."):
            result = lch.generate_pet_name(animal_type, pet_colour)
        st.success("Here are some cool names:")
        st.text(result)
    else:
        st.warning("Please enter both animal type and pet color.")
