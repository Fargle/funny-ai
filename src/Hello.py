import streamlit as st

st.set_page_config(
    page_title="Hello"
)

st.sidebar.success("Select a pre-trained agent!")

st.markdown("""
    ### Welcome!

    The point of this app is to investigate the effects of training an AI with certain goals/rewards. 
    On the left side, you will see a columns of selections for you to explore. 

    Each example you will look at has a modified reward. The AI learns how to maximize this reward by interacting with
    its environment. As we will see, this can lead to some interesting results.

    Enjoy!
""")