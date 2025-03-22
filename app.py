import streamlit as st
import sys
import io
import subprocess
import matplotlib.pyplot as plt
import json

import problem_solver
from css import *

# Run CSS
css()


def load_problems():
    with open('problems.json', 'r') as f:
        return json.load(f)

def main():
    if "selected_problem" not in st.session_state:
        problem_flag = 0

    else:
        problem_flag = 1

    if problem_flag == 0:

        st.title("Problem List")
        problems = load_problems()


        for problem in problems:
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button(problem["name"], key=problem["id"]):
                    st.session_state.selected_problem = problem
                    st.rerun()

            with col2:
                st.button("Solution", key=f'solution_{problem["id"]}')
                    # st.session_state.selected_problem = problem

                    # st.rerun()

    else:
        problem_solver.main()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run-streamlit":
        print("Starting Streamlit server...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", __file__])
        sys.exit(0)
    else:
        print("Running app logic directly...")
        main()