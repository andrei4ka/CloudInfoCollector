#!/usr/bin/env python

import os, sys
from stat import *

print oct(os.stat(sys.argv[1])[ST_MODE])[-3:]
