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
          [sg.Text(' Outside                 Water                   Food', font=('Arial', 25), pad=(65,0))],
          [sg.Text(size=(10,2), font=('Helvetica', 33), justification='center', key='text0', pad = (0, 30)), 
           sg.Text(size=(10,2), font=('Helvetica', 33), justification='center', key='text1'), 
           sg.Text(size=(10,2), font=('Helvetica', 33), justification='center', key='text2')],
          [sg.Button('Reset Outside', key='reset0', pad = ((60, 0) ,0)),
           sg.Button('Reset Water', key='reset1', pad = (155, 0)),
           sg.Button('Reset Food', key='reset2')],
          [sg.Button('Exit', size=(5, 1), pad=(0, (130, 0)))]]

window = sg.Window('Cylus Timer', layout, no_titlebar=True, location=(0,0), size=(800,480), keep_on_top=True)

#Main Logic ---------------------------------------------------
current_time_0 = 0
current_time_1 = 0
current_time_2 = 0
hours_0 = 0
hours_1 = 0
hours_2 = 0
start_time_0 = int(time.time())
start_time_1 = int(time.time())
start_time_2 = int(time.time())
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
    #Timer #2 -------------------------------------------------
    current_time_2 = int(time.time()) - start_time_2

    if current_time_2 >= 3600:
        hours_2 = current_time_2 // 3600


    #Display Timers -------------------------------------------
    window['text0'].update('{:02d}:{:02d}:{:02d}'.format(current_time_0 // 3600, (current_time_0 // 60) - (hours_0 * 60), current_time_0 % 60))
    window['text1'].update('{:02d}:{:02d}:{:02d}'.format(current_time_1 // 3600, (current_time_1 // 60) - (hours_1 * 60), current_time_1 % 60))
    window['text2'].update('{:02d}:{:02d}:{:02d}'.format(current_time_2 // 3600, (current_time_2 // 60) - (hours_2 * 60), current_time_2 % 60))

    #Exit & Reset Statements ----------------------------------
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'reset0':
        start_time_0 = int(time.time())
        hours_0 = 0

    if event == 'reset1':
        start_time_1 = int(time.time())
        hours_1 = 0

    if event == 'reset2':
        start_time_2 = int(time.time())
        hours_2 = 0


window.close()
