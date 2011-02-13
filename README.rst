Tofu Roll
=========
A simple framework for building command line tools.

Example
-------

greetings.py::

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

on the command line::
    
    $: python greetings.py hi
    Hi there
    $: python greetings.py hi -n nate
    Hi, nate

Installation
------------
pip install tofuroll

Why?
----
When I was working on the second version of Done_ I wrote a bunch of code to
generalize command line argument handling. I liked its simplicity so I
extracted it into tofu roll.

.. _Done: http://www.github.com/nathanielksmith/done

Name
----
This project is named after the delicious vegan sushi made here in Atlanta by
TheSushi.

Author
------
Nathaniel Smith, nathanielksmith@gmail.com

