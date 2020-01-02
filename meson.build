project('frescobaldi',
    version: '3.1.0',
    meson_version: '>= 0.51.0'
)

# Importing modules
i18n  = import('i18n')
python = import('python')

# Check python installation and required modules
pyinst = python.find_installation('python3', modules : ['ly', 'popplerqt5'])

# Variables
APPLICATION_ID = 'org.frescobaldi.Frescobaldi'

# Dependencies found by pkgconfig
dependency('poppler-qt5')

subdir('po')
