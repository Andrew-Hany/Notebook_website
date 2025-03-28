import streamlit as st
import streamlit.components.v1 as components

def cell_component(user_code: str, text_area_key: str) -> str:
    """
    Renders an interactive text area that dynamically adjusts its height in real time
    as the user types. The height increases automatically when the user adds new lines.

    Parameters:
        idx (int): The index of the cell, used to generate a unique key for the text area.

    Returns:
        str: The user-inputted code from the text area.
    """

    
    # Dynamically calculate the height based on the number of lines in the input
    num_lines = user_code.count("\n") + 1  # Count the number of lines
    # print(user_code, num_lines)
    dynamic_height = max(68, num_lines * 30)  # Adjust height (min 100px, 20px per line)
    
    # Render the interactive text area with the calculated height
    user_code = st.text_area(
        label="",
        value=user_code,
        height=dynamic_height,
        key=text_area_key
    )
    
    return user_code
