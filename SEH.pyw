# -*- coding: utf8 -*-
import smtplib
from datetime import *
from email.header import Header
from email.mime.text import MIMEText
from tkinter import *
from tkinter.ttk import Treeview


def mail_base():
    global data_base_mail
    data_base_mail = []
    file_mail = open('data/Почта_пользователя.txt', mode='r', encoding='utf-8')
    for line in file_mail:
        if line != '\n':
            data_base_mail.append(line)
    file_mail.close()

def o_program():
    main_window.title('Система развития человека/О программе')
    button_lekarstva.config(fg=fg_color_button, bg=bg_color_button)
    button_yprajneniya.config(fg=fg_color_button, bg=bg_color_button)
    button_o_programe.config(fg=bg_color_button, bg=fg_color_button, activebackground=bg_color_button,
                             activeforeground=fg_color_button)
    button_rejim_priem.config(fg=fg_color_button, bg=bg_color_button)
    clearFrame()
    o_proge = Frame(frame_display)
    o_proge.place(x=40, y=150)
    Label(o_proge, text='Разработчик: _\n'
                        'Консультант: _\n'
                        'Научный руководитель: _\n'
                        'Факультет: Цифровых Технологий и Кибербезоапаности\n'
                        'Направление: ДИТ-11\n'
                        'Пользуясь данной программой вы\n соглашаетесь с обработкой данных\n'
                        'Дата создания: 29.05.2021', font='Times 15', background="white").pack()


def clearFrame():
    for widget in frame_display.winfo_children():
        widget.destroy()


def isu():
    def delete_isu():
        isu_win.destroy()

    isu_win = Toplevel(main_window, background="white")
    isu_win.title('Ошибка')
    isu_win.geometry('300x90')
    isu_win.resizable(False, False)
    Label(isu_win, text='Ошибка, вы ничего не выбрали!', font='Times 15', background="white").place(x=10, y=10)
    Button(isu_win, text='Ок', font='Times 15', width=10, command=delete_isu, fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button).place(x=80, y=40)


def nootrops():
    clearFrame()
    button_lekarstva.config(fg=bg_color_button, bg=fg_color_button, activebackground=bg_color_button,
                            activeforeground=fg_color_button)
    button_yprajneniya.config(fg=fg_color_button, bg=bg_color_button)
    button_o_programe.config(fg=fg_color_button, bg=bg_color_button)
    button_rejim_priem.config(fg=fg_color_button, bg=bg_color_button)
    main_window.title('Система развития человека/Ноотропы')

    def dring_some_med():
        try:
            global drinking_data
            drinking_data = []
            line1 = tabel1.focus()
            elem_line = tabel1.item(line1)['values'][0]
            file = open('Data/Лекарства_на_курсе.txt', mode='a', encoding='utf-8')
            for line in data_base:
                if elem_line in line:
                    line = line.split(' | ')
                    line_split = line[3].split(':')
                    date_now = date.today() + timedelta(days=int(line_split[1][0:len(line_split[1]) - 1]))
                    date_now = date_now.strftime("%d.%m.%Y")
                    # print(date_now)
                    add_string = elem_line + ' | ' + 'Курс:' + line_split[1].replace('\n',
                                                                                     '') + ' | ' + 'Начало: ' + str(
                        date.today().strftime("%d.%m.%Y")) + ' | ' + 'Конец: ' + str(date_now) + '\n'
                    # print(add_string)
                    file.write(add_string)
                    drinking_data.append(add_string)
            # print(elem_line)
            file.close()
        except:
            isu()

    def del_func():  # Удаление элемента
        try:
            del_line = tabel1.focus()
            name_to_del = tabel1.item(del_line)['values'][0]
            if name_to_del != '':
                new_med = open('Data/Ноотропы.txt', mode='w', encoding='utf-8')
                for elem in range(len(data_base)):
                    if str(name_to_del) in data_base[elem]:
                        data_base[elem] = '\n'
                        new_med.write(data_base[elem])
                    else:
                        new_med.write((data_base[elem]))
                new_med.close()
                nootrops()
        except:
            isu()

    def edit_func():  # Редактирование элемента
        try:
            def edit():
                for l in range(len(data_base)):
                    if l == k:
                        if str(input1.get()) != '' and 0 < int(input2.get()) < 100 and 0 < int(input3.get()) < 10000 and str(input4.get())[0] not in '0987654321' and 0 < int(input5.get()) < 1000:
                            EditedLine = 'Название: ' + input1.get() + ' | ' + 'Дозировка: ' + input2.get() + ' т. ' + 'по ' + input3.get() + ' мг' + ' | ' + 'Категория: ' + input4.get() + ' | ' + 'Курс: ' + input5.get() + '\n'
                            data_base[l] = EditedLine
                        else:
                            Isue = Toplevel(edit_win)
                            Isue.title('Ошибка')
                            Label(Isue, text='Пожалуйста, заполните все поля!', font='Times 15').pack()
                            Button(Isue, text='Ок', font='Times 15', bg=bg_color_button, fg=fg_color_button,
                                   command=lambda: Isue.destroy()).pack()
                edit_file = open('Data/Ноотропы.txt', mode='w', encoding='utf-8')
                for h in data_base:
                    edit_file.write(h)
                edit_file.close()
                nootrops()

            edit_line = tabel1.focus()
            line_to_edit = tabel1.item(edit_line)['values'][0]
            new_med = open('Data/Ноотропы.txt', mode='r', encoding='utf-8')
            edit_win = Toplevel(main_window, background="white")
            edit_win.geometry('255x245')
            edit_win.geometry('+250+300')
            edit_win.resizable(False, False)
            edit_win.title('Редактировать препарат')
            Label(edit_win, text='Название:', font='Times 15', background="white").place(x=85, y=0)
            Label(edit_win, text='Дозировка:', font='Times 15', background="white").place(x=85, y=50)
            Label(edit_win, text='Категория:', font='Times 15', background="white").place(x=85, y=100)
            Label(edit_win, text='Длительность курса в днях:', font='Times 15', background="white").place(x=15, y=150)
            Label(edit_win, text='таблетки', font='Times 15', background="white").place(x=80, y=75)
            Label(edit_win, text='мг.', font='Times 15', background="white").place(x=200, y=77)
            input1 = Entry(edit_win)
            input1.insert(0, tabel1.item(edit_line)['values'][0])
            input1.place(x=68, y=30)
            input2 = Entry(edit_win, width=5)
            input2_in = tabel1.item(edit_line)['values'][1].split(' ')
            input2.insert(0, input2_in[0])
            input2.place(x=43, y=77)
            input3 = Entry(edit_win, width=5)
            input2_in = tabel1.item(edit_line)['values'][1].split(' ')
            input3.insert(0, input2_in[3])
            input3.place(x=162, y=77)
            input4 = Entry(edit_win)
            input4.insert(0, tabel1.item(edit_line)['values'][2])
            input4.place(x=68, y=130)
            input5 = Entry(edit_win)
            input5.place(x=68, y=180)
            Button(edit_win, text='Подтвердить', font='Times 15', width=15, command=edit, fg=fg_color_button,
                   bg=bg_color_button).place(x=40, y=200)
            for elem in range(len(data_base)):
                if str(line_to_edit) in data_base[elem]:
                    k = elem
                    need_line = data_base[elem].split(' | ')
            need_line = need_line[3].split(' ')
            need_line = need_line[1]
            input5.insert(0, need_line)
            new_med.close()
        except:
            isu()

    def sort_func():  # Сортировка
        try:
            Line = filtr.get(filtr.curselection())
            print(Line)
            if Line == 'Все':
                nootrops()
            else:
                tabel1.delete(*tabel1.get_children())
                for elem_in_data_base in data_base:
                    if Line in elem_in_data_base:
                        elem_in_data_base = elem_in_data_base.split(' | ')
                        name = elem_in_data_base[0].split(': ')
                        dose = elem_in_data_base[1].split(': ')
                        for_what = elem_in_data_base[2].split(': ')
                        tabel1.insert('', 'end', values=(name[1], dose[1], for_what[1]))
        except:
            isu()

    array_data()

    add_button = Button(frame_display, compound='l', image=img_add, text='Добавить\nпрепарат', command=add_func,
                        height=95, font='Times 15', fg=fg_color_button, bg=bg_color_button,
                        activebackground=fg_color_button, activeforeground=bg_color_button)
    add_button.grid(row=0, column=0, sticky='news')
    del_button2 = Button(frame_display, compound='l', image=img_delete, text='Удалить\n препарат', command=del_func,
                         height=95, font='Times 15', fg=fg_color_button, bg=bg_color_button,
                         activebackground=fg_color_button, activeforeground=bg_color_button)
    del_button2.grid(row=0, column=1, sticky='news')
    edit_button = Button(frame_display, compound='l', image=img_edit, text='Редактировать \n препарат',
                         command=edit_func, height=95, font='Times 15', fg=fg_color_button, bg=bg_color_button,
                         activebackground=fg_color_button, activeforeground=bg_color_button)
    edit_button.grid(row=0, column=2, sticky='news')

    tabel1 = Treeview(frame_display)
    tabel1.grid(row=1, column=0, columnspan=3)
    scroll = Scrollbar(frame_display, command=tabel1.yview)
    scroll.place(x=585, y=106, height=221)
    tabel1.config(yscrollcommand=scroll.set)
    tabel1['show'] = 'headings'
    tabel1['columns'] = ('1', '2', '3')
    tabel1.column("1", width=200, minwidth=50)
    tabel1.heading('1', text='Название')
    tabel1.column("2", width=200, minwidth=50)
    tabel1.heading('2', text='Дозировка')
    tabel1.column("3", width=200, minwidth=50)
    tabel1.heading('3', text='Категория')
    for line in data_base:
        line = line.split(' | ')
        name = line[0].split(': ')
        dose = line[1].split(': ')
        for_what = line[2].split(': ')
        tabel1.insert('', 'end', values=(name[1], dose[1], for_what[1]))

    drink_med = Button(frame_display, compound='l', image=img_clock, text='Начать пить\n добавки',
                       font='Times 15', height=78, command=dring_some_med,
                       fg=fg_color_button, bg=bg_color_button,
                       activebackground=fg_color_button, activeforeground=bg_color_button)
    drink_med.grid(row=2, column=0, sticky='nesw')

    sort = Button(frame_display, compound='l', image=img_sort, text='Сортировать\n по категории',
                  font='Times 15', height=82, command=sort_func,
                  fg=fg_color_button, bg=bg_color_button,
                  activebackground=fg_color_button, activeforeground=bg_color_button)
    sort.grid(row=2, column=1, sticky='nesw')

    categories = []
    for elem_data_base in data_base:
        elem_data_base = elem_data_base.split(' | ')
        ElemInElem = elem_data_base[2].split(': ')
        if ElemInElem[1] not in categories:
            categories.append(ElemInElem[1])
    # print(categories)
    filtr = Listbox(frame_display, selectmode=SINGLE, height=4)
    filtr.insert(END, 'Все')
    for add in categories:
        filtr.insert(END, add)
    filtr.grid(row=2, column=2, sticky='nesw')

    scroll_filtr = Scrollbar(frame_display, command=filtr.yview)
    scroll_filtr.place(x=585, y=334, height=87)
    filtr.config(yscrollcommand=scroll_filtr.set)


def add_func():
    def add_to_file():
        if input_add_name.get() != '' or input_add_dose.get() != '' or input_add_dose2.get() != '' or input_days.get() != '' or input_for_what.get() != '':
            med = open('Data/Ноотропы.txt', encoding='utf-8', mode='a')
            add_elem = 'Название: ' + input_add_name.get() + ' | ' + 'Дозировка: ' + input_add_dose.get() + ' т. ' + 'по ' + input_add_dose2.get() + ' мг' + ' | ' + 'Категория: ' + input_for_what.get() + ' | ' + 'Курс: ' + input_days.get() + '\n'
            med.write(add_elem)
            med.close()
            nootrops()
        else:
            Isue = Toplevel(add_win, background="white")
            Isue.title('Ошибка')
            Label(Isue, text='Пожалуйста, заполните все поля!', font='Times 15', background="white").pack()
            Button(Isue, text='Ок', font='Times 15', bg=bg_color_button, fg=fg_color_button,
                   command=lambda: Isue.destroy()).pack()

            nootrops()

    add_win = Toplevel(main_window, background="white")
    add_win.geometry('255x245')
    add_win.geometry('+250+300')
    add_win.resizable(False, False)
    add_win.title('Добавить препарат')
    Label(add_win, text='Название:', font='Times 15', background="white").place(x=85, y=0)
    Label(add_win, text='Дозировка:', font='Times 15', background="white").place(x=85, y=50)
    Label(add_win, text='Категория:', font='Times 15', background="white").place(x=85, y=100)
    Label(add_win, text='Длительность курса в днях:', font='Times 15', background="white").place(x=15, y=150)
    Label(add_win, text='таблетки', font='Times 15', background="white").place(x=80, y=75)
    Label(add_win, text='мг.', font='Times 15', background="white").place(x=200, y=77)
    input_add_name = Entry(add_win)
    input_add_name.place(x=68, y=30)
    input_add_dose = Entry(add_win, width=5)
    input_add_dose.place(x=43, y=77)
    input_add_dose2 = Entry(add_win, width=5)
    input_add_dose2.place(x=162, y=77)
    input_for_what = Entry(add_win)
    input_for_what.place(x=68, y=130)
    input_days = Entry(add_win)
    input_days.place(x=68, y=180)
    add_button2 = Button(add_win, text='Подтвердить', font='Times 15', width=15, command=add_to_file,
                         fg=fg_color_button, bg=bg_color_button).place(x=40, y=200)


def drinking_win():
    main_window.title('Система развития человека/Режим приема')
    button_lekarstva.config(fg=fg_color_button, bg=bg_color_button)
    button_yprajneniya.config(fg=fg_color_button, bg=bg_color_button)
    button_o_programe.config(fg=fg_color_button, bg=bg_color_button)
    button_rejim_priem.config(fg=bg_color_button, bg=fg_color_button, activebackground=bg_color_button,
                              activeforeground=fg_color_button)

    def edit_mail():
        def accept_mail():
            if '@' in input_mail.get():
                file_mail_2 = open('data/Почта_пользователя.txt', mode='w', encoding='utf-8')
                file_mail_2.write(input_mail.get())
                file_mail_2.close()
                edit_mail_win.destroy()
            else:
                error = Toplevel(edit_mail_win, background='white')
                error.geometry('340x85')
                Label(error, text='\nОшибка. Введите коректную почту', font='Times 15', background='white').pack()
        mail_base()
        edit_mail_win = Toplevel(main_window, background='white')
        edit_mail_win.geometry('400x115')
        edit_mail_win.resizable(False, False)
        edit_mail_win.title('Редактирование почты')
        Label(edit_mail_win, text='Введите или измените почту:', font='Times 15', background='white').place(x=40, y=10)
        input_mail = Entry(edit_mail_win, width=40)
        input_mail.place(x=90, y=40)
        if len(data_base_mail) > 0:
            input_mail.insert(0, data_base_mail[0])
        but1 = Button(edit_mail_win, text='Подтвердить', width=25, font='Times 15', command=accept_mail, fg=fg_color_button, bg=bg_color_button, activebackground=fg_color_button, activeforeground=bg_color_button)
        but1.place(x=70, y=65)



    def del_func():  # Удаление элемента
        try:
            del_line = tabel2.focus()
            name_to_del = tabel2.item(del_line)['values'][0]
            drink_file = open('Data/Лекарства_на_курсе.txt', mode='w', encoding='utf-8')
            for elem in range(len(array_drink)):
                if str(name_to_del) in array_drink[elem]:
                    array_drink[elem] = '\n'
                    drink_file.write(array_drink[elem])
                else:
                    drink_file.write((array_drink[elem]))
            drink_file.close()
            drinking_win()
        except:
            isu()

    def make_File():
        time_hour = datetime.now().strftime("%S.%M.%H")
        maked_file = open(f'Документ от {date.today().strftime("%d.%m.%Y")} {time_hour}.txt', mode='w',
                          encoding='utf-8')
        for string in array_drink:
            maked_file.write(string)

    global array_drink
    clearFrame()
    file = open('Data/Лекарства_на_курсе.txt', mode='r', encoding='utf-8')
    array_drink = []
    for i in file:
        if i != '\n':
            array_drink.append(i)
    file.close()

    Button(frame_display,
           compound='l',
           image=img_delete, text='Удалить препарат', font='Times 20',
           height=2,
           command=del_func,
           fg=fg_color_button,
           bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button
           ).grid(row=0, column=0, sticky='nesw')
    Button(frame_display,
           compound='l',
           image=img_make, text='Создать файл с \nпрепаратми на курсе', font='Times 20',
           command=make_File,
           height=96,
           fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button
           ).grid(row=0, column=1, sticky='news')

    tabel2 = Treeview(frame_display)
    tabel2.grid(row=1, column=0, columnspan=2, sticky='news')
    scroll = Scrollbar(frame_display, command=tabel2.yview)
    scroll.place(x=585, y=105, height=224)
    tabel2.config(yscrollcommand=scroll.set)
    tabel2['show'] = 'headings'
    tabel2['columns'] = ('1', '2', '3', '4')
    tabel2.column("1", width=150, minwidth=50)
    tabel2.heading('1', text='Название')
    tabel2.column("2", width=150, minwidth=50)
    tabel2.heading('2', text='Курс. Д.')
    tabel2.column("3", width=150, minwidth=50)
    tabel2.heading('3', text='Начало')
    tabel2.column('4', width=150, minwidth=50)
    tabel2.heading('4', text='Конец')
    for line in array_drink:
        line = line.split(' | ')
        name = line[0].split(': ')
        days = line[1].split(': ')
        start = line[2].split(': ')
        ends = line[3].split(': ')
        tabel2.insert('', 'end', values=(name[0], days[1], start[1], ends[1]))

    Button(frame_display,
           compound='l',
           image=img_edit,
           text='Изменить почту', font='Times 20',
           height=82,
           fg=fg_color_button,
           bg=bg_color_button,
           command=edit_mail,
           activebackground=fg_color_button, activeforeground=bg_color_button
           ).grid(row=2, column=0, columnspan=2, sticky='nesw')






def array_data():
    global data_base
    file_med = open('Data/Ноотропы.txt', mode='r', encoding='utf-8')
    data_base = []
    for line in file_med:
        if line not in '\n':
            data_base.append(line)
    file_med.close()


def exesize():
    main_window.title('Система развития человека/Мнемотехники')
    clearFrame()
    button_lekarstva.config(fg=fg_color_button, bg=bg_color_button)
    button_yprajneniya.config(fg=bg_color_button, bg=fg_color_button, activebackground=bg_color_button,
                              activeforeground=fg_color_button)
    button_o_programe.config(fg=fg_color_button, bg=bg_color_button)
    button_rejim_priem.config(fg=fg_color_button, bg=bg_color_button)

    def bck_sym():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_1, background="white").pack()

    def palace():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_2, background="white").pack()

    def bck_word():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_3, background="white").pack()

    def word_word():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_4, background="white").pack()

    def cep():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_5, background="white").pack()

    def matresh():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_6, background="white").pack()

    def symbols():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_7, background="white").pack()

    def met_ai():
        win1 = Toplevel()
        win1.resizable(False, False)
        Label(win1, image=img_8, background="white").pack()

    Label(frame_display, image=img_9, background="white").grid(row=0, column=0, rowspan=8, sticky='news')
    Button(frame_display, text='Цифры - образы', font='Times 18', command=bck_sym, fg=fg_color_button,
           bg=bg_color_button, activebackground=fg_color_button, activeforeground=bg_color_button, width=24).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  sticky='news')
    Button(frame_display, text='Дворец памяти', font='Times 18', command=palace, fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=1, column=1, sticky='news')
    Button(frame_display, text='Цифры - слова', font='Times 18', command=bck_word, fg=fg_color_button,
           bg=bg_color_button, activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=2, column=1,
                                                                                                        sticky='news')
    Button(frame_display, text='Числа - числа', font='Times 18', command=word_word, fg=fg_color_button,
           bg=bg_color_button, activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=3, column=1,
                                                                                                        sticky='news')
    Button(frame_display, text='Цепочка', font='Times 18', command=cep, fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=4, column=1, sticky='news')
    Button(frame_display, text='Матрешка', font='Times 18', command=matresh, fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=5, column=1, sticky='news')
    Button(frame_display, text='Символы', font='Times 18', command=symbols, fg=fg_color_button, bg=bg_color_button,
           activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=6, column=1, sticky='news')
    Button(frame_display, text='Метод - Айвазовского', font='Times 18', command=met_ai, fg=fg_color_button,
           bg=bg_color_button, activebackground=fg_color_button, activeforeground=bg_color_button).grid(row=7, column=1,
                                                                                                        sticky='news')


main_window = Tk()
main_window.iconphoto(True, PhotoImage(file='Image/icon.png'))
main_window.config(background="white")
frame_display = Frame(main_window, background="white")
frame_display.place(x=186, y=0)
frame_button = Frame(main_window)
frame_button.place(x=0, y=0)
main_window.geometry('789x421')
main_window.geometry('+540+300')
main_window.resizable(False, False)
main_window.title('Система развития человека')

img_1 = PhotoImage(file='Image/1.png')
img_2 = PhotoImage(file='Image/2.png')
img_3 = PhotoImage(file='Image/3.png')
img_4 = PhotoImage(file='Image/4.png')
img_5 = PhotoImage(file='Image/5.png')
img_6 = PhotoImage(file='Image/6.png')
img_7 = PhotoImage(file='Image/7.png')
img_8 = PhotoImage(file='Image/8.png')
img_9 = PhotoImage(file='Image/9.png')

img_delete = PhotoImage(file='Image/img_delete.png')
img_add = PhotoImage(file='Image/add_img.png')
img_edit = PhotoImage(file='Image/img_edit.png')
img_sort = PhotoImage(file='Image/img_sort.png')
img_clock = PhotoImage(file='Image/img_clock.png')
img_make = PhotoImage(file='Image/img_make.png')
img_med = PhotoImage(file='Image/img_med.png')
img_teh = PhotoImage(file='Image/img_teh.png')

fg_color_button = '#115293'
bg_color_button = 'white'

hight_button = 4
button_rejim_priem = Button(frame_button, compound='l', image=img_clock,
                            text='Режим приема',
                            height=100,
                            font='Times 15',
                            command=drinking_win,
                            fg=fg_color_button,
                            bg=bg_color_button,
                            activebackground=fg_color_button, activeforeground=bg_color_button
                            )
button_rejim_priem.grid(row=0, column=0, sticky='nesw')  # Расположение

button_lekarstva = Button(frame_button, compound='l', image=img_med,
                          text='Ноотропы',
                          height=100,
                          font='Times 15',
                          command=nootrops,
                          fg=fg_color_button,
                          bg=bg_color_button,
                          activebackground=fg_color_button, activeforeground=bg_color_button
                          )
button_lekarstva.grid(row=1, column=0, sticky='nesw')  # Расположение

button_yprajneniya = Button(frame_button, compound='l', image=img_teh,
                            text='Мнемотехники',
                            height=100,
                            font='Times 15',
                            command=exesize,
                            fg=fg_color_button,
                            bg=bg_color_button,
                            activebackground=fg_color_button, activeforeground=bg_color_button
                            )
button_yprajneniya.grid(row=2, column=0, sticky='nesw')  # Расположение

button_o_programe = Button(frame_button,
                           text='О программе',
                           height=hight_button, width=16,
                           font='Times 15',
                           command=o_program,
                           fg=fg_color_button,
                           bg=bg_color_button,
                           activebackground=fg_color_button, activeforeground=bg_color_button
                           )
button_o_programe.grid(row=3, column=0)  # Расположение

nootrops()

date_base = []

file_in_curse = open('data/Лекарства_на_курсе.txt', mode='r', encoding='utf-8')
for i in file_in_curse:
    if i != '\n':
        i = i.replace('\n', '')
        i_split = i.split(' | ')[3].split(' ')[1].split('.')
        netx_time = datetime.today() + timedelta(2)
        if date(int(i_split[2]), int(i_split[1]), int(i_split[0])).strftime('%d.%m.%Y') == netx_time.strftime('%d.%m.%Y'):
            date_base.append(i)
#print(date_base)

mail_base()

if len(data_base_mail) > 0 and len(date_base) > 0:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('rakrosovic@gmail.com', 'virtmail17')
    TO = data_base_mail[0].replace('\n', '')
    FROM = 'test@org.com'
    if len(date_base) == 1:
        BODY = 'Через два дня заканчивается прием препарата'
        for i in date_base:
             i = i.split(" | ")[0]
             BODY += f' {i}'
    elif len(date_base) > 1:
        BODY = 'Через два дня заканчиваются курсы приемов препаратов '
        for i in date_base:
             i = i.split(" | ")[0]
             BODY += f' {i},'
    msg = MIMEText(BODY, 'plain', 'utf-8')
    msg['Subject'] = Header('Скоро заканчивается курс приема лекарств', 'utf-8')
    server.sendmail(FROM, TO, msg.as_string())



main_window.mainloop()
