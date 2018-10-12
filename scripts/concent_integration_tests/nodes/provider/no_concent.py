#!/usr/bin/env python
"""

Regular, unmodified Provider node, running with DEBUG loglevel

"""

import sys
from scripts.concent_integration_tests import params

from golemapp import start

sys.argv.extend(params.PROVIDER_ARGS_NO_CONCENT)

start()
