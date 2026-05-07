import FreeSimpleGUI as gg
import func

label = gg.Text("Type in a to-do")
input_box = gg.InputText(tooltip="Enter todo", key="todo")

add_button = gg.Button("Add")

list_box = gg.Listbox(
    values=func.get_todo(),
    key='todos',
    enable_events=True,
    size=(45, 10)
)

edit_button = gg.Button("Edit")

window = gg.Window(
    "My To-Do APP",
    layout=[
        [label],
        [input_box, add_button],
        [list_box, edit_button]
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = func.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            func.write_todo(todos)

            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Edit":
            try:
                selected = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = func.get_todo()
                index = todos.index(selected)
                todos[index] = new_todo

                func.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                gg.popup("Please select a todo first")

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case gg.WIN_CLOSED:
            break

window.close()