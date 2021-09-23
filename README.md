# mycroft-niv
an audiobible bible reading skill for mycroft. with david suchet!


check out the laugh skill in the mycroft-skills repo to see how to develop this mycroft skill

https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/message-bus

https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/message-bus

https://mycroft-core.readthedocs.io/en/master/source/mycroft.html#audioservice-class


https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps
```
from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance


@given('a {timer_length} timer is set')
@given('a timer is set for {timer_length}')
def given_set_timer_length(context, timer_length):
    emit_utterance(context.bus, 'set a timer for {}'.format(timer_length))
    wait_for_dialog(context.bus, ['started.timer'])
```

https://opensource.com/article/20/6/mycroft-voice-assistant-skill

