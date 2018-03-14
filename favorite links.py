import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=x0uXVy4fzUA"]

music = ["https://www.youtube.com/watch?v=LsoLEjrDogU"]

answer = pg.prompt (
"""
Which would you like to do?
a) watch vines
b) listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)


elif answer == "b":
    for i in music:
        webbrowser.open(i)
