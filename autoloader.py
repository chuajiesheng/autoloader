#!/usr/bin/python -tt

import argparse
from datetime import datetime
import os
import sys
import time
import shlex, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Option(object):
    pass

class ExitInterrupt(Exception):
    pass

class EventHandler(FileSystemEventHandler):
    def run_make(self):
        if (self._child != None):
            print 'Terminate Existing Process.'
            self._child.terminate()

        print 'Starting Make Process'
        self._child = subprocess.Popen(self._args)

    def __init__(self):
        self._args = ['make']
        if target is not None:
            self._args.extend(target)

        os.chdir(path)
        print 'Running', self._args, 'in', os.getcwd()

        self._child = None
        self._previous = datetime.now()
        print 'Init at', self._previous, 'with delay', delay
        self.run_make()

    def on_modified(self, event):
        #print "On Modified"

        if (datetime.now() - self._previous).seconds > delay:
            self._previous = datetime.now()

            self.run_make()
        else:
            print '.'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This script would automatically re-run the Makefile after \
                     a change is detected in the folder being monitored.')
    parser.add_argument('-d', '--delay', nargs=1, type=int, default=10,
                        help='the delay between sequential builds (default: 10)')
    parser.add_argument('-l', '--location', nargs=1, default='.',
                        help='the location being monitored')
    parser.add_argument('-t', '--target', nargs=1, type=str, default='',
                        help='the Makefile target to run')

    opt = Option()
    args = parser.parse_args(namespace=opt)

    path = opt.location[0]

    if type(opt.delay) is list:
        delay = opt.delay[0]
    else:
        delay = opt.delay

    if (delay < 0):
        delay = 10

    target = opt.target

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print 'Keyboard Interrupt Captured'
        observer.unschedule_all()
        observer.stop()
    observer.join()
