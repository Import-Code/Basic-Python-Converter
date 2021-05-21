import ffmpeg
import PySimpleGUI as sg
layout = [  [sg.Text("Select Format")],     
            [sg.Input()],
            [sg.Text("Select Output Format")],
            [sg.Input()],
            [sg.Button('Ok')] ]
window = sg.Window('Format selector', layout)
event, values = window.read()

window.close()

stream = ffmpeg.input('input.' + values[0])
stream = ffmpeg.output(stream, 'output.' + values[1])

ffmpeg.run(stream)