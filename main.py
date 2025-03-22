import streamlit as st

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Problem Solver"])

    if page == "Home":
        import home
        home.main()
    elif page == "Problem Solver":
        import problem_solver
        problem_solver.main()

if __name__ == "__main__":
    main()