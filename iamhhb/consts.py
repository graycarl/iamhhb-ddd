import os.path as op
from iamhhb import config


http = {
    'templates_folder': op.join(config.HOME, 'html', 'templates'),
    'static_folder': op.join(config.HOME, 'html', 'statics'),
    'static_gen_folder': op.join(config.HOME, 'html', 'statics', 'gen'),
    'bower_folder': op.join(config.HOME, 'bower_components'),
    'webassets_cache': op.join(config.HOME, '.cache', 'webassets')
}


database = {
    'path': op.join(config.RUNDIR, 'db.sqlite')
}
