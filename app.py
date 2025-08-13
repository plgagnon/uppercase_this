import streamlit as st

def uppercase_this():
    st.session_state['this_string'] = st.session_state['this_string'].upper()


st.text_input(
    "Enter a string:",
    key='this_string',
)

st.button(
    label="Uppercase the string above",
    key='uppercase_button',
    on_click=uppercase_this
)

# st.write(f"Current string: {st.session_state.get('this_string', '')}")
