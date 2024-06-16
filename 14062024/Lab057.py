def allowed_to_attend_python_class(name):
    match name:
        case "DELL":
            print("DELL is allowed")
        case "Sourav":
            print("Sourav is allowed")
        case "Sangita":
            print("Sangita is allowed")
        case _:
            print("No one is allowed")


allowed_to_attend_python_class("Rahul")
