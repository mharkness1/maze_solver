from tkinter import Tk, BOTH, Canvas
from WindowClass import WindowClass

def main():
    win = WindowClass(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()