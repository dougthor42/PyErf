# Changelog for PyErf:


# Unreleased
+ Pip and wheel are now pinned in CI so that builds don't break
  when things are updated. (#9)
+ CI was migrated to GitHub Actions. (#18, #23)
+ Code was formatted with `ruff`. (#24)


## 1.0.1 (2017-06-22)
+ Mucked up the previous release... No actual code change, just need to not
  have [ci skip] in my commit message. Doh!


## 1.0.0 (2017-06-22)
+ Updates to unit tests (#6)
+ Better builds (#6)
+ Fixed some edge-case bugs (#6)
+ Updated image url for builds (#7)


## 0.1.6 (2017-03-02)
+ Added PyPy builds to Travis (#5)
+ Added author email to setup.py


## 0.1.5 (2017-02-27)
+ Updated `README.rst` and other docs.


## 0.1.4 (2017-02-27): More Python Versions!
+ Added support for Python27, 33, and 34 by backporting `erf` and `erfc`.
+ added Travis auto-deploy to PyPI.


## 0.1.1 (2017-02-22): Initial Release
+ Initial release! Horray!


## 0.0.1 (2017-02-22): Project Creation
+ Created project from template.
