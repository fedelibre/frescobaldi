project('frescobaldi',
    version: '3.1.0',
    meson_version: '>= 0.51.0'
)

pymod = import('python')
pyinst = pymod.find_installation('python3', modules : ['ly', 'popplerqt5'])

# Variables
APPLICATION_ID = 'org.frescobaldi.Frescobaldi'

# Dependencies found by pkgconfig
dependency('poppler-qt5')
