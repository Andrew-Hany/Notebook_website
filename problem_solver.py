import streamlit as st
import sys
import io
import subprocess
import matplotlib.pyplot as plt

from css import *
from cell import cell_component

# Run CSS
css()

# Initialize session state for cells and shared global state
if "cells" not in st.session_state:
    st.session_state.cells = [{"code": "", "output": "", "plot": None}]
if "shared_globals" not in st.session_state:
    st.session_state.shared_globals = {}

def main():
    if "selected_problem" not in st.session_state:
        st.error("No problem selected. Please go back to the home page and select a problem.")
        return

    problem = st.session_state.selected_problem

    st.title(problem["name"])
    st.markdown(problem["description"])

    st.sidebar.header("Problem Description")
    st.sidebar.markdown(problem["description"])

    if st.sidebar.button("🔙 Go Back", key="go_back"):
        del st.session_state.selected_problem
        st.rerun()
    

    # Render all cells
    for idx, cell in enumerate(st.session_state.cells):
        with st.container():
            col1, col2 = st.columns([0.95, 0.05])

            with col1:
                cell_code = cell_component(idx)

            with col2:
                if st.button("▶️", key=f"run_{idx}", help="Run this cell"):
                    try:
                        old_stdout = sys.stdout
                        redirected_output = io.StringIO()
                        sys.stdout = redirected_output

                        plot_buffer = io.BytesIO()

                        with st.spinner(f"Running Cell {idx + 1}..."):
                            exec(cell_code, st.session_state.shared_globals)

                        sys.stdout = old_stdout
                        output = redirected_output.getvalue()

                        if plt.get_fignums():
                            fig = plt.gcf()
                            fig.savefig(plot_buffer, format="png")
                            plot_buffer.seek(0)
                            st.session_state.cells[idx]["plot"] = plot_buffer
                            plt.close(fig)
                        else:
                            st.session_state.cells[idx]["plot"] = None

                        st.session_state.cells[idx]["code"] = cell_code
                        st.session_state.cells[idx]["output"] = output.strip() if output.strip() else ""

                        st.rerun()

                    except Exception as e:
                        sys.stdout = old_stdout
                        st.session_state.cells[idx]["output"] = f"Error:\n```\n{str(e)}\n```"
                        st.session_state.cells[idx]["plot"] = None
                        st.rerun()

            if cell["output"]:
                st.text(cell["output"])

            if cell["plot"]:
                st.image(cell["plot"])

    if st.button("➕ Add New Cell", key="add_cell"):
        st.session_state.cells.append({"code": "", "output": "", "plot": None})
        st.rerun()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run-streamlit":
        print("Starting Streamlit server...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", __file__])
        sys.exit(0)
    else:
        print("Running app logic directly...")
        main()