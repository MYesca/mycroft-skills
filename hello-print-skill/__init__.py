from mycroft import MycroftSkill, intent_file_handler

class HelloPrint(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # def initialize(self):  
    #     self.add_event('enclosure.printer.print.file',  
    #                 self.printFile)  
    #     self.add_event('enclosure.printer.print.text',  
    #                 self.printText)

    # def printFile(self, message):
    #     printer.printFile(message.data["fileName"])
    #     self.speak("The printer Emilia should do her work now.")

    # def printText(self, message):  
    #     printer.printText(message.data["text"])
    #     self.speak("The printer Emilia should do her work now.")

    @intent_file_handler('print.hello.intent')
    def handle_print_hello(self, message):
        self.enclosure.print_text("Hello World!!! I am Emilia, a smart old printer from the eighties!")
        self.speak_dialog('print.hello')

    @intent_file_handler('print.picture.intent')
    def handle_print_picture(self, message):
        self.enclosure.print_file("/home/yesca/bs.txt")
        self.speak_dialog('print.picture')

def create_skill():
    return HelloPrint()
