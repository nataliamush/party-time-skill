from mycroft import MycroftSkill, intent_file_handler


class PartyTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.num_asks = 0

    @intent_file_handler('time.party.intent')
    def handle_time_party(self, message):
        self.speak_dialog('Its party time')
    
    def converse(self, message):
        utterance_has_time = self.voc_match(message.data['utterances'][0], 'Time')
        if utterance_has_time:
            self.num_asks += 1
            if self.num_asks % 3 == 0:
                self.speak_dialog("It's party time")
                return True



def create_skill():
    return PartyTime()

