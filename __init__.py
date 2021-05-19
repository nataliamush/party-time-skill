from mycroft import MycroftSkill, intent_file_handler


class PartyTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.party.intent')
    def handle_time_party(self, message):
        self.speak_dialog('time.party')


def create_skill():
    return PartyTime()

