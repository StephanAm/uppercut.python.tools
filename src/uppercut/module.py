""" tools to configure modules used in an uppercut system """
from redis import Redis
import constants
import json

import signal
import time


class Module(object):
    def terminate(self,signum,frame):
        self._isUp = False
    
    def __init__(self,name,interval,loopCallable,vars):
        signal.signal(signal.SIGINT,self.terminate)
        signal.signal(signal.SIGTERM,self.terminate)
        self._name = name
        self._interval = interval
        self._mainLoop = loopCallable
        self._isUp = False

    def _register(self):
        _redis = Redis(host=constants.EnvVars.MOD_REG_SERVER)
        modInfo = {'name':self._name}
        _redis.lpush(constants.Keys.MOD_LIST)

    def start(self):
        self._isUp = True
        while self._isUp:
            self._mainLoop(self)
            time.sleep(self._interval)


