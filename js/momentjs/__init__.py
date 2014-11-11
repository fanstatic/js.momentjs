from fanstatic import Library, Resource

library = Library('moment.js', 'resources')

moment = Resource(library, 'moment.js', minified='moment.min.js')

moment_with_locales = Resource(
    library,
    'moment-with-locales.js',
    minified='moment-with-locales.min.js')
