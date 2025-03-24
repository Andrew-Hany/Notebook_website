import streamlit as st
import sys
import io
import subprocess
import matplotlib.pyplot as plt
import json
import inspect
from css import *
from cell import cell_component
import random
import numpy as np

# Set the seed for random and numpy
random.seed(42)
np.random.seed(42)
def main():
    if "solution_flag" not in st.session_state:
        st.session_state.solution_flag = 0
    if "sub_page" not in st.session_state:
        st.session_state.sub_page = "notebook"
    if "selected_problem" not in st.session_state:
        st.error("No problem selected. Please go back to the home page and select a problem.")
        return
    # if solution_flag in st.session_state:

    if  "cells" not in st.session_state:
        st.session_state.cells = [{"code": "", "output": "", "plot": None}]
    if "shared_globals" not in st.session_state:
        st.session_state.shared_globals = {}
    problem = st.session_state.selected_problem

    st.title(problem["name"])
    st.markdown(problem["description"])

    # st.sidebar.header("Problem Description")
    # st.sidebar.markdown(problem["description"])

    if st.session_state.solution_flag == 1:
        st.header("Solution")
        st.code(problem["right_solution"])
    elif st.session_state.sub_page == "notebook":
        Notebook()
        if st.sidebar.button("🔍 Run Tests", key="run_test_page"):
            st.session_state.sub_page = "testing"
            st.rerun()
    elif st.session_state.sub_page == "testing":
        passed, failed, results = test( problem["test_cases"])

        if failed> 0:
            st.error(f"Passed: {passed}, Failed: {failed}")
            # st.sidebar.error(f"Passed: {passed}, Failed: {failed}")    
        elif passed == len(problem["test_cases"]):
            st.success(f"Passed: {passed}, Failed: {failed}")
            # st.sidebar.success("All tests passed!")
        
        if st.sidebar.button("📝 Notebook", key="notebook"):
            st.session_state.sub_page = "notebook"
            st.rerun()
            
        

    if st.sidebar.button("🔙 Go Back", key="go_back"):
        del st.session_state.selected_problem
        del st.session_state.solution_flag
        del st.session_state.user_test_code
        # del st.session_state.cells
        # del st.session_state.shared_globals

        st.rerun()
                
def test(test_cases):

    if 'user_test_code' not in st.session_state:
        st.session_state.user_test_code = st.session_state.selected_problem["starting_code"]
    user_solution_code = cell_component(st.session_state.user_test_code, 'user_solution')

    passed = 0
    failed = 0
    results = []

    if st.button("✅ Run Tests", key="run_tests"):
        st.session_state.user_test_code= user_solution_code
        
        try:
            exec(user_solution_code, st.session_state.shared_globals)
            exec(st.session_state.selected_problem["right_solution"], st.session_state.shared_globals)
            func = st.session_state.shared_globals.get("solution")
            solition_func = st.session_state.shared_globals.get("right_solution")

            for case in test_cases:
                print(func(case["input"]), solition_func(case["input"]))
                print(func(case["input"]))
                print(case)
                try:
                    # Assuming the user-defined function is named 'solution'
                    func = st.session_state.shared_globals.get("solution")
                    solition_func = st.session_state.shared_globals.get("right_solution")
                    # print(func(case["input"]))
                    if func:
                        random.seed(42)
                        np.random.seed(42)
                        result =  func(case["input"])

                        random.seed(42)
                        np.random.seed(42)
                        right_result = solition_func(case["input"])
                        print(result, right_result)
                        if result == right_result:
                            passed += 1
                            results.append((case, "Passed"))
                        else:
                            failed += 1
                            results.append((case, "Failed"))
                    else:
                        st.error("No function named 'solution' found in the provided code.")
                        break
                except Exception as e:
                    failed += 1
                    results.append((case, f"Error: {str(e)}"))
        except Exception as e:
            st.error(f"Error executing user solution: {str(e)}")

    return passed, failed, results
def Notebook():
    # Render all cells
    for idx, cell in enumerate(st.session_state.cells):
        with st.container():
            col1, col2 = st.columns([0.95, 0.05])

            with col1:
                # Create a unique key for the text area
                text_area_key = f"code_{idx}"
                
                # Retrieve the current value of the text area (if it exists)
                user_code = st.session_state.cells[idx]['code']
                cell_code = cell_component(user_code, text_area_key)

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