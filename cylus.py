import PySimpleGUI as sg
import sys
import os 
import time 

#Created by Zach Hirst 2/15/22 for the purpose of training my puppy Cylus

if os.environ.get('DISPLAY','') == '':
        print('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')

sg.theme('DarkAmber')

#Layout of the text and button elements
layout = [[sg.Text('How long has Cylus gone without:', justification='center', size=(200, 1), font=('Arial', 30))],
          [sg.Text('Being Outside                          Food & Water ', font=('Arial', 25), pad=(55,0))],
          [sg.Text(size=(12,3), font=('Helvetica', 35), justification='center', key='text0', pad=(0, 75)), 
           sg.Text(size=(12,3), font=('Helvetica', 35), justification='center', key='text1', pad=((125, 0), 75))],
          [sg.Button('Reset Outside', key='reset0', pad = ((100, 320), (0, 0))),
           sg.Button('Reset Food & Water', key='reset1')],
          [sg.Button('Exit', size=(5, 1), pad=(0, (0, 0)))]]

window = sg.Window('Cylus Timer', layout, no_titlebar=True, location=(0,0), size=(800,480), keep_on_top=True)

#Main Logic ---------------------------------------------------
current_time_0 = 0
current_time_1 = 0
hours_0 = 0
hours_1 = 0
start_time_0 = int(time.time())
start_time_1 = int(time.time())
while True:
    event, values = window.read(timeout=10)

    #Timer #0 -------------------------------------------------
    current_time_0 = int(time.time()) - start_time_0

    if current_time_0 >= 3600:
        hours_0 = current_time_0 // 3600

    #Timer #1 -------------------------------------------------
    current_time_1 = int(time.time()) - start_time_1

    if current_time_1 >= 3600:
        hours_1 = current_time_1 // 3600

    #Display Timers -------------------------------------------
    window['text0'].update('{:02d}:{:02d}:{:02d}'.format(current_time_0 // 3600, (current_time_0 // 60) - (hours_0 * 60), current_time_0 % 60))
    window['text1'].update('{:02d}:{:02d}:{:02d}'.format(current_time_1 // 3600, (current_time_1 // 60) - (hours_1 * 60), current_time_1 % 60))

    #Exit & Reset Statements ----------------------------------
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'reset0':
        start_time_0 = int(time.time())
        hours_0 = 0

    if event == 'reset1':
        start_time_1 = int(time.time())
        hours_1 = 0

window.close()
