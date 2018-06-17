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

        # frame for information about process
        self.info_frame = Frame(master,
                                bg=self.color['bg'],
                                height=200)
        self.info_frame.pack(side='top')

        # create frame for user
        self.step_frame = Frame(master,
                                bg=self.color['bg'])
        self.step_frame.pack(side='top')

        # create frame for opportunities to go back
        self.back_frame = Frame(master,
                                bg=self.color['bg'])
        self.back_frame.pack(side='bottom')

    def step_one(self):

        # clear the frame to display
        self.clear_frame(self.info_frame)
        self.clear_frame(self.step_frame)
        self.clear_frame(self.back_frame)

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

    def step_two(self):

        # clear the frame to display
        self.clear_frame(self.info_frame)
        self.clear_frame(self.step_frame)
        self.clear_frame(self.back_frame)

        self.paint_logo()

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

        back_button = Button(self.back_frame,
                             text='Предыдущий шаг',
                             command=self.step_one,
                             font=('Helvetica', 14),
                             bg=self.color['botton_bg'],
                             activebackground=self.color['active_botton_bg'])
        back_button.pack(side=LEFT,
                         anchor=W)

    def step_three(self, target_path):

        # clear the frame to display the logo
        self.clear_frame(self.info_frame)
        self.clear_frame(self.step_frame)
        self.clear_frame(self.back_frame)

        self.paint_logo()

        label_photo = Label(self.info_frame,
                            text='Отлично, теперь я знаю какую фотографию мне нужно брать.\n '
                                 'Теперь можешь нажать "Залоготипить"\n'
                                 'Если что, они находятся вот здесь: ' + target_path,
                            font=('Helvetica', 14),
                            bg=self.color['bg'])
        label_photo.pack(side=RIGHT)

        submit_button = Button(self.step_frame,
                               text='Залоготипить',
                               command=self.start_logo,
                               font=('Helvetica', 14),
                               bg=self.color['botton_bg'],
                               activebackground=self.color['active_botton_bg'])
        submit_button.pack(pady=30)

        back_button = Button(self.back_frame,
                             text='Предыдущий шаг',
                             command=self.step_two,
                             font=('Helvetica', 14),
                             bg=self.color['botton_bg'],
                             activebackground=self.color['active_botton_bg'])
        back_button.pack(side=LEFT,
                         anchor=W)

    def select_logo(self):
        logo_path = filedialog.askopenfilename(title='Выбери логотип',
                                               filetypes=(('png files', '*.png'),
                                                          ('jpg files', '*.jpg'),
                                                          ('all files', '*.*')))
        if logo_path:
            # Parameter for LogoPainter
            self.command_painter['logo_path'] = logo_path

            self.step_two()

    def select_photo(self):
        photo_path = filedialog.askopenfilename(title='Выбери фото',
                                                filetypes=(('png files', '*.png'),
                                                           ('jpg files', '*.jpg'),
                                                           ('all files', '*.*')))
        if photo_path:
            # Parameter for LogoPainter
            self.command_painter['target_path'] = photo_path

            self.step_three(photo_path)

    def select_photos(self):
        photos_path = filedialog.askdirectory(title='Выбери папку')

        if photos_path:
            # Parameter for LogoPainter
            self.command_painter['target_path'] = photos_path

            self.step_three(photos_path)

    def get_resized_logo(self, logo, img_min_dim):
        logo_min_dim = min(logo.width, logo.height)

        related_resize_rate = img_min_dim * self.command_painter['logo_resize_rate'] / logo_min_dim
        new_width = int(logo.width * related_resize_rate)
        new_height = int(logo.height * related_resize_rate)

        return logo.resize((new_width, new_height))

    def paint_logo(self):
        # opening image
        img = PIL.Image.open(self.command_painter['logo_path'])
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

    # main method
    def create_ui(self):
        self.step_one()

    # Clears the frame of all the objects
    @staticmethod
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    root = Tk()
    LogoPainterGUI(root).create_ui()
    root.mainloop()
