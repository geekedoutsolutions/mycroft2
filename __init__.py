from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'chrismcawesome'

LOGGER = getLogger(__name__)

class PersonalitySkill1(MycroftSkill):

    def __init__(self):
        super(PersonalitySkill1, self).__init__(name="PersonalitySkill1")
		
    def initialize(self):
	matt_or_dave_intent = IntentBuilder("MattOrDaveIntent").\
            require("MattOrDaveKeyword").build()
	self.register_intent(matt_or_dave_intent, self.handle_matt_or_dave_intent)

    def handle_matt_or_dave_intent(self, message):
	self.speak_dialog("matt.dave")
	
	
    def stop(self):
        pass
	
def create_skill():
    return PersonalitySkill1()
