from pathlib import Path

import streamlit as st

ROOT_PATH = Path(__file__).parent.parent.parent.absolute()

st.set_page_config(page_title = "Humanoid Agent Demo")
st.sidebar.header("Humanoid Agent")

st.markdown("""
    ### The Humanoid Agent.
    Each example below will be of a humanoid agent trained with different rewards.

    Click the selections below to view!
""")
with st.expander("Default..."):
    st.markdown("""
        ## A Basic Agent
        Here we have a humanoid. The goal of the humanoid is to stay standing, walk, and mainly do things that have to do with human walking.
        The catch is that the humanoid is controlled by an AI. Let's see what it looks like!
    """)
    video = open(f"{ROOT_PATH}/movies/TQC-step-0-to-step-500.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.markdown("""
        The problem is that this humanoid doesn't look very natural walking. This is a prime example of where training for a specific goal didn't 
        really work out as expected.
    """)


with st.expander("Moving Forward..."):
    st.write("""
        Maybe we give the humanoid the goal of moving forward. Like, if it moves forward, we give it many congrats and all the cookies.
        Or.. whatever a humanoid likes... Maybe it is cookies! 
    """)
    video = open(f"{ROOT_PATH}/movies/TQC-move-forward-step-0-to-step-500.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        Wow! Look at the AI go! Still, not exactly as expected... Maybe we need to think a little more careful about the goals we are giving it.
    """)


with st.expander("I think I broke it..."):
    st.write("""
        There are some rewards in here that seem to be based on ground contact time. Lets mess with them!
    """)
    video = open(f"{ROOT_PATH}/movies/TQC-contact-step-0-to-step-500.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        Well... Not sure exactly what happened. I think its existence is just pain now. 
    """)


with st.expander("Give Agent Alcohol."):
    st.write("""
        This one's on you, you clicked.
    """)
    video = open(f"{ROOT_PATH}/movies/dancing-or-drunk.mp4", "rb")
    video_bytes = video.read()
    st.video(video_bytes)

    st.write("""
        I mean, maybe it's just dancing... badly... It's still learning!
    """)