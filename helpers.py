import pandas as pd

def saving( per1, per2, per3, per4, per5, per6, per7, per8, per9, per10, per11, per12, per13, per14, per15,
          per16, per17, per18, per19, per20, per21, per22, per23, per24, per25, per26, per27, per28, per29, per30, per31):
    df = pd.DataFrame({
        'var': ['entry_dat_days', 'entry_dat_students', 'entry_dat_teachers', 'entry_light_count', 'entry_light_power', 'entry_light_time',
          'entry_comp_count', 'entry_comp_power', 'entry_comp_time', 'entry_proj_count', 'entry_proj_power', 'entry_proj_time', 'entry_gadget_count',
          'entry_gadget_power', 'entry_gadget_time', 'entry_water_hot', 'entry_water_cold', 'entry_water_days', 'entry_water_device_hot',
          'entry_water_device_cold', 'entry_water_days_device', 'entry_water_count_device', 'entry_trash_paper', 'entry_trash_glass',
          'entry_trash_plass', 'entry_trash_org', 'entry_heat_square', 'entry_heat_floor', 'entry_heat_power', 'entry_heat_days']
    })
    series = pd.Series([per1.get(), per2.get(), per3.get(), per4.get(), per5.get(), per6.get(), per7.get(),
                        per8.get(), per9.get(), per10.get(), per11.get(), per12.get(), per13.get(), per14.get(),
                        per15.get(),per16.get(), per17.get(), per18.get(), per19.get(), per20.get(), per21.get(), per22.get(),
                        per23.get(), per24.get(), per25.get(), per26.get(), per27.get(), per28.get(), per29.get(), per30.get()])

    df['value']=series
    return df

def opens(file, per1, per2, per3, per4, per5, per6, per7, per8, per9, per10, per11, per12, per13, per14, per15,
          per16, per17, per18, per19, per20, per21, per22, per23, per24, per25, per26, per27, per28, per29, per30):
    list=file['value'].tolist()

    per1.delete(0, 'end')
    per2.delete(0, 'end')
    per3.delete(0, 'end')
    per4.delete(0, 'end')
    per5.delete(0, 'end')
    per6.delete(0, 'end')
    per7.delete(0, 'end')
    per8.delete(0, 'end')
    per9.delete(0, 'end')
    per10.delete(0, 'end')
    per11.delete(0, 'end')
    per12.delete(0, 'end')
    per13.delete(0, 'end')
    per14.delete(0, 'end')
    per15.delete(0, 'end')
    per16.delete(0, 'end')
    per17.delete(0, 'end')
    per18.delete(0, 'end')
    per19.delete(0, 'end')
    per20.delete(0, 'end')
    per21.delete(0, 'end')
    per22.delete(0, 'end')
    per23.delete(0, 'end')
    per24.delete(0, 'end')
    per25.delete(0, 'end')
    per26.delete(0, 'end')
    per27.delete(0, 'end')
    per28.delete(0, 'end')
    per29.delete(0, 'end')
    per30.delete(0, 'end')


    per1.insert(0, str(list[0]))
    per2.insert(0, str(list[1]))
    per3.insert(0, str(list[2]))
    per4.insert(0, str(list[3]))
    per5.insert(0, str(list[4]))
    per6.insert(0, str(list[5]))
    per7.insert(0, str(list[6]))
    per8.insert(0, str(list[7]))
    per9.insert(0, str(list[8]))
    per10.insert(0, str(list[9]))
    per11.insert(0, str(list[10]))
    per12.insert(0, str(list[11]))
    per13.insert(0, str(list[12]))
    per14.insert(0, str(list[13]))
    per15.insert(0, str(list[14]))
    per16.insert(0, str(list[15]))
    per17.insert(0, str(list[16]))
    per18.insert(0, str(list[17]))
    per19.insert(0, str(list[18]))
    per20.insert(0, str(list[19]))
    per21.insert(0, str(list[20]))
    per22.insert(0, str(list[21]))
    per23.insert(0, str(list[22]))
    per24.insert(0, str(list[23]))
    per25.insert(0, str(list[24]))
    per26.insert(0, str(list[25]))
    per27.insert(0, str(list[26]))
    per28.insert(0, str(list[27]))
    per29.insert(0, str(list[28]))
    per30.insert(0, str(list[29]))


