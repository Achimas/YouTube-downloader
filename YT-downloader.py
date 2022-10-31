import PySimpleGUI as sg
from pytube import YouTube

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#888',
                                        'TEXT': '#121212',
                                        'INPUT': 'white',
                                        'TEXT_INPUT': '#339966',
                                        'SCROLL': '#99CC99',
                                        'BUTTON': ('white', '#475841'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }
  
# Switch to use your newly created theme
# sg.theme('DarkTeal9')
sg.theme('MyCreatedTheme')


# Choose layout for programm GUI
layout = [
    [sg.Text('Введите ссылку на папку:')],
    [sg.Input(key = '-FOLDER_INPUT-')],
    [sg.Text('Скопируйте ссылку на видео:')],
    [sg.Input(key = '-LINK_INPUT-')],
    [sg.Button('Cкачать!', key = '-DOWNLOAD-')],
    [sg.Text('', enable_events=True, key = '-TEXT-')]
    ]


# Naming and starting window
window = sg.Window('YouTube Downloader', layout)

while True:
    event, values = window.read()

    # Condition for closing
    if event == sg.WIN_CLOSED:
        break

    # Event for clicking Button
    if event == '-DOWNLOAD-':
        try:
            folder_link = values['-FOLDER_INPUT-'].strip()
            video_link = values['-LINK_INPUT-'].strip()
            folder_link_in = folder_link.replace(r"\\", r"\\\\")
            vt = YouTube(video_link)
            vd = vt.streams.get_highest_resolution()
            vd.download('%s' % folder_link_in)
            window['-TEXT-'].update('Загрузка завершена!')
        except:
            window['-TEXT-'].update('Проверьте ссылки!')

window.close()

""" # Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '# 000066',
                                        'TEXT': '# FFCC66',
                                        'INPUT': '# 339966',
                                        'TEXT_INPUT': '# 000000',
                                        'SCROLL': '# 99CC99',
                                        'BUTTON': ('# 003333', '# FFCC66'),
                                        'PROGRESS': ('# D1826B', '# CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }
  
# Switch to use your newly created theme
sg.theme('MyCreatedTheme') """