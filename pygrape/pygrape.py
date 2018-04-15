#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018 leviathan
# @license MIT

import threading


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function()

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class pygrape:
    interval_ = 0
    clean_ = "\r\033[K"
    msg_ = ""
    timer = threading.Timer
    rt = RepeatedTimer

    def __init__(self, interval):
        self.interval_ = interval
        self.rt = RepeatedTimer(self.interval_, self.flush)

    def writer(self, msg):
        self.msg_ = msg

    def flush(self):
        print(self.clean_, end='')
        print(self.msg_, end='', flush=True)

    def stop(self):
        print("\n")
        self.rt.stop()
