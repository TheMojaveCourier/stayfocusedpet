class Pet(object):


    def __init__(self,name,key):
        self.name = name
        self.hungry = True
        self.starved = False
        self.bored = False
        self.upset = False
        self.violent = False
        self.sleepy = False

        self.key = key
        self.messages = {
           'hungry' : "Peinaw",
            'bored' : "Variemai",
            'upset' :  "Taragmenos",
            'awake' :  "Jipnios",
            'asleep':  "ZzZ",
            'sleepy':  "nystagmenos"
        }


    def message_output(self,key):
        self.key = key
        print(self.messages[self.key])


