import streamlit as st
import sys
import io
import subprocess

# Initialize session state for cells and shared global state
if "cells" not in st.session_state:
    st.session_state.cells = [{"code": "", "output": ""}]
if "shared_globals" not in st.session_state:
    st.session_state.shared_globals = {}

# Custom CSS for hover buttons
st.markdown("""
<style>
.hover-button {
    visibility: hidden;
    float: right;
    margin-top: -25px; /* Adjust position relative to the cell */
}
.cell:hover .hover-button {
    visibility: visible;
}
div.stTextArea > div > textarea {
    font-size: 25px !important; /* Larger font size */
    padding: 10px !important; /* Adjust padding */
    line-height: 1.5 !important; /* Adjust line height */
    border-radius: 4px !important; /* Optional: Rounded corners */
}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Interactive Problem Solver")
    st.markdown("""
    This app allows you to write Python code in multiple notebook-style cells, run them independently, and view their outputs.
    """)

    # Sidebar for Problem Description
    st.sidebar.header("Problem Description")
    problem_description = """
    Write Python code in multiple cells and execute them independently. Each cell supports its own input and output.
    
    Example Task:
    - Write a function that takes an integer `n` as input and prints "Hello World!" `n` times.
    """
    st.sidebar.markdown(problem_description)

    # Render all cells
    for idx, cell in enumerate(st.session_state.cells):
        # Create a container for each cell
        with st.container():
            st.markdown(f"### Cell {idx + 1}")
            col1, col2 = st.columns([0.95, 0.05])  # Main content and hover button layout

            with col1:
                # Text area for the cell's code
                cell_code = st.text_area(
                    f"Code for Cell {idx + 1}",
                    value=cell["code"],
                    height=68,
                    key=f"code_{idx}"
                )

            with col2:
                # Hover-triggered run button
                if st.button("▶️", key=f"run_{idx}", help="Run this cell"):
                    try:
                        # Redirect stdout to capture the output
                        old_stdout = sys.stdout
                        redirected_output = io.StringIO()
                        sys.stdout = redirected_output

                        # Execute the Python code in the shared global namespace
                        with st.spinner(f"Running Cell {idx + 1}..."):
                            exec(cell_code, st.session_state.shared_globals)

                        # Restore stdout and get the captured output
                        sys.stdout = old_stdout
                        output = redirected_output.getvalue()

                        # Update the cell's code and output in session state
                        st.session_state.cells[idx]["code"] = cell_code
                        st.session_state.cells[idx]["output"] = output.strip() if output.strip() else "No output generated."

                        # Rerun the app to reflect changes
                        st.rerun()

                    except Exception as e:
                        # Restore stdout in case of an error
                        sys.stdout = old_stdout
                        st.session_state.cells[idx]["output"] = f"Error:\n```\n{str(e)}\n```"
                        st.rerun()

            # Display the output of the current cell
            if cell["output"]:
                st.markdown(f"""
                <div style="font-size: 16px; margin-top: 10px;">
                Output for Cell {idx + 1}
                </div>
                """, unsafe_allow_html=True)
                st.code(cell["output"], language="text")

    # Add a button to create a new cell below the last cell
    if st.button("➕ Add New Cell", key="add_cell"):
        st.session_state.cells.append({"code": "", "output": ""})
        st.rerun()

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) > 1 and sys.argv[1] == "run-streamlit":
        # Ensure this block is only executed once
        print("Starting Streamlit server...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", __file__])
        sys.exit(0)  # Exit after starting the Streamlit server
    else:
        # Run the app logic directly (useful for debugging)
        print("Running app logic directly...")
        main()