from behave import *
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance
from mycroft.skills.audioservice import AudioService

@given('a recitation may or may not be in progress')
def step_impl(context):
    audioservice = AudioService()
    # seams dumb but it will test to see if the audio service is initialised
    assert(audioservice.is_playing() is True or audioservice.is_playing() is False)

@when('the user asks for a bible book without a chapter')
def step_impl(context):
    audioservice = AudioService()
    wait_for_dialog(context.bus, ['read.me.a.book.of.the.bible'])
    wait_for_dialog(context.bus, ['Daniel'])
    assert (audioservice.is_playing() is True)