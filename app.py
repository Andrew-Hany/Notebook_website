import streamlit as st
import sys
import io
import subprocess
import matplotlib.pyplot as plt
import json

import problem_solver

from convert_problems_to_json import *
from css import *

# Run CSS
css()


def load_courses():
    # if 'load_course_flag' not in st.session_state:
    #     base_path = 'problems'
    #     output_file = 'problems.json'
    #     problems_data = convert_problems_to_json(base_path)
    #     save_json(problems_data, output_file)
    #     st.session_state.load_course_flag = 1
    #     print(f"Problems data saved to {output_file}")
    with open('problems.json', 'r') as f:
        return json.load(f)

def main():
    if "selected_problem" not in st.session_state:
        problem_flag = 0

    else:
        problem_flag = 1

    if problem_flag == 0:

        st.title("Problem List")
        courses = load_courses()

        for course_name, topics in courses.items():
            st.info(course_name)
            for topic_name, problems in topics.items():
                col1, col2 = st.columns([9,1])
                with col1:
                    st.warning(topic_name)
                with col2:
                    st.button("learn", key=topic_name)
                # print(topic_name,course_name)
                for problem in problems:
                    col1,col2,col3,col4,col5 = st.columns([2,2,1,1, 1.5])
                    with col1:
                        if st.button(problem["name"], key=problem["id"]):
                            st.session_state.selected_problem = problem
                            st.rerun()
                    with col3:
                        if st.button("solution", key=f'solution_{problem["id"]}'):
                            st.session_state.selected_problem = problem
                            st.session_state.solution_flag = 1
                            st.rerun()
                    with col2: 
                        if st.button("step by step solution", key=f'step_by_step_solution_{problem["id"]}'):
                            st.session_state.selected_problem = problem
                            st.session_state.solution_flag = 2
                            st.rerun()
                    with col4:
                        if st.button("learn", key=f'learn_topic_beforehand_{problem["id"]}'):
                            st.session_state.selected_problem = problem
                            st.session_state.learn = 1
                            st.rerun()
                    with col5:
                        if problem["severity"] == "easy":
                            st.success(f"easy")
                        elif problem["severity"] == "medium":
                            st.warning(f"medium")
                        else:
                            st.error(f"hard")
               

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