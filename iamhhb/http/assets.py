from webassets import Environment, Bundle
from iamhhb import consts

# TODO: disable autobuild in production
env = Environment(
    directory=consts.http['static_gen_folder'],
    url='/statics/gen',
    load_path=[
        consts.http['static_folder'],
        consts.http['bower_folder'],
    ],
    auto_build=True
)

js = Bundle(
    'site.js',
    output='main.js'
)
css = Bundle(
    'site.scss',
    filters='libsass',
    output='main.css'
)

env.register('mainjs', js)
env.register('maincss', css)
