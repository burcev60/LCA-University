from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
from helpers import *
import pandas as pd

def open_file():
    global file
    filename = filedialog.askopenfilename(defaultextension='.xlsx')

    file = pd.read_excel(filename)

    opens(file, entry_dat_days, entry_dat_students, entry_dat_teachers, entry_light_count, entry_light_power, entry_light_time,
          entry_comp_count, entry_comp_power, entry_comp_time, entry_proj_count, entry_proj_power, entry_proj_time, entry_gadget_count,
          entry_gadget_power, entry_gadget_time, entry_water_hot, entry_water_cold, entry_water_days, entry_water_device_hot,
          entry_water_device_cold, entry_water_days_device, entry_water_count_device, entry_trash_paper, entry_trash_glass,
          entry_trash_plass, entry_trash_org, entry_heat_square, entry_heat_power, entry_heat_floor,
          entry_heat_days)


def save_file_as():
    global df
    df=saving( entry_dat_days, entry_dat_students, entry_dat_teachers, entry_light_count, entry_light_power, entry_light_time,
          entry_comp_count, entry_comp_power, entry_comp_time, entry_proj_count, entry_proj_power, entry_proj_time, entry_gadget_count,
          entry_gadget_power, entry_gadget_time, entry_water_hot, entry_water_cold, entry_water_days, entry_water_device_hot,
          entry_water_device_cold, entry_water_days_device, entry_water_count_device, entry_trash_paper, entry_trash_glass,
          entry_trash_plass, entry_trash_org, entry_heat_square, entry_heat_power, entry_heat_floor, entry_heat_days)

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)

def exit_app():
    root.destroy()

def helps():
    help_window = Toplevel(root)
    help_window.title('Помощь')
    help_label = Label(help_window, text="Привет! \n В приложениии присуствует возможность открытия и сохранения файлов \n"
                                         "Основная деятельность происхоодит в первых четырех вкладках, необходимо задать значения \n"
                                         "После этого во вкладке Расчет можно посмотреть результаты вычисления программы")
    help_label.configure(bd=3, justify=LEFT)
    help_label.pack()

def about():
    about_window = Toplevel(root)
    about_window.title('О программе')
    about_label = Label(about_window, text="University LCA - программа для оценки жизненной деятельности университета \n"
                                           "Версия программы: 0.1\n"
                                           "С вопросами и предложениями пишите nikita-pronin@yandex.ru")
    about_label.configure(bd=3, justify=LEFT)
    about_label.pack()

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def digit_in_frame(element):
    string = element.get()
    if is_digit(string)==False and string != '':
        mb.showerror("Ошибка", "Должно быть введено число")
    return string.isdigit()


def calc_electro():
    light_power=int(entry_light_power.get())
    light_count=int(entry_light_count.get())
    light_time=int(entry_light_time.get())
    comp_count=int(entry_comp_count.get())
    comp_power=int(entry_comp_power.get())
    comp_time=int(entry_comp_time.get())
    proj_power=int(entry_proj_power.get())
    proj_count=int(entry_proj_count.get())
    proj_time=int(entry_proj_time.get())
    gadget_power=int(entry_gadget_power.get())
    gadget_count=int(entry_gadget_count.get())
    gadget_time=int(entry_gadget_time.get())
    people=int(entry_dat_students.get())+int(entry_dat_teachers.get())
    days=int(entry_dat_days.get())
    count=(light_power*light_count*light_time+comp_power*comp_count*comp_time+proj_power*proj_count*proj_time+gadget_power*
            gadget_count*gadget_time)/people*days/1000
    if count > 40:
        label_calculate_el_left['text'] = 'Превышает на'
        label_calculate_el_center['text']=str(float("{0:.3f}".format(abs(40-count))))
        label_calculate_el_center['bg']='#ff5252'
        label_calculate_el_right['text']='кВт/ч на человека. Рекомендуется уменьшить.'
    else:
        label_calculate_el_left['text']='Потребляет'
        label_calculate_el_center['text'] = str(float("{0:.3f}".format(abs(count))))
        label_calculate_el_center['bg'] = 'green'
        label_calculate_el_right['text'] = 'кВт/ч на человека. Всё в норме.'

def calc_water():
    water_hot=int(entry_water_hot.get())
    water_cold=int(entry_water_cold.get())
    water_period=int(entry_water_days.get())
    water_hot_device=int(entry_water_device_hot.get())
    water_cold_device=int(entry_water_device_cold.get())
    water_period_device=int(entry_water_days_device.get())
    water_count_device=int(entry_water_count_device.get())
    people=(int(entry_dat_teachers.get())+int(entry_dat_students.get()))/2

    if water_hot/water_period/people > 8 and water_cold/water_period/people < 20:
        #превышает горячая вода но в норме
        label_calculate_water_left['text'] = 'Перерасход на человека'
        label_calculate_water_center['text'] = str(
            float("{0:.3f}".format((water_hot / water_period / people - 8))))
        label_calculate_water_center['bg'] = '#ff5252'
        label_calculate_water_right['text'] = 'литров горячей воды, холодная в норме.'
    elif water_hot/water_period/people <=8 and water_cold/water_period/people > 20:
        #превышает горячая вода
        label_calculate_water_left['text'] = 'Перерасход на человека'
        label_calculate_water_center['text'] = str(
            float("{0:.3f}".format(water_cold / water_period / people - 12)))
        label_calculate_water_center['bg'] = '#ff5252'
        label_calculate_water_right['text'] = 'литров холодной воды, горячая в норме.'
    elif water_hot / water_period / people > 8 and (water_cold + water_hot) / water_period / people > 20:
        # превышает и холодная и горячая вода
        label_calculate_water_left['text'] = 'Перерасход на человека'
        label_calculate_water_center['text'] = str(
            float("{0:.3f}".format((water_cold + water_hot) / water_period / people - 20)))
        label_calculate_water_center['bg'] = '#ff5252'
        label_calculate_water_right['text'] = 'литров холодной и горячей.'
    else:
        #все в норме
        label_calculate_water_left['text'] = 'Расход на человека'
        label_calculate_water_center['text'] = str(
            float("{0:.3f}".format((water_cold + water_hot) / water_period / people )))
        label_calculate_water_center['bg'] = 'green'
        label_calculate_water_right['text'] = 'литров. Расход в норме.'

    if water_hot_device / water_period_device / water_count_device > 130 and (water_cold_device + water_hot_device) / water_period_device / water_count_device < 260:
        # превышает и холодная и горячая вода
        label_calculate_water_device_left['text'] = 'Перерасход для прибора'
        label_calculate_water_device_center['text'] = str(
            float("{0:.3f}".format((water_hot_device / water_period_device / water_count_device - 130))))
        label_calculate_water_device_center['bg'] = '#ff5252'
        label_calculate_water_device_right['text'] = 'литров горячей воды, холодная в норме.'
    elif water_hot_device / water_period_device / water_count_device<= 130 and (water_cold_device + water_hot_device) / water_period_device / water_count_device > 260:
        # превышает вода вода
        label_calculate_water_device_left['text'] = 'Перерасход для прибора'
        label_calculate_water_device_center['text'] = str(
            float("{0:.3f}".format(water_cold_device / water_period_device / water_count_device - 130)))
        label_calculate_water_device_center['bg'] = '#ff5252'
        label_calculate_water_device_right['text'] = 'литров холодной воды, горячая в норме.'
    elif water_hot_device / water_period_device / water_count_device> 130 and (water_cold_device + water_hot_device) / water_period_device / water_count_device > 260:
        # превышает горячая вода но в норме
        label_calculate_water_device_left['text'] = 'Перерасход для прибора'
        label_calculate_water_device_center['text'] = str(
            float("{0:.3f}".format((water_cold_device + water_hot_device) / water_period_device / water_count_device - 260)))
        label_calculate_water_device_center['bg'] = '#ff5252'
        label_calculate_water_device_right['text'] = 'литров холодной и горячей.'
    else:
        # все в норме
        label_calculate_water_device_left['text'] = 'Расход для прибора'
        label_calculate_water_device_center['text'] = str(
            float("{0:.3f}".format((water_cold_device + water_hot_device) / water_period_device / water_count_device)))
        label_calculate_water_device_center['bg'] = 'green'
        label_calculate_water_device_right['text'] = 'литров. Расход в норме.'


def calc_trash():
    trash_glass=float(entry_trash_glass.get())
    trash_paper=float(entry_trash_paper.get())
    trash_plass=float(entry_trash_plass.get())
    trash_org=float(entry_trash_org.get())
    students=int(entry_dat_students.get())
    teachers=int(entry_dat_teachers.get())
    days=float(entry_dat_days.get())
    days/=365
    trash_normal_weight=(students*22+teachers*156)*days
    if trash_glass_bool.get(): trash_glass*=0.95
    if trash_plass_bool.get(): trash_plass*=0.9
    if trash_paper_bool.get(): trash_paper*=0.75
    calculate=(trash_glass+trash_paper+trash_plass+trash_org)

    if calculate > trash_normal_weight:
        label_calculate_trash_left['text'] = 'Превышает на'
        label_calculate_trash_center['bg']='#ff5252'
        label_calculate_trash_center['text'] = str(float("{0:.1f}".format(abs(calculate-trash_normal_weight))))
        label_calculate_trash_right['text']='Рекомендуется уменьшить количесто мусорных отходов'
    else:
        label_calculate_trash_left['text'] = 'Меньше на'
        label_calculate_trash_center['bg']='green'
        label_calculate_trash_center['text'] = str(float("{0:.1f}".format(abs(calculate-trash_normal_weight))))
        label_calculate_trash_right['text'] = 'Количество мусорных отходов в норме'

def calc_heat():
    heat_square=int(entry_heat_square.get())
    heat_floor=int(entry_heat_floor.get())
    heat_days=int(entry_heat_days.get())
    heat_power=int(entry_heat_power.get())
    heat_power=heat_power/heat_square/heat_days/24

    if heat_floor == 1 and heat_power < 190:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif heat_floor == 1 and heat_power > 190:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-190)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif heat_floor == 2 and heat_power < 175:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif heat_floor == 2 and heat_power > 175:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-175)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif heat_floor == 3 and heat_power < 160:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif heat_floor == 3 and heat_power > 160:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-160)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif (heat_floor == 4 or heat_floor==5) and heat_power < 145:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif (heat_floor == 4 or heat_floor==5) and heat_power > 145:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-145)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif (heat_floor == 6 or heat_floor==7) and heat_power < 140:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif (heat_floor == 6 or heat_floor==7) and heat_power > 140:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-140)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif (heat_floor == 8 or heat_floor == 9) and heat_power < 135:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif (heat_floor == 8 or heat_floor == 9) and heat_power > 135:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-135)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'
    elif (heat_floor == 10 or heat_floor == 11) and heat_power < 130:
        label_calculate_heat_left['text'] = 'Расход'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power)))
        label_calculate_heat_center['bg'] = 'green'
        label_calculate_heat_right['text'] = 'кВт/ч. Расход в норме.'
    elif (heat_floor == 10 or heat_floor == 11) and heat_power > 130:
        label_calculate_heat_left['text'] = 'Перерасход на'
        label_calculate_heat_center['text'] = str(float("{0:.3f}".format(heat_power-130)))
        label_calculate_heat_center['bg'] = '#ff5252'
        label_calculate_heat_right['text'] = 'кВт/ч. Следует уменьшить расход теплоэнергии.'


def calculate():
    try:
        calc_electro()
        calc_trash()
        calc_water()
        calc_heat()
        return True
    except ValueError:
        return mb.showerror("Ошибка", "Все поля должны быть заполнены")


root=Tk()
root.title('University LCA')
menu=Menu(root)
root.configure(menu=menu)

filemenu=Menu(menu, tearoff=0)
filemenu.add_command(label='Открыть', command=open_file)
filemenu.add_command(label='Сохранить как', command=save_file_as)
filemenu.add_command(label='Выход', command=exit_app)

helpmenu= Menu(menu, tearoff=0)
helpmenu.add_command(label='Помощь', command=helps)
helpmenu.add_command(label='О программе', command=about)

menu.add_cascade(label="Файл", menu=filemenu)
menu.add_cascade(label="Справка", menu=helpmenu)


#вкладки
tab_control=ttk.Notebook(root)
#основные данные
tab_dat=ttk.Frame(tab_control)
tab_control.add(tab_dat, text="Данные")
label_dat=Label(tab_dat, text="Основные данные", font="bold")
label_dat.grid(sticky='w', row=0, column=0)
lebel_dat_students=Label(tab_dat, text="Количество студентов:")
lebel_dat_teachers=Label(tab_dat, text="Количество преподавателей и обслуживающего персонала:")
label_dat_days=Label(tab_dat, text="Период анализа в днях:")
entry_dat_days=Entry(tab_dat)
entry_dat_days.bind('<FocusOut>', lambda _: digit_in_frame(entry_dat_days))
entry_dat_students=Entry(tab_dat)
entry_dat_students.bind('<FocusOut>', lambda _: digit_in_frame(entry_dat_students))
entry_dat_teachers=Entry(tab_dat)
entry_dat_teachers.bind('<FocusOut>', lambda _: digit_in_frame(entry_dat_teachers))
lebel_dat_students.grid(row=1, column=0, sticky='w')
lebel_dat_teachers.grid(row=2, column=0, sticky='w')
entry_dat_students.grid(row=1, column=1)
entry_dat_teachers.grid(row=2, column=1)
label_dat_days.grid(row=3, column=0, sticky='w')
entry_dat_days.grid(row=3, column=1)

#создание вкладки электроэнергия
tab_el=ttk.Frame(tab_control)
tab_control.add(tab_el, text="Электроэнергия")
#раздел освещение во вкладке электроэнергия
label_light=Label(tab_el, text="Освещение", font="bold")
label_light_count=Label(tab_el, text='Количество ламп:')
label_light_power=Label(tab_el, text='Мощность ламп:')
label_light_time=Label(tab_el, text='Среднее ремя работы:')
entry_light_count=Entry(tab_el)
entry_light_count.bind('<FocusOut>', lambda _: digit_in_frame(entry_light_count))
entry_light_power=Entry(tab_el)
entry_light_power.bind('<FocusOut>', lambda _: digit_in_frame(entry_light_power))
entry_light_time=Entry(tab_el)
entry_light_time.bind('<FocusOut>', lambda _: digit_in_frame(entry_light_time))
label_light.grid(sticky='w')
label_light_count.grid(sticky='w')
label_light_power.grid(sticky='w')
label_light_time.grid(sticky='w')
entry_light_count.grid(row=1, column=1, sticky='e')
entry_light_power.grid(row=2, column=1, sticky='e')
entry_light_time.grid(row=3, column=1, sticky='e')
#раздел компьютеры во вкладке электроэнергия
label_comp=Label(tab_el, text="Компьютеры", font="bold")
label_comp_count=Label(tab_el, text='Количество ПК:')
label_comp_power=Label(tab_el, text='Мощность ПК:')
label_comp_time=Label(tab_el, text='Среднее ремя работы:')
entry_comp_count=Entry(tab_el)
entry_comp_count.bind('<FocusOut>', lambda _: digit_in_frame(entry_comp_count))
entry_comp_power=Entry(tab_el)
entry_comp_power.bind('<FocusOut>', lambda _: digit_in_frame(entry_comp_power))
entry_comp_time=Entry(tab_el)
entry_comp_time.bind('<FocusOut>', lambda _: digit_in_frame(entry_comp_time))
label_comp.grid(sticky='w', row=5, column=0)
label_comp_count.grid(sticky='w', row=6, column=0)
label_comp_power.grid(sticky='w', row=7, column=0)
label_comp_time.grid(sticky='w', row=8, column=0)
entry_comp_count.grid(row=6, column=1, sticky='e')
entry_comp_power.grid(row=7, column=1, sticky='e')
entry_comp_time.grid(row=8, column=1, sticky='e')
#раздел проектор во вкладке электроэнергия
label_proj=Label(tab_el, text="Проекторы", font="bold")
label_proj_count=Label(tab_el, text='Количество проекторов:')
label_proj_power=Label(tab_el, text='Мощность проекторов:')
label_proj_time=Label(tab_el, text='Среднее ремя работы:')
entry_proj_count=Entry(tab_el)
entry_proj_count.bind('<FocusOut>', lambda _: digit_in_frame(entry_proj_count))
entry_proj_power=Entry(tab_el)
entry_proj_power.bind('<FocusOut>', lambda _: digit_in_frame(entry_proj_power))
entry_proj_time=Entry(tab_el)
entry_proj_time.bind('<FocusOut>', lambda _: digit_in_frame(entry_proj_time))
label_proj.grid(sticky='w', row=0, column=2)
label_proj_count.grid(sticky='w', row=1, column=2)
label_proj_power.grid(sticky='w', row=2, column=2)
label_proj_time.grid(sticky='w', row=3, column=2)
entry_proj_count.grid(row=1, column=3, sticky='e')
entry_proj_power.grid(row=2, column=3, sticky='e')
entry_proj_time.grid(row=3, column=3, sticky='e')
#раздел прочая электроника во вкладке электроэнергия
label_gadget=Label(tab_el, text="Прочая электроника", font="bold")
label_gadget_count=Label(tab_el, text='Количество устройств:')
label_gadget_power=Label(tab_el, text='Средняя мощность устройств:')
label_gadget_time=Label(tab_el, text='Среднее ремя работы:')
entry_gadget_count=Entry(tab_el)
entry_gadget_count.bind('<FocusOut>', lambda _: digit_in_frame(entry_gadget_count))
entry_gadget_power=Entry(tab_el)
entry_gadget_count.bind('<FocusOut>', lambda _: digit_in_frame(entry_gadget_count))
entry_gadget_time=Entry(tab_el)
entry_gadget_time.bind('<FocusOut>', lambda _: digit_in_frame(entry_gadget_time))
label_gadget.grid(sticky='w', row=5, column=2)
label_gadget_count.grid(sticky='w', row=6, column=2)
label_gadget_power.grid(sticky='w', row=7, column=2)
label_gadget_time.grid(sticky='w', row=8, column=2)
entry_gadget_count.grid(row=6, column=3, sticky='e')
entry_gadget_power.grid(row=7, column=3, sticky='e')
entry_gadget_time.grid(row=8, column=3, sticky='e')
text_el_sprav=Text(tab_el, font=('Times new roman', 12), bg='#f0f0f0', state=NORMAL)
text_el_sprav.insert(CURRENT, 'Необходимо вводить данные для мощности в Ваттах, все данные необходимо вводить для     одного дня.'
                              ' В отчете параметры будут в виде кВт/ч на человека')
text_el_sprav.grid(row=10, columnspan=4)
#вкладка вода
tab_water=ttk.Frame(tab_control)
tab_control.add(tab_water, text="Водопотребление")
label_water=Label(tab_water, text="Расход воды потребителями", font="bold")
label_water.grid(sticky='w')
label_water_hot=Label(tab_water, text="Расход горячей воды за период:")
label_water_cold=Label(tab_water, text="Расход холодной воды за период:")
label_water_days=Label(tab_water, text="Количество суток:")
label_water_hot.grid(row=1, column=0,sticky='w')
label_water_cold.grid(row=2, column=0,sticky='w')
label_water_days.grid(row=3, column=0,sticky='w')
entry_water_hot=Entry(tab_water)
entry_water_hot.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_hot))
entry_water_cold=Entry(tab_water)
entry_water_cold.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_cold))
entry_water_days=Entry(tab_water)
entry_water_days.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_days))
entry_water_hot.grid(row=1, column=1)
entry_water_cold.grid(row=2, column=1)
entry_water_days.grid(row=3, column=1)

label_water=Label(tab_water, text="Расход воды приборами", font="bold")
label_water.grid(row=4, column=0, sticky='w')
label_water_device_hot=Label(tab_water, text="Расход горячей воды за период:")
label_water_device_cold=Label(tab_water, text="Расход холодной воды за период:")
label_water_days_device=Label(tab_water, text="Количество суток:")
label_water_count_device=Label(tab_water, text="Количество приборов:")
label_water_count_device.grid(row=8, column=0,sticky='w')
label_water_device_hot.grid(row=5, column=0,sticky='w')
label_water_device_cold.grid(row=6, column=0,sticky='w')
label_water_days_device.grid(row=7, column=0,sticky='w')
entry_water_device_hot=Entry(tab_water)
entry_water_device_hot.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_device_hot))
entry_water_device_cold=Entry(tab_water)
entry_water_device_cold.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_device_cold))
entry_water_days_device=Entry(tab_water)
entry_water_days_device.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_days_device))
entry_water_count_device=Entry(tab_water)
entry_water_count_device.bind('<FocusOut>', lambda _: digit_in_frame(entry_water_count_device))
entry_water_device_hot.grid(row=5, column=1)
entry_water_device_cold.grid(row=6, column=1)
entry_water_days_device.grid(row=7, column=1)
entry_water_count_device.grid(row=8, column=1)
#вкладка мусор
tab_trash=ttk.Frame(tab_control)
tab_control.add(tab_trash, text="Мусорные отходы")
label_trash=Label(tab_trash, text="Мусорные отходы (в килограммах)", font="bold")
label_trash.grid(sticky='w')
#бумажный мусор
label_trash_paper=Label(tab_trash, text='Бумажный:')
entry_trash_paper=Entry(tab_trash)
entry_trash_paper.bind('<FocusOut>', lambda _: digit_in_frame(entry_trash_paper))
global trash_paper_bool
trash_paper_bool=BooleanVar()
check_trash_paper=Checkbutton(tab_trash, text='Перерабатываем', variable=trash_paper_bool)
label_trash_paper.grid(sticky='w', row=1, column=0)
entry_trash_paper.grid(row=1, column=1)
check_trash_paper.grid(row=1, column=3)
#стеклянный мусор
label_trash_glass=Label(tab_trash, text='Стеклянный:')
entry_trash_glass=Entry(tab_trash)
entry_trash_glass.bind('<FocusOut>', lambda _: digit_in_frame(entry_trash_glass))
global trash_glass_bool
trash_glass_bool=BooleanVar()
check_trash_glass=Checkbutton(tab_trash, text='Перерабатываем', variable=trash_glass_bool)
label_trash_glass.grid(sticky='w',row=2, column=0)
entry_trash_glass.grid(row=2, column=1)
check_trash_glass.grid(row=2, column=3)
#пластиковый мусор
label_trash_plass=Label(tab_trash, text='Пластмассовый:')
entry_trash_plass=Entry(tab_trash)
entry_trash_plass.bind('<FocusOut>', lambda _: digit_in_frame(entry_trash_plass))
global trash_plass_bool
trash_plass_bool=BooleanVar()
check_trash_plass=Checkbutton(tab_trash, text='Перерабатываем', variable=trash_plass_bool)
label_trash_plass.grid(sticky='w',row=3, column=0)
entry_trash_plass.grid(row=3, column=1)
check_trash_plass.grid(row=3, column=3)
#органический мусор
label_trash_org=Label(tab_trash, text='Органический:')
entry_trash_org=Entry(tab_trash)
entry_trash_org.bind('<FocusOut>', lambda _: digit_in_frame(entry_trash_org))
label_trash_org.grid(sticky='w',row=4, column=0 )
entry_trash_org.grid(row=4, column=1)
tab_trash.focus_set()
                 #################
tab_heat=ttk.Frame(tab_control)
tab_control.add(tab_heat, text="Отопление")
label_heat=Label(tab_heat, text="Теплопотребление", font="bold")

label_heat_square=Label(tab_heat, text="Площадь здания:")
entry_heat_square=Entry(tab_heat)
entry_heat_square.bind('<FocusOut>', lambda _: digit_in_frame(entry_heat_square)) # ок

label_heat_power=Label(tab_heat, text="Сколько кВт энергии затрачено на отопление:")
entry_heat_power=Entry(tab_heat)
entry_heat_power.bind('<FocusOut>', lambda _: digit_in_frame(entry_heat_power))

label_heat_floor=Label(tab_heat, text="Этажность здания:")
entry_heat_floor=Entry(tab_heat)
entry_heat_floor.bind('<FocusOut>', lambda _: digit_in_frame(entry_heat_floor))

label_heat_days=Label(tab_heat, text="Сутки отопительного периода:")
entry_heat_days=Entry(tab_heat)
entry_heat_days.bind('<FocusOut>', lambda _: digit_in_frame(entry_heat_days))

label_heat.grid(row=0, column=0, sticky='w')
label_heat_square.grid(row=1, column=0, sticky='w')
entry_heat_square.grid(row=1, column=1)
label_heat_power.grid(row=2, column=0, sticky='w')
entry_heat_power.grid(row=2, column=1)
label_heat_floor.grid(row=3, column=0, sticky='w')
entry_heat_floor.grid(row=3, column=1)
label_heat_days.grid(row=4, column=0, sticky='w')
entry_heat_days.grid(row=4, column=1)

#################
tab_calculate=ttk.Frame(tab_control)
tab_control.add(tab_calculate, text="Отчет")
label_calculate=Label(tab_calculate, text="Отчет", font="bold")
label_calculate.grid(row=0, column=0, sticky='w')
button_calculate=Button(tab_calculate, text='Рассчитать', command=calculate)
button_calculate.grid(row=0, column=1)
label_calculate_el=Label(tab_calculate, text="Расходы электроэнергии", font='bold')
label_calculate_el.grid(row=1, column=0, sticky='w')

label_calculate_el_left=Label(tab_calculate, text="Оценка")
label_calculate_el_left.grid(row=2, column=0, sticky='w')
label_calculate_el_center=Label(tab_calculate, text="Количество")
label_calculate_el_center.grid(row=2, column=1)
label_calculate_el_right=Label(tab_calculate, text="кВт/ч на человека")
label_calculate_el_right.grid(row=2, column=2, sticky='w')

label_calculate_trash=Label(tab_calculate, text="Мусорные отходы", font='bold')
label_calculate_trash.grid(row=3, column=0, sticky='w')

label_calculate_trash_left=Label(tab_calculate, text="Оценка")
label_calculate_trash_left.grid(row=4, column=0, sticky='w')
label_calculate_trash_center=Label(tab_calculate, text="Количество")
label_calculate_trash_center.grid(row=4, column=1)
label_calculate_trash_right=Label(tab_calculate, text="кг")
label_calculate_trash_right.grid(row=4, column=2, sticky='w')

label_calculate_water=Label(tab_calculate, text="Водопотребление", font='bold')
label_calculate_water.grid(row=5, column=0, sticky='w')

label_calculate_water_left=Label(tab_calculate, text="Оценка")
label_calculate_water_left.grid(row=6, column=0, sticky='w')
label_calculate_water_center=Label(tab_calculate, text="Количество")
label_calculate_water_center.grid(row=6, column=1)
label_calculate_water_right=Label(tab_calculate, text="литров")
label_calculate_water_right.grid(row=6, column=2, sticky='w')

label_calculate_water_device_left=Label(tab_calculate, text="Оценка")
label_calculate_water_device_left.grid(row=7, column=0, sticky='w')
label_calculate_water_device_center=Label(tab_calculate, text="Количество")
label_calculate_water_device_center.grid(row=7, column=1)
label_calculate_water_device_right=Label(tab_calculate, text="литров")
label_calculate_water_device_right.grid(row=7, column=2, sticky='w')

label_calculate_heat=Label(tab_calculate, text="Теплопотребление", font='bold')
label_calculate_heat.grid(row=8, column=0, sticky='w')

label_calculate_heat_left=Label(tab_calculate, text="Оценка")
label_calculate_heat_left.grid(row=9, column=0, sticky='w')
label_calculate_heat_center=Label(tab_calculate, text="Количество")
label_calculate_heat_center.grid(row=9, column=1)
label_calculate_heat_right=Label(tab_calculate, text="литров")
label_calculate_heat_right.grid(row=9, column=2, sticky='w')

tab_control.pack(expand=0, fill="both", anchor=W)
root.geometry('655x400')
root.mainloop()