"""
Utility functions for generating "bacon ipsum" filler text.
"""

# Bacon Ipsum for Django
#
# Inspired by django.contrib.webdesign
# and Pete Nelson's http://baconipsum.com/ source code at https://github.com/petenelson/bacon-ipsum/
# built by rhfung at http://www.yetihq.com/
#
# March 2013
# MIT license


from __future__ import unicode_literals

import random

COMMON_P = 'Bacon ipsum dolor sit amet pork venison kielbasa, pork chop ham hock meatloaf frankfurter chicken shank tri-tip strip steak salami meatball. Shank t-bone doner pork chop meatball flank leberkas venison. Doner ham pork shankle turkey meatball tenderloin salami prosciutto tail. Meatball bresaola jerky shank leberkas prosciutto. Prosciutto venison boudin, bacon drumstick brisket sausage swine pork belly pork loin andouille chuck chicken short loin. Short ribs pork belly frankfurter doner chuck pastrami, capicola shankle beef flank. Boudin short loin turkey corned beef ham hock pastrami tenderloin beef ribs shank pork tongue prosciutto pancetta spare ribs sausage.'

WORDS = ('beef',
         'chicken',
         'pork',
         'bacon',
         'chuck',
         'short loin',
         'sirloin',
         'shank',
         'flank',
         'sausage',
         'pork belly',
         'shoulder',
         'cow',
         'pig',
         'ground round',
         'hamburger',
         'meatball',
         'tenderloin',
         'strip steak',
         't-bone',
         'ribeye',
         'shankle',
         'tongue',
         'tail',
         'pork chop',
         'pastrami',
         'corned beef',
         'jerky',
         'ham',
         'fatback',
         'ham hock',
         'pancetta',
         'pork loin',
         'short ribs',
         'spare ribs',
         'beef ribs',
         'drumstick',
         'tri-tip',
         'ball tip',
         'venison',
         'turkey',
         'biltong',
         'rump',
         'jowl',
         'salami',
         'bresaola',
         'meatloaf',
         'brisket',
         'boudin',
         'andouille',
         'capicola',
         'swine',
         'kielbasa',
         'frankfurter',
         'prosciutto',
         'filet mignon',
         'leberkas',
         'turducken',
         'doner')

COMMON_WORDS = ('consectetur',
                'adipisicing',
                'elit',
                'sed',
                'do',
                'eiusmod',
                'tempor',
                'incididunt',
                'ut',
                'labore',
                'et',
                'dolore',
                'magna',
                'aliqua',
                'ut',
                'enim',
                'ad',
                'minim',
                'veniam',
                'quis',
                'nostrud',
                'exercitation',
                'ullamco',
                'laboris',
                'nisi',
                'ut',
                'aliquip',
                'ex',
                'ea',
                'commodo',
                'consequat',
                'duis',
                'aute',
                'irure',
                'dolor',
                'in',
                'reprehenderit',
                'in',
                'voluptate',
                'velit',
                'esse',
                'cillum',
                'dolore',
                'eu',
                'fugiat',
                'nulla',
                'pariatur',
                'excepteur',
                'sint',
                'occaecat',
                'cupidatat',
                'non',
                'proident',
                'sunt',
                'in',
                'culpa',
                'qui',
                'officia',
                'deserunt',
                'mollit',
                'anim',
                'id',
                'est',
                'laborum',

)

def sentence():
    """
    Returns a randomly generated sentence of bacon ipsum text.

    The first word is capitalized, and the sentence ends in either a period or
    question mark. Commas are added at random.
    """
    # Determine the number of comma-separated sections and number of words in
    # each section for this sentence.
    sections = [' '.join(random.sample(WORDS, random.randint(3, 12))) for i in range(random.randint(1, 5))]
    s = ', '.join(sections)
    # Convert to sentence case and add end punctuation.
    return '%s%s%s' % (s[0].upper(), s[1:], random.choice('?.'))

def paragraph():
    """
    Returns a randomly generated paragraph of bacon ipsum text.

    The paragraph consists of between 1 and 4 sentences, inclusive.
    """
    return ' '.join([sentence() for i in range(random.randint(1, 4))])

def paragraphs(count, common=True):
    """
    Returns a list of paragraphs as returned by paragraph().

    If `common` is True, then the first paragraph will be the standard
    'bacon ipsum' paragraph. Otherwise, the first paragraph will be random
    Latin text. Either way, subsequent paragraphs will be random Latin text.
    """
    paras = []
    for i in range(count):
        if common and i == 0:
            paras.append(COMMON_P)
        else:
            paras.append(paragraph())
    return paras

def words(count, common=True):
    """
    Returns a string of `count` bacon ipsum words separated by a single space.
    """
    if common:
        word_list = list(WORDS) # don't support common words
    else:
        word_list = []
    c = len(word_list)
    if count > c:
        count -= c
        while count > 0:
            c = min(count, len(WORDS))
            count -= c
            word_list += random.sample(WORDS, c)
    else:
        word_list = word_list[:count]
    return ' '.join(word_list)
