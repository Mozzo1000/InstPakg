#!/usr/bin/python

import os, sys, curses, atexit, time

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class cmenu(object):
    datum = {}
    ordered = []
    pos = 0

    def __init__(self, options, title="Menu"):
        curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.curs_set(0)
        self.screen = curses.initscr()
        self.screen.keypad(1)

        self.h = curses.color_pair(1)
        self.n = curses.A_NORMAL

        for item in options:
            k, v = item.items()[0]
            self.datum[k] = v
            self.ordered.append(k)

        self.title = title

        atexit.register(self.cleanup)

    def cleanup(self):
        curses.doupdate()
        curses.endwin()

    def upKey(self):
        if self.pos == (len(self.ordered) - 1):
            self.pos = 0
        else:
            self.pos += 1

    def downKey(self):
        if self.pos <= 0:
            self.pos = len(self.ordered) - 1
        else:
            self.pos -= 1

    def display(self):
        screen = self.screen
        while True:
            screen.clear()
            screen.addstr(2, 2, self.title, curses.A_STANDOUT|curses.A_BOLD)
            screen.addstr(4, 2, "Please select an option...", curses.A_BOLD)

            ckey = None
            func = None

            while ckey != ord('\n'):
                for n in range(0, len(self.ordered)):
                    optn = self.ordered[n]

                    if n != self.pos:
                            screen.addstr(6 + n, 4, "%d. %s" % (n, optn), self.n)
                    else:
                        screen.addstr(6 + n, 4, "%d. %s" % (n, optn), self.h)
                screen.refresh()

                ckey = screen.getch()

                if ckey == 258:
                    self.upKey()

                if ckey == 259:
                    self.downKey()

            ckey = 0
            self.cleanup()
            if self.pos >= 0 and self.pos < len(self.ordered):
                self.datum[self.ordered[self.pos]]()
                self.pos = -1
            else:
                curses.flash()


