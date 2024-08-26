import tkinter
from os import system
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from fd_converter import get_ffmpeg_cmd, default_ffparams


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Конвертер (by dimnissv)')
        self.form = ttk.Frame(self, padding=10)
        self.form.grid()
        self.video = self.form_element('видео', 0, 'C:/Portable Programs/конвертер/ch_example/video.mkv')
        self.audio = self.form_element('аудио', 1, 'C:/Portable Programs/конвертер/ch_example/audio.flac')
        self.subs = self.form_element('субтитры', 2, 'C:/Portable Programs/конвертер/ch_example/subs.ass')
        self.logo = self.form_element('логотип', 3, 'C:/Portable Programs/конвертер/ch_logos/logo_cr.png')
        self.intro = self.form_element('интро', 4, 'C:/Portable Programs/конвертер/ch_example/video.mkv')
        self.logo_height = self.form_element('высота логотипа', 6, '50', None)
        self.ffmpeg_params = self.form_element('доп параметры ffmpeg', 7, default_ffparams, None)
        self.out = self.form_element('выходной файл', 8, 'C:/Portable Programs/конвертер/ch_example/out.mkv',
                                     fd=asksaveasfilename)

        buttons = ttk.Frame(self, padding=5)
        buttons.grid()
        self.rewrite = tkinter.StringVar(buttons, 'y')
        ttk.Checkbutton(buttons, text='перезаписать файл?', onvalue='y', offvalue='n', variable=self.rewrite
                        ).grid(column=2, row=0)
        self.intro_img = tkinter.BooleanVar(buttons, False)
        ttk.Checkbutton(buttons, text='изображение вместо интро?', variable=self.intro_img).grid(column=3, row=0)
        start_btn = ttk.Button(buttons, text='начать', command=self.start)
        start_btn.grid(column=0, row=0)


    def start(self):
        cmd = get_ffmpeg_cmd(
            *[i.get() for i in (
                self.video, self.audio, self.subs, self.logo, self.intro, self.intro_img, self.logo_height,
                self.ffmpeg_params, self.out, self.rewrite)])
        print(f'Выполняется команда:\n{cmd}')
        system(cmd)
        print('Готово')

    def form_element(self, name: str, row: int = 0, default: str = '', fd=askopenfilename) -> ttk.Entry:
        ttk.Label(self.form, text=name.capitalize() + ':', anchor='e').grid(column=0, row=row)
        el = ttk.Entry(self.form, width=100)
        el.insert(0, default)
        el.grid(column=1, row=row)
        if fd:
            def fd_f():
                el.delete(0, tkinter.END)
                el.insert(0, fd())

            fd_btn = ttk.Button(self.form, text='Выбрать', command=fd_f)
            fd_btn.grid(column=2, row=row)
        return el


def main():
    App().mainloop()


if __name__ == '__main__':
    main()
