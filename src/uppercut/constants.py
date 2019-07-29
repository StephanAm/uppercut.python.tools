"""some standard constants used with an uppercut system"""
class EnvVars(object):
    """commonly used env variable names"""
    SHARED_VAR_SERVER = "SHARED_VAR_SERVER" # the env var used to store the host name of the service that manages variables shared between modules.
    MOD_REG_SERVER = "MOD_REG_SERVER" # the env var used to indicate the host name of the module registration server

class Keys(object):
    """commonly used key names"""
    MOD_LIST = "UPPERCUT_MOD_LIST"
# some friendlier constant names.
SharedVariableServer = SHARED_VAR_SERVER
ModuleRegistrationServer = MOD_REG_SERVER