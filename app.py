import streamlit as st
import whisper
import tempfile

st.set_page_config(page_title="Audio to Text", page_icon="🎤")

st.title("🎤 Audio to Text Converter")

uploaded_file = st.file_uploader(
    "Upload an Audio or Vedio",
    type=["mp3","wav","m4a","mp4","mov","avi","mkv"]
)

if uploaded_file is not None:
    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_path = temp_audio.name

    if st.button("Convert to Text"):
        with st.spinner("Converting... Please wait..."):
            model = whisper.load_model("base")
            result = model.transcribe(temp_path)

        st.success("Conversion Completed!")
        st.subheader("Transcribed Text")
        st.write(result["text"])