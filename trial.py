import commands
import os
import eyed3

# Changing string to unicode


def str_uni(string):
    unicode = unicode(string, 'utf-8')
    return unicode


def addslashes(s):
    s = s.replace(' ', '\ ').replace("'", "\'").replace('"', '\"')
    return s

# I used a class here
# This is pretty surprising since I suck at OOPS
# Looks like I want to conquer my Fear
# Carpe Diem
# Also , Fuck you TKT


class Trial(object):

    def __init__(self):
        self.message = 'is it a constructor'

    def show_details(self, audio_file):
        print "Artist name is %s" % (audio_file.tag.artist)

# Below Link will be useful for images
# http://tuxpool.blogspot.in/2013/02/how-to-store-images-in-mp3-files-using.html

# Official Docs
# http://eyed3.nicfit.net/api/eyed3.id3.html#id1

# Change method of taking input , use some file - explorer
#music_path = str(raw_input("Enter the path for the Music Directory: "))
music_path = '/home/yashmehrotra/Music/Music/'
os.chdir(music_path)
current_directory = commands.getoutput('pwd')
# Finding the right bash command took 30 mins , it isnt as easy as it seems
mp3_list = commands.getoutput('ls -R | grep ".mp3" ').split('\n')

# List of all the music files in the given directory
# Be a true pythonista and do not use this -- edit - fixed i am a true
# pythonista \n Me Gusta (Why did that troll went out of fashion)
print "Here is a list of all the songs"
for index, song in enumerate(mp3_list, start=1):
    print index, song

print "Please enter the song no. you want to edit,press -1 to exit"
user_choice = int(raw_input())
if user_choice != -1:
    x = mp3_list[user_choice - 1]
    str1 = 'find ' + current_directory + ' -name "' + x + '*"'
    str1 = 'find %s -name "%s*" ' % (current_directory, x)
    # Improve fucking str1 , have u ever heard of string formatting asshole
    # Also finding this command took a lot of time
    x = commands.getoutput(str1)
    print x
    audio_file = eyed3.load(x)
    t = Trial()
    t.show_details(audio_file)
