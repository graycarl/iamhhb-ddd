import os.path as op
from iamhhb import config


http = {
    'templates_folder': op.join(config.HOME, 'html', 'templates'),
    'static_folder': op.join(config.HOME, 'html', 'statics')
}
