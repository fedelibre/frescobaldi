i18n.gettext(meson.project_name(),
  install_dir: join_paths(pypadir, 'frescobaldi_app', 'i18n'),
  args: [
    '--from-code=UTF-8',
    '--package-name=Frescobaldi',
    '--package-version=' + meson.project_version(),
    '--msgid-bugs-address=https://github.com/frescobaldi/frescobaldi/issues/new',
    '--keyword',                # empty the default keyword list
    '--keyword=_:1c,2,3,4t',    # context, message, plural, count
    '--keyword=_:1,2,3t',       # message, plural, count
    '--keyword=_:1c,2,2t',      # context, message
    '--keyword=_:1',            # message
    '--add-comments=L10N',
  ]
)
