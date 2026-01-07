import streamlit as st
import base64

def base64ToString(b):
    return base64.b64decode(b).decode('ascii')

st.title("Šifrování a Dešifrování BBC")

title = st.text_input("Tady zadejte váš text", "")


encod = title.encode('ascii')
encoded = base64.b64encode(encod)

st.text_area("Tady je vaše šifra", encoded)

st.subheader("Dešifrace BBC")

b = st.text_input("Tady napište vaši BBC šifru", "")


encoded_bytes = b.encode('utf-8')
        
decoded_bytes = base64.b64decode(encoded_bytes)
        
original_string = decoded_bytes.decode('utf-8')
        
st.text_area("Dešifrovaný text", original_string)


