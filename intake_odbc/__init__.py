from ._version import get_versions
from .intake_odbc import ODBCSource, ODBCPartitionedSource

__version__ = get_versions()['version']
del get_versions
