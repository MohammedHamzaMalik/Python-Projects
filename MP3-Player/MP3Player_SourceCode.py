'''
Let's get started
We gonna use Tkinter to render our application menu and buttons, and also loading the music 
from files and then pygame library to play, pause and stop the music

Basics of pygame
Pygame has an inbuilt method called mixer () which provides us intuitive syntax on dealing 
with sounds files in python, we will see ;

loading and playing music
pausing and unpausing music
stoping the music file
loading and playing music with pygame
To play music with pygame you're firstly supposed to import mixer(), initialize it through 
init(), *and then using *music.load() to load the music and finally playing it with music.play().
'''


# First Let us import all necessary Library
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Let's now implement our class & Buttons for our application
class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60) 
        self.music_file = False
        self.playing_state = False


    # Let's now add the method to the class we just made to load music file from our computer, 
    # just as shown in the code below

    # Adding Load Method to our MusicPlayer class
    def load(self):
        self.music_file = filedialog.askopenfilename()


    # After Loading the Music file from the file we need a function to Play our Music File.
    # Let's make it using the concepts we just learned above.

    # Adding Play Method to our class
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()


    # After adding the Play Method to our class we need a Method to pause and unpause & also to 
    # Stop the Music

    # Finally Let's add the pause and stop method to our class
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
