Tofu Roll
=========

    A simple framework for building command line tools.

Example
-------

greetings.py::

    from tofuroll import *
    
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
                'name' : 'name',
                'help' : "someone's name"
            }

    if __name__ == '__main__':
        app().run()

on the command line::
    
    $: python greetings.py hi
    Hi there
    $: python greetings.py hi -n nate
    Hi, nate

