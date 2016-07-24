django-filepreviewfields
========================

> Fields for previewing image and video uploaded files

Installation
------------

```sh
pip install django-filepreviewfields
```

Adding to installed apps
------------------------

- To use file preview fields, you have to add it to your INSTALLED_APPS on your project's settings.py so the needed static files can be loaded:

```python
    INSTALLED_APPS = (
        ...
        'filepreviewfields',
    )
```

Using SortedManyToManyField
---------------------------

- To use SortedManyToMany field, just create a field as if you were adding the default ManyToMany

```python
    from django.db import models
    from filepreviewfields.fields import ImagePreviewField, VideoPreviewField

    class Movie(models.Model):
        ...
        cover = ImagePreviewField()
        video = VideoPreviewField()

```

License
-------

MIT
