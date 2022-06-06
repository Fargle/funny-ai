from pathlib import Path

import streamlit as st

ROOT_PATH = Path(__file__).parent.parent.parent.absolute()


st.markdown("""
    ### The Hopper Agent.
    Each example below will be of a humanoid agent trained with different rewards.

    Click the selections below to view!
""")

with st.expander("Demo"):
    st.write("""
        Here is a hopper! This agent moves by hopping. We can give it minimal
        rewards and it will learn how to move! Amazing!
    """)

    video = open(f"{ROOT_PATH}/movies/hopper-default-step-0-to-step-500.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        I don't know what a normal hopper looks like, so we will leave it here. 
    """)
