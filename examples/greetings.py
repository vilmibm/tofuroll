from tofuroll.tofuroll import *

class app(TofuApp):
    @command
    def hi(self, options, args):
        if options.name:
            print "Hi, %s" % options.name
        else:
            print "Hi there"

    @option
    def name(self):
        return {
            'help' : "someone's name"
        }

if __name__ == '__main__':
    app().run()
