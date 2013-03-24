from distutils.core import setup

setup(
    name='django-bacon-ipsum',
    version='0.1',
    author=u'Richard Fung',
    author_email='richard@yetihq.com',
    packages=find_packages(),
    url='http://github.com/YetiHQ/django-bacon-ipsum',
    license='MIT license, see LICENSE',
    description='An alternative to lorem ipsum filler text.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
