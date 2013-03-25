Django Bacon Ipsum
==================

Django Bacon Ipsum is a simple Django app that replaces the default lorem ipsum filler
text with something meatier. This project was inspired by Pete Nelson's [http://baconipsum.com/](http://baconipsum.com/) but not related to the original. The original PHP and JavaScript project is available at [https://github.com/petenelson/bacon-ipsum](https://github.com/petenelson/bacon-ipsum)

Installation
------------

You will be able to install from PyPI:

    pip install django-bacon-ipsum
    
Or you can include the app directly into your project by copying and pasting it.

Quick start
-----------

1. Add `"django-bacon-ipsum"` to your INSTALLED_APPS setting like this:

```
  INSTALLED_APPS = (
      ...
      'django-bacon-ipsum',
  )
```

2. Include `bacondesign` in the template .html file.

```
  {% load bacondesign %}

```

3. Add in bacon text wherever in one of the following forms:

```
  {% bacon %}
  {% bacon 2 b %}
  {% bacon 4 p %}
  {% bacon 6 w %}
```

where `b` is block of text, `p` is &lt;p&gt;-wrapped block of text, and `w` is number of words.
