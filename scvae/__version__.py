MAJOR_VERSION = "2"
MINOR_VERSION = "1"
PATCH_VERSION = "2"
VERSION_SUFFIX = "dev"

VERSION = (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)

__version__ = ".".join(map(str, VERSION))

if VERSION_SUFFIX:
    __version__ = __version__ + VERSION_SUFFIX
