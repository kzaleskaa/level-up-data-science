import streamlit as st

st.set_page_config(
    page_title="Multipage App",
)
st.title("Main Page")
st.sidebar.success("Select a page above.")

# streamlit features
col1, col2 = st.columns([2, 1])
col1.markdown("# Streamlit features")

uploaded_photo = st.file_uploader("Upload a photo")
camera_photo = st.camera_input("Take a photo")

col2.metric(label="Temperature", value="60 °C", delta="2 °C")

with st.expander("Click to read more"):
    st.write("Hello, here are more details on this topic that you were interested in.")

    if uploaded_photo:
        st.image(uploaded_photo)
        