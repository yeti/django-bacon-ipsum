# Bacon Ipsum for Django
#
# Inspired by django.contrib.webdesign
# and Pete Nelson's http://baconipsum.com/ source code at https://github.com/petenelson/bacon-ipsum/
# built by rhfung at http://www.yetihq.com/
#
# March 2013
# MIT license

from __future__ import unicode_literals

from bacon.bacon_ipsum import words, paragraphs
from django import template

register = template.Library()

class BaconNode(template.Node):
    def __init__(self, count, method, common):
        self.count, self.method, self.common = count, method, common

    def render(self, context):
        try:
            count = int(self.count.resolve(context))
        except (ValueError, TypeError):
            count = 1
        if self.method == 'w':
            return words(count, common=self.common)
        else:
            paras = paragraphs(count, common=self.common)
        if self.method == 'p':
            paras = ['<p>%s</p>' % p for p in paras]
        return '\n\n'.join(paras)

@register.tag
def bacon(parser, token):
    """
    Creates random Latin text useful for providing test data in templates.

    Usage format::

        {% bacon [count] [method] %}

    ``count`` is a number (or variable) containing the number of paragraphs or
    words to generate (default is 1).

    ``method`` is either ``w`` for words, ``p`` for HTML paragraphs, ``b`` for
    plain-text paragraph blocks (default is ``b``).

    Examples:
        * ``{% bacon %}`` will output the common "bacon ipsum" paragraph
        * ``{% bacon 3 p %}`` will output the common "bacon ipsum" paragraph
          and two random paragraphs each wrapped in HTML ``<p>`` tags
        * ``{% bacon 2 w %}`` will output two random latin words
    """
    bits = list(token.split_contents())
    tagname = bits[0]
    # Random bit
    common = bits[-1] != 'random'
    if not common:
        bits.pop()
    # Method bit
    if bits[-1] in ('w', 'p', 'b'):
        method = bits.pop()
    else:
        method = 'b'
    # Count bit
    if len(bits) > 1:
        count = bits.pop()
    else:
        count = '1'
    count = parser.compile_filter(count)
    if len(bits) != 1:
        raise template.TemplateSyntaxError("Incorrect format for %r tag" % tagname)
    return BaconNode(count, method, common)
