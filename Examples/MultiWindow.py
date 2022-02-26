import PySimpleGUI as sg 
import os

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

options = {
        'font':('Helvetica', 24, 'bold'),
        'title_color':'grey',
        'tab_background_color':'green',
        'selected_title_color':'white',
        'selected_background_color':'blue',
        'enable_events':True,
        'tab_location':'bottomLeft',
}

layout_tab1 = [
        [sg.Text('Here is Tab 1')],
        [sg.Text('Nothing here, but buttons', size=(30,2), font=('Helvetica', 20))],
        [sg.Button('Pause', button_color=('white', '#001480')),
         sg.Button('Reset', button_color=('white', '#007339')),
         sg.Exit(button_color=('white', 'firebrick4'))]]

layout_tab2 = [
        [sg.Text('Window 1'),],
        [sg.Input(do_not_clear=True)],
        [sg.Text(size=(15,1))],
        [sg.Button('Launch 2'), sg.Button('Exit')]]

layout_tab3 = [
        [sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'),initial_value=16, change_submits=True),
         sg.Slider(range=(6,172), orientation='h', size=(10,20), change_submits=True, font=('Helvetica 20')),
         sg.Text("Aa", size=(2,1), font="Helvetica 16")]]

layout_tab = [[
    sg.Tab('Weather', layout_tab1, key='-TAB1-'),
    sg.Tab('Work Status', layout_tab2, key='-TAB2-'),
    sg.Tab('Home Auto Control', layout_tab3, key='-TAB3-')]]

layout = [[sg.TabGroup(layout_tab, **options, key='-TAB-')]]

window = sg.Window('TAB GROUP', layout, font=('Helvetica', 12), finalize=True)
window['-TAB3-'].select()


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-TAB':
        tab = values['-TAB-']
        print(f'Tab selected with key {tab}')

window.close()
