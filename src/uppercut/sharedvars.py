from redis import Redis
import json

class SharedVarAccessor(object)
    def __init__(self,sharedvars,varName,defaultValue=None):
        self._sharedvars = sharedvars
        self._varname = varName
        self._defaultValue = defaultValue
    @property
    def Value(self):
        return self._sharedvars.get(self.varName,self._defaultValue)

    @Value
    def Value(self,val):
        self._sharedvars.set(self.varName,self.value)

class SharedVarStore(Redis):
    """This class abstracts the reading and setting of shared variables between modules.
    This specific implementation uses Redis"""
    def __init__(self,moduleName,*args,**kwargs):
        self._client = Redis(*args,**kwargs)
        self._modName = moduleName

    def getKey(self,varName):
        """generate the key name used to store the var in Redis"""
        return '{}/{}'.format(self._modName,varName)

    def getAccessor(self,varName):


    def get(self,varName,defaultValue=None):
        """ Get the value of a shared variable.

        @param: varName The name of the variable that you need to access.
        @param: defaultValue The default value to return if the variable doesn't exist yet.
        """
        v = self._client.get(self.getKey(varName))
        if v is None: return defaultValue
        v = v.decode('utf-8')
        v = json.loads(v)
        return v

    def set(self,varName,value):
        """ Set the value of a shared variable.

        @param: varName The name of the variable to set.
        @param: value The new value of the variable.
        """
        self._client.set(self.getKey(varName),json.dumps(value))

    
