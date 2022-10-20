def get_height(window, height):
    return str((window.winfo_screenheight() - height) // 2)


def get_width(window, width):
    return str((window.winfo_screenwidth() - width) // 2)
