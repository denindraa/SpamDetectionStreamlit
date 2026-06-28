import streamlit as st
import pickle

# Load model dan vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Tampilan
st.set_page_config(page_title="Spam Detection", page_icon="📩")

st.title("📩 Spam Message Detection")
st.write("Masukkan pesan yang ingin diperiksa.")

message = st.text_area("Pesan")

if st.button("Deteksi"):

    if message.strip() == "":
        st.warning("Silakan masukkan pesan terlebih dahulu.")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("🚨 Pesan ini terdeteksi sebagai SPAM")
        else:
            st.success("✅ Pesan ini BUKAN SPAM")
