import streamlit as st
import func

todos = func.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todo(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("Hii")

for i, t in enumerate(todos):

    checkbox = st.checkbox(
        t,
        key=f"todo_{i}"
    )

    if checkbox:
        todos.pop(i)
        func.write_todo(todos)

        del st.session_state[f"todo_{i}"]

        st.rerun()

st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)