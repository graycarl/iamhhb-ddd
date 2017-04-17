import os
import os.path as op


HOME = op.abspath(op.join(op.dirname(__file__), '..'))
RUNDIR = op.join(HOME, 'run')

# Load local config
ENV_CONFIG_KEY = 'IAMHHB_LOCAL_CONFIG'
if ENV_CONFIG_KEY in os.environ:
    try:
        custom_confile = op.abspath(os.environ[ENV_CONFIG_KEY])
        with open(custom_confile) as confile:
            exec(compile(confile.read(), custom_confile, "exec"), globals())
    except IOError as e:
        e.strerror = "Unable to read config file [%s] (%s)" \
            % (custom_confile, e.strerror)
        raise
