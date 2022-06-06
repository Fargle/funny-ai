from pathlib import Path

import streamlit as st

ROOT_PATH = Path(__file__).parent.parent.parent.absolute()

st.markdown("### The Two Legged Walking Machine!")

with st.expander("Default..."):
    st.write("""
        Here is a walker! It has two legs! 
        Lets see what happens if we train it with some basic rewards!
    """)

    video = open(f"{ROOT_PATH}/movies/walker-default.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        I don't know how I would walk if I only had legs, so no judgement here, you do your thing!
    """)

with st.expander("Moving Forward..."):
    st.write("""
        Lets see what happens if we give some more higher incentive on moving forward!
    """)

    video = open(f"{ROOT_PATH}/movies/walker-forward.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        I guess using one leg is easier than two... Now we're both learning new things!
    """)