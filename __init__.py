# Done - Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.
import os
import random
import json

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import LOG
from mycroft.util import play_mp3
from mycroft.util.log import LOG
from mycroft.audio import is_speaking, wait_while_speaking
from os.path import expanduser

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# a big thanks to the jarbisAI person for the study material (the laugh skill)

class NIVReaderSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(NIVReaderSkill, self).__init__(name="NIVReaderSkill")
        # get playlist
        self.audio_bible_folder = expanduser('~/Music/NIV/')
        self.playlist = os.listdir(self.audio_bible_folder)
        self.player = False
        self.playlist_filename = self.audio_bible_folder + 'playlist.list'
        with open(self.playlist_filename, 'w') as playlist_file:
            for index in range(len(self.playlist)):
                self.playlist[index] = self.playlist[index].replace(' ','\ ')
                self.playlist[index] = self.playlist[index].rstrip()
                playlist_file.write(self.playlist[index])
        self.playlist = open(self.playlist_filename, 'r').readlines()

        # Initialize working variables used within the skill.
        # self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    # @intent_handler(IntentBuilder("").require("Hello").require("World"))
    # def handle_hello_world_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        # self.speak_dialog("hello.world")

    # @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    # def handle_count_intent(self, message):
    #     if message.data["Dir"] == "up":
    #         self.count += 1
    #     else:  # assume "down"
    #         self.count -= 1
    #     self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False



    @intent_file_handler('play.me.a.random.chapter.of.the.bible.intent')
    def handle_random_bible_book_intent(self):
        filename = self.audio_bible_folder + str(random.choice(self.playlist))
        LOG.debug('bible book now playing is %s',filename)
        if is_speaking():
            wait_while_speaking()
        self.player = play_mp3(filename)


    def stop(self):
        try:
            if self.player.is_playing():
                self.player.terminate()
            return True
        except(Exception):
            return False #pass the crackpipe lol - of coarse its gonna return true.

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return NIVReaderSkill()
