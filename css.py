# Custom CSS for hover buttons
import streamlit as st

def css():
    st.markdown("""
    <style>

    # .st-emotion-cache-l1ktzw.em9zgd018 {
    #     visibility: hidden;
    # }
    # .st-emotion-cache-yjrfjy.em9zgd017{
    #     visibility: hidden;
    # }

    # .hover-button {
    #     visibility: hidden;
    #     float: right;
    #     margin-top: -25px; /* Adjust position relative to the cell */
    # }
    # .cell:hover .hover-button {
    #     visibility: visible;
    # }
    # div.stTextArea > div > textarea {
    #     font-size: 25px !important; /* Larger font size */
    #     padding: 10px !important; /* Adjust padding */
    #     line-height: 1.5 !important; /* Adjust line height */
    #     border-radius: 4px !important; /* Optional: Rounded corners */
    # }
    </style>
    """, unsafe_allow_html=True)