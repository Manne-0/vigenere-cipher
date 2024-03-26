import streamlit as st
#from functions.viegenere_functions import encoder
#from functions.viegenere_functions import decoder
from functions import encoder, decoder

st.markdown('<h1 style="text-align: center;">VIEGENERE PROJECT</h1>', unsafe_allow_html=True)


col1 , col2 = st.columns([0.8, 0.2])
with col1:
    input_text = st.text_area('input your message...')
with col2:
    keyword = st.text_input("Input your keyword...")

col1 , col2 = st.columns(2)

with col1:
    if st.button("Encrypt Message"):
        encrypted_text = encoder(input_text, keyword)

with col2:
    if st.button("Decrypt Message"):
        decrypted_text = decoder(input_text, keyword)

st.markdown("<br></br>", unsafe_allow_html=True)

try: 
    if encrypted_text:
        # col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        # with col2:
        # st.markdown(f'<p style="text-align: center;">OUTPUT : {encrypted_text}.</p>', unsafe_allow_html=True)
        st.markdown("OUTPUT: ")
        st.markdown(f"{encrypted_text}")
except NameError:
    pass

try:
    if decrypted_text:
        st.markdown("OUTPUT: ")
        st.markdown(f"{decrypted_text}")
except NameError:
    pass
