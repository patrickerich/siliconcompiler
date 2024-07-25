from siliconcompiler._common import NodeStatus as SCNodeStatus

# CLI entry banner autogenerated using pyfiglet.
# >> pyfiglet.figlet_format("SC Server")
banner = r'''
 ____   ____   ____
/ ___| / ___| / ___|  ___ _ ____   _____ _ __
\___ \| |     \___ \ / _ \ '__\ \ / / _ \ '__|
 ___) | |___   ___) |  __/ |   \ V /  __/ |
|____/ \____| |____/ \___|_|    \_/ \___|_|
'''


class NodeStatus(SCNodeStatus):
    '''
    Enum class to help ensure consistent status messages
    '''

    # special code for uploaded
    UPLOADED = 'uploaded'


class JobStatus():
    '''
    Enum class to help ensure consistent status messages
    '''

    RUNNING = "running"

    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"
    REJECTED = "rejected"
    TIMEOUT = "timeout"

    UNKNOWN = "unknown"
