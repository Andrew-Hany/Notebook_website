import streamlit as st
import sys
import io
import subprocess
import matplotlib.pyplot as plt

from css import *
from cell import cell_component
#run CSS
css()


# Initialize session state for cells and shared global state
if "cells" not in st.session_state:
    st.session_state.cells = [{"code": "", "output": "", "plot": None}]
if "shared_globals" not in st.session_state:
    st.session_state.shared_globals = {}




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
            # st.markdown(f"### Cell {idx + 1}")
            col1, col2 = st.columns([0.95, 0.05])  # Main content and hover button layout

            with col1:
                # Text area for the cell's code
                cell_code = cell_component(idx)

            with col2:
                # Hover-triggered run button
               if st.button("▶️", key=f"run_{idx}", help="Run this cell"):
                    try:
                        # Redirect stdout to capture the output
                        old_stdout = sys.stdout
                        redirected_output = io.StringIO()
                        sys.stdout = redirected_output

                        # Create a buffer to capture matplotlib plots
                        plot_buffer = io.BytesIO()

                        # Execute the Python code in the shared global namespace
                        with st.spinner(f"Running Cell {idx + 1}..."):
                            exec(cell_code, st.session_state.shared_globals)

                        # Restore stdout and get the captured output
                        sys.stdout = old_stdout
                        output = redirected_output.getvalue()

                        # Check if a matplotlib figure was created
                        if plt.get_fignums():  # If there are active figures
                            fig = plt.gcf()  # Get the current figure
                            fig.savefig(plot_buffer, format="png")  # Save the figure to the buffer
                            plot_buffer.seek(0)  # Rewind the buffer to the beginning
                            st.session_state.cells[idx]["plot"] = plot_buffer  # Store the plot in session state
                            plt.close(fig)  # Close the figure to free up memory
                        else:
                            st.session_state.cells[idx]["plot"] = None  # No plot was generated

                        # Update the cell's code and output in session state
                        st.session_state.cells[idx]["code"] = cell_code
                        st.session_state.cells[idx]["output"] = output.strip() if output.strip() else ""

                        # Rerun the app to reflect changes
                        st.rerun()

                    except Exception as e:
                        # Restore stdout in case of an error
                        sys.stdout = old_stdout
                        st.session_state.cells[idx]["output"] = f"Error:\n```\n{str(e)}\n```"
                        st.session_state.cells[idx]["plot"] = None  # Ensure no plot is stored on error
                        st.rerun()

            if cell["output"]:
                st.text(cell["output"])  # Use st.text() for plain text output

            # Display the plot of the current cell (if any)
            if cell["plot"]:

                st.image(cell["plot"])  # Use st.image() to display the plot

    # Add a button to create a new cell below the last cell
    if st.button("➕ Add New Cell", key="add_cell"):
        st.session_state.cells.append({"code": "", "output": "", "plot": None})
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
