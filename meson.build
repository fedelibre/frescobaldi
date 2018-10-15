project('frescobaldi',
    version: '3.0.1-beta',
    meson_version: '>= 0.46.0'
)

## MESON MODULES ##
#i18n  = import('i18n')
# NOTE: Meson python3 module is deprecated, use python module instead.
pymod = import('python')
pyinst = pymod.find_installation('python3')


## DEPENDENCIES ##

# Dependencies found by pkgconfig
dependency('poppler-qt5')

# Python 3 dependencies
pydep = [
  'ly',
  'popplerqt5',
]

foreach module : pydep
  module_check = run_command(pyinst, '-c', 'import ' + module)
  if module_check.returncode() == 0
    message(module + ' python module was found')
  else
    warning(module + ' python module was not found!')
  endif
endforeach
