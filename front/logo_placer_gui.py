from tkinter import *
from tkinter import filedialog, ttk, font
from painter import Corner, LogoPainter


class LogoPainterGUI(object):
    def __init__(self, master):
        self.master = master
        master.title('Логотипная')  # logoPhotoFactory
        master.geometry('800x600+500+200')  # width=800, height=600, x=500, y=200
        master.resizable(True, True)  # the window can be resize horizontally and vertically
        master.protocol('WM_DELETE_WINDOW', master.quit)  # handler close the window

        main_menu = Menu(master,
                         font=('Helvetica', 16))

        # 1 submenu
        work_menu = Menu(main_menu,
                         tearoff=0,
                         font=('Helvetica',16))
        work_menu.add_command(label='Добавить логотип',
                              command=self.select_logo)
        work_menu.add_command(label='Добавить фото для логотипа',
                              command=self.select_photo)
        work_menu.add_command(label='Добавить папку с фото для логотипа',
                              command=self.select_photos)

        work_menu.add_separator()

        work_menu.add_command(label='Выйти', command=master.quit)

        # the name of first submenu
        main_menu.add_cascade(label='Начать работать!', menu=work_menu)

        # 2 submenu
        help_menu = Menu(main_menu,
                         tearoff=0,
                         font=('Helvetica',16))
        help_menu.add_command(label='Спроси кого-нибудь :)')

        # the name of second submenu
        main_menu.add_cascade(label='Нужна помощь?', menu=help_menu)

        master.config(menu=main_menu)

    def select_logo(self):
        logo_path = filedialog.askopenfilename(title='Выбери логотип',
                                               filetypes=(('png files', '*.png'),
                                                          ('jpeg files', '*.jpg'),
                                                          ('all files', '*.*')))
        logo = PhotoImage(file=logo_path)
        label1 = Label(self.master, text='lal')
        label1.pack()

    @staticmethod
    def select_photos():
        directory = filedialog.askdirectory(title='Выбери папку')
        print(directory)

    @staticmethod
    def select_photo():
        directory = filedialog.askopenfilename(title='Выбери фото')
        print(directory)


if __name__ == '__main__':
    root = Tk()
    gui = LogoPainterGUI(root)
    root.mainloop()
