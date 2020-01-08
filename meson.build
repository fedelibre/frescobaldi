project('frescobaldi',
    version: '3.2.0',
    meson_version: '>= 0.51.0'
)

# Meson modules
i18n  = import('i18n')
python = import('python')

# Python modules
py_modules = [
    'cups',
    'ly',
    'popplerqt5',
    'pyportmidi',
    'PyQt5.QtCore',
    'PyQt5.QtGui',
    'PyQt5.QtNetwork',
    'PyQt5.QtPrintSupport',
    'PyQt5.QtSvg',
    'PyQt5.QtWebChannel',
    'PyQt5.QtWebEngineWidgets',
    'PyQt5.QtWidgets',
    'PyQt5.sip',
]

# Check python installation and required modules
pyinst = python.find_installation('python3', modules : py_modules)

# Dependencies found by pkgconfig
dependency('poppler-qt5')

# Variables
APPLICATION_ID = 'org.frescobaldi.Frescobaldi'

subdir('po')

# Copy the app in the python path.
install_subdir(
    'frescobaldi_app',
    install_dir: pyinst.get_install_dir()
)

# Install the executable in bindir.
configure_file(
    input: 'frescobaldi',
    output: 'frescobaldi',
    copy: true,
    install_dir: get_option('bindir')
)
