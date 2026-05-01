from voting import *

def main() -> None:
    """
    Function launches GUI
    """
    window = Tk()
    window.title('Project 1')
    window.geometry('350x400')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()