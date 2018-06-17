import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog, messagebox
from back.painter import Corner, LogoPainter


class LogoPainterGUI(object):
    def __init__(self, master):
        self.command_painter = {
            'logo_path': '',
            'target_path': '',
            'save_to': 'result',
            'corner': Corner.BOTTOM_RIGHT,
            'logo_resize_rate': 0.2
        }
        self.color = {
            'bg': 'azure',
            'botton_bg': 'lavender',
            'active_botton_bg': 'lemon chiffon'
        }
        self.step = 1
        self.master = master
        master.title('Логотипная')  # logoPhotoFactory
        master.geometry('1100x700+500+100')  # width=1000, height=700, x=500, y=100
        master.resizable(True, True)  # the window can be resize horizontally and vertically
        master.protocol('WM_DELETE_WINDOW', master.quit)  # handler close the window
        master.configure(bg=self.color['bg'])

        # self.create_main_menu()
        # self.create_helper()

        self.info_frame = Frame(master,
                                bg=self.color['bg'],
                                height=200)
        self.info_frame.pack(side='top')

        self.step_frame = Frame(master,
                                bg=self.color['bg'])
        self.step_frame.pack(side='top')

        self.create_step_by_step()

    def create_step_by_step(self):
        if self.step == 1:

            # clear the frame to display the logo
            self.clear_frame(self.step_frame)

            welcome_label = Label(self.step_frame,
                                  text='Для начала нужно выбрать логотип',
                                  font=('Helvetica', 14),
                                  bg=self.color['bg'])
            welcome_label.pack()

            logo_button = Button(self.step_frame,
                                 text='Выбрать логотип',
                                 command=self.select_logo,
                                 font=('Helvetica', 14),
                                 bg=self.color['botton_bg'],
                                 activebackground=self.color['active_botton_bg'])
            logo_button.pack(pady=30)

        elif self.step == 2:

            # clear the frame to display the logo
            self.clear_frame(self.step_frame)

            photo_label = Label(self.step_frame,
                                text='Выбери фотографию или папку с фотографиями для логотипа',
                                font=('Helvetica', 14),
                                bg=self.color['bg'])
            photo_label.pack()

            photo_button = Button(self.step_frame,
                                  text='Выбрать фотографию',
                                  command=self.select_photo,
                                  font=('Helvetica', 14),
                                  bg=self.color['botton_bg'],
                                  activebackground=self.color['active_botton_bg'])
            photo_button.pack(side=LEFT,
                              pady=30)

            photos_button = Button(self.step_frame,
                                   text='Выбрать папку с фотографиями',
                                   command=self.select_photos,
                                   font=('Helvetica', 14),
                                   bg=self.color['botton_bg'],
                                   activebackground=self.color['active_botton_bg'])
            photos_button.pack(side=RIGHT,
                              pady=30)

        elif self.step == 3:

            # clear the frame to display the logo
            self.clear_frame(self.step_frame)

            submit_button = Button(self.step_frame,
                                   text='Залоготипить',
                                   command=self.start_logo,
                                   font=('Helvetica', 14),
                                   bg=self.color['botton_bg'],
                                   activebackground=self.color['active_botton_bg'])
            submit_button.pack(pady=30)
    # def create_helper(self):
    #     label_help = Label(self.master,
    #                        text='Что нужно делать?\n '
    #                             '1. Нажать "Начать работать!" -> "Добавить логотип"\n'
    #                             '2. Нажать "Начать работать!" -> "Добавить фото для логотипа или папку для логотипа"\n'
    #                             '3. Нажать "Начать работать!" -> "Залоготипить!"\n',
    #                        font=('Helvetica', 14))
    #     label_help.pack()
    #
    # def create_main_menu(self):
    #     main_menu = Menu(self.master,
    #                      font=('Helvetica', 16))
    #
    #     # 1 submenu
    #     work_menu = Menu(main_menu,
    #                      tearoff=0,
    #                      font=('Helvetica', 16))
    #     work_menu.add_command(label='Добавить логотип',
    #                           command=self.select_logo)
    #     work_menu.add_command(label='Добавить фото для логотипа',
    #                           command=self.select_photo)
    #     work_menu.add_command(label='Добавить папку с фото для логотипа',
    #                           command=self.select_photos)
    #     work_menu.add_separator()
    #
    #     work_menu.add_command(label='Залоготипить!',
    #                           command=self.start_logo)
    #
    #     work_menu.add_separator()
    #
    #     work_menu.add_command(label='Выйти', command=self.master.quit)
    #
    #     # the name of first submenu
    #     main_menu.add_cascade(label='Начать работать!', menu=work_menu)
    #
    #     # 2 submenu
    #     help_menu = Menu(main_menu,
    #                      tearoff=0,
    #                      font=('Helvetica', 16))
    #     help_menu.add_command(label='Спроси кого-нибудь :)')
    #
    #     # the name of second submenu
    #     main_menu.add_cascade(label='Нужна помощь?', menu=help_menu)
    #
    #     self.master.config(menu=main_menu)

    def select_logo(self):
        logo_path = filedialog.askopenfilename(title='Выбери логотип',
                                               filetypes=(('png files', '*.png'),
                                                          ('jpg files', '*.jpg'),
                                                          ('all files', '*.*')))
        # Parameter for LogoPainter
        self.command_painter['logo_path'] = logo_path

        # clear the frame to display the logo
        self.clear_frame(self.info_frame)

        # opening image
        img = PIL.Image.open(logo_path)
        img_min_dim = min(img.width, img.height)

        # resize logo for correct display
        lg = self.get_resized_logo(img, img_min_dim)

        # display the logo in the window
        global logo
        logo = PIL.ImageTk.PhotoImage(lg)
        label_logo = Label(self.info_frame,
                           image=logo,
                           bg=self.color['bg'])
        label_logo.pack(side=LEFT)

        self.step = 2

        self.create_step_by_step()

    def select_photo(self):
        photo_path = filedialog.askopenfilename(title='Выбери фото',
                                                filetypes=(('png files', '*.png'),
                                                           ('jpg files', '*.jpg'),
                                                           ('all files', '*.*')))
        self.command_painter['target_path'] = photo_path

        # clear the frame to display the logo
        self.clear_frame(self.step_frame)

        label_photo = Label(self.info_frame,
                            text='Отлично, теперь я знаю какую фотографию мне нужно брать.\n '
                                 'Теперь можешь нажать "Залоготипить"\n'
                                 'Если что, они находятся вот здесь: ' + photo_path,
                            font=('Helvetica', 14),
                            bg=self.color['bg'])
        label_photo.pack(side=RIGHT)
        print(photo_path)

        self.step = 3

        self.create_step_by_step()

    def select_photos(self):
        photo_path = filedialog.askdirectory(title='Выбери папку')

        self.command_painter['target_path'] = photo_path

        # clear the frame to display the logo
        self.clear_frame(self.step_frame)

        label_photo = Label(self.info_frame,
                            text='Отлично, теперь я знаю какие фотографии мне нужно брать.\n '
                                 'Теперь можешь нажать "Залоготипить"\n'
                                 'Если что, они находятся вот здесь: ' + photo_path,
                            font=('Helvetica', 14),
                            bg=self.color['bg'])
        label_photo.pack(side=RIGHT)
        print(photo_path)

        self.step = 3

        self.create_step_by_step()

    def get_resized_logo(self, logo, img_min_dim):
        logo_min_dim = min(logo.width, logo.height)

        related_resize_rate = img_min_dim * self.command_painter['logo_resize_rate'] / logo_min_dim
        new_width = int(logo.width * related_resize_rate)
        new_height = int(logo.height * related_resize_rate)

        return logo.resize((new_width, new_height))

    # run painter if all parameters exists
    def start_logo(self):
        if self.command_painter['logo_path'] and self.command_painter['target_path']:
            LogoPainter(logo_path=self.command_painter['logo_path'],
                        target_path=self.command_painter['target_path'],
                        save_to_path=self.command_painter['save_to'],
                        corner=self.command_painter['corner']
                        ).process_all()
            self.command_painter = {
                'logo_path': '',
                'target_path': '',
                'save_to': 'result',
                'corner': Corner.BOTTOM_RIGHT,
                'logo_resize_rate': 0.2
            }
        else:
            messagebox.showerror('Введены не все данные',
                                 'Пожалуйста, укажите логотип и файлы для логотипа')

    # Clears the frame of all the objects
    @staticmethod
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()



if __name__ == '__main__':
    root = Tk()
    gui = LogoPainterGUI(root)
    root.mainloop()
