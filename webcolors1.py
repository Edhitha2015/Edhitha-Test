"""
Utility functions for working with the color names and color value
formats defined by the HTML and CSS specifications for use in
documents on the Web.


What this module supports
-------------------------

This module supports the following methods of specifying sRGB colors,
and conversions between them:

* Six-digit hexadecimal.

* Three-digit hexadecimal.

* Integer ``rgb()`` triplet.

* Percentage ``rgb()`` triplet.

* Varying selections of predefined color names.

This module does not support ``hsl()`` triplets, nor does it support
opacity/alpha-channel information via ``rgba()`` or ``hsla()``.

If you need to convert between RGB-specified colors and HSL-specified
colors, or colors specified via other means, consult `the colorsys
module`_ in the Python standard library, which can perform conversions
amongst several common color systems.

.. _the colorsys module: http://docs.python.org/library/colorsys.html


Normalization and conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For colors specified via hexadecimal values, this module will accept
input in the following formats:

* A hash mark (#) followed by three hexadecimal digits, where digits
  A-F may be upper- or lower-case.

* A hash mark (#) followed by six hexadecimal digits, where digits A-F
  may be upper- or lower-case.

For output which consists of a color specified via hexadecimal values,
and for functions which perform intermediate conversion to hexadecimal
before returning a result in another format, this module always
normalizes such values to the following format:

* A hash mark (#) followed by six hexadecimal digits, with digits A-F
  forced to lower-case.

The function :func:`normalize_hex` in this module can be used to
perform this normalization manually if desired.

For colors specified via predefined names, this module will accept
input in the following formats:

* An entirely lower-case name, such as ``aliceblue``.

* A name using CamelCase, such as ``AliceBlue``.

For output which consists of a color specified via a predefined name,
and for functions which perform intermediate conversion to a
predefined name before returning a result in another format, this
module always normalizes such values to be entirely lower-case.

For colors specified via ``rgb()`` triplets, values contained in the
triplets will be normalized via clipping in accordance with CSS:

* Integer values less than 0 will be normalized to 0, and percentage
  values less than 0% will be normalized to 0%.

* Integer values greater than 255 will be normalized to 255, and
  percentage values greater than 100% will be normalized to 100%.

The functions :func:`normalize_integer_triplet` and
:func:`normalize_percent_triplet` in this module can be used to
perform this normalization manually if desired.

For purposes of identifying the specification from which to draw the
selection of defined color names, this module recognizes the following
identifiers:

``html4``
    The HTML 4 named colors.

``css2``
    The CSS 2 named colors.

``css21``
    The CSS 2.1 named colors.

``css3``
    The CSS 3/SVG named colors.

The CSS 1 specification is not represented here, as it merely
"suggested" a set of color names, and declined to provide values for
them.


Mappings of color names
-----------------------

For each set of defined color names -- HTML 4, CSS 2, CSS 2.1 and CSS
3 -- this module exports two mappings: one of normalized color names
to normalized hexadecimal values, and one of normalized hexadecimal
values to normalized color names. These eight mappings are as follows:

``html4_names_to_hex``
    Mapping of normalized HTML 4 color names to normalized hexadecimal
    values.

``html4_hex_to_names``
    Mapping of normalized hexadecimal values to normalized HTML 4
    color names.

``css2_names_to_hex``
    Mapping of normalized CSS 2 color names to normalized hexadecimal
    values. Because CSS 2 defines the same set of named colors as HTML
    4, this is merely an alias for ``html4_names_to_hex``.

``css2_hex_to_names``
    Mapping of normalized hexadecimal values to normalized CSS 2 color
    nams. For the reasons described above, this is merely an alias for
    ``html4_hex_to_names``.

``css21_names_to_hex``
    Mapping of normalized CSS 2.1 color names to normalized
    hexadecimal values. This is identical to ``html4_names_to_hex``,
    except for one addition: ``orange``.

``css21_hex_to_names``
    Mapping of normalized hexadecimal values to normalized CSS 2.1
    color names. As above, this is identical to ``html4_hex_to_names``
    except for the addition of ``orange``.

``css3_names_to_hex``
    Mapping of normalized CSS3 color names to normalized hexadecimal
    values.

``css3_hex_to_names``
    Mapping of normalized hexadecimal values to normalized CSS3 color
    names.

"""

import math
import re


def _reversedict(d):
    """
    Internal helper for generating reverse mappings; given a
    dictionary, returns a new dictionary with keys and values swapped.

    """
    return dict(list(zip(list(d.values()), list(d.keys()))))


HEX_COLOR_RE = re.compile(r'^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')

SUPPORTED_SPECIFICATIONS = ('html4', 'css2', 'css21', 'css3')


# Mappings of color names to normalized hexadecimal color values.
#################################################################
html4_names_to_hex = {'blue34': '#00ffff',
                      'black1': '#000000',
                      'blue35': '#0000ff',
                      'pink1': '#ff00ff',
                      'green1': '#008000',
                      'gray1': '#808080',
                      'yellow1': '#00ff00',
                      'maroon': '#800000',
                      'blue36': '#000080',
                      'green2': '#808000',
                      'purple1': '#800080',
                      'red1': '#ff0000',
                      'gray2': '#c0c0c0',
                      'teal': '#008080',
                      'white1': '#ffffff',
                      'yellow2': '#ffff00'}

css2_names_to_hex = html4_names_to_hex

css21_names_to_hex = dict(html4_names_to_hex, orange1='#ffa500')
css3_names_to_hex = {'blue1': '#00ffff',
                     'blue2': '#f0f8ff',
                     'blue3': '#faebd7',
                     'blue4': '#00ffff',
                     'blue5': '#7fffd4',
                     'blue6': '#f0ffff',
                     'cream1': '#f5f5dc',
                     'cream2': '#ffe4c4',
                     'black2': '#000000',
                     'cream3': '#ffebcd',
                     'blue7': '#0000ff',
                     'blue8': '#8a2be2',
                     'brown1': '#a52a2a',
                     'cream4': '#deb887',
                     'blue9': '#5f9ea0',
                     'green3': '#7fff00',
                     'brown2': '#d2691e',
                     'coral': '#ff7f50',
                     'blue10': '#6495ed',
                     'white2': '#fff8dc',
                     'red2': '#dc143c',
                     'blue11': '#00ffff',
                     'blue12': '#00008b',
                     'blue13': '#008b8b',
                     'brown3': '#b8860b',
                     'gray3': '#a9a9a9',
                     'green4': '#006400',
                     'darkkhaki': '#bdb76b',
                     'pink2': '#8b008b',
                     'green5': '#556b2f',
                     'orange2': '#ff8c00',
                     'purple2': '#9932cc',
                     'red3': '#8b0000',
                     'darksalmon': '#e9967a',
                     'green6': '#8fbc8f',
                     'blue14': '#483d8b',
                     'gray4': '#2f4f4f',
                     'blue15': '#00ced1',
                     'violet3': '#9400d3',
                     'pink3': '#ff1493',
                     'blue16': '#00bfff',
                     'gray5': '#696969',
                     'blue17': '#1e90ff',
                     'red4': '#b22222',
                     'white3': '#fffaf0',
                     'green7': '#228b22',
                     'pink4': '#ff00ff',
                     'gray6': '#dcdcdc',
                     'white4': '#f8f8ff',
                     'yellow3': '#ffd700',
                     'yellow4': '#daa520',
                     'gray7': '#808080',
                     'green8': '#008000',
                     'green9': '#adff2f',
                     'green10': '#f0fff0',
                     'pink5': '#ff69b4',
                     'red5': '#cd5c5c',
                     'indigo': '#4b0082',
                     'white5': '#fffff0',
                     'yellow5': '#f0e68c',
                     'violet1': '#e6e6fa',
                     'pink6': '#fff0f5',
                     'green11': '#7cfc00',
                     'yellow6': '#fffacd',
                     'blue18': '#add8e6',
                     'lightcoral': '#f08080',
                     'blue19': '#e0ffff',
                     'yellow7': '#fafad2',
                     'gray8': '#d3d3d3',
                     'green12': '#90ee90',
                     'pink7': '#ffb6c1',
                     'orange3': '#ffa07a',
                     'green13': '#20b2aa',
                     'blue20': '#87cefa',
                     'gray9': '#778899',
                     'gray10': '#b0c4de',
                     'cream5': '#ffffe0',
                     'green14': '#00ff00',
                     'green15': '#32cd32',
                     'cream6': '#faf0e6',
                     'red6': '#ff00ff',
                     'maroon': '#800000',
                     'green16': '#66cdaa',
                     'blue21': '#0000cd',
                     'purple3': '#ba55d3',
                     'purple4': '#9370d8',
		     'purple5':'#9370db',
                     'green17': '#3cb371',
                     'blue22': '#7b68ee',
                     'green18': '#00fa9a',
                     'blue23': '#48d1cc',
                     'pink8': '#c71585',
                     'blue24': '#191970',
                     'green19': '#f5fffa',
                     'cream7': '#ffe4e1',
                     'cream8': '#ffe4b5',
                     'cream9': '#ffdead',
                     'blue25': '#000080',
                     'cream10': '#fdf5e6',
                     'green20': '#808000',
                     'green21': '#6b8e23',
                     'orange4': '#ffa500',
                     'orange5': '#ff4500',
                     'purple6': '#da70d6',
                     'yellow8': '#eee8aa',
                     'green22': '#98fb98',
                     'blue26': '#afeeee',
                     'pink9': '#d87093',
                     'cream11': '#ffefd5',
                     'cream12': '#ffdab9',
                     'brown4': '#cd853f',
                     'pink10': '#ffc0cb',
                     'purple7': '#dda0dd',
                     'blue27': '#b0e0e6',
                     'purple8': '#800080',
                     'red7': '#ff0000',
                     'brown5': '#bc8f8f',
                     'blue28': '#4169e1',
                     'brown6': '#8b4513',
                     'orange6': '#fa8072',
                     'brown7': '#f4a460',
                     'green23': '#2e8b57',
                     'cream13': '#fff5ee',
                     'brown8': '#a0522d',
                     'gray11': '#c0c0c0',
                     'blue29': '#87ceeb',
                     'blue30': '#6a5acd',
                     'gray12': '#708090',
                     'white6': '#fffafa',
                     'green24': '#00ff7f',
                     'blue31': '#4682b4',
                     'brown9': '#d2b48c',
                     'blue32': '#008080',
                     'purple9': '#d8bfd8',
                     'orange7': '#ff6347',
                     'blue33': '#40e0d0',
                     'violet2': '#ee82ee',
                     'cream14': '#f5deb3',
                     'white7': '#ffffff',
                     'white8': '#f5f5f5',
                     'yellow9': '#ffff00',
                     'green25': '#9acd32'}




# Mappings of normalized hexadecimal color values to color names.
#################################################################

html4_hex_to_names = _reversedict(html4_names_to_hex)

css2_hex_to_names = html4_hex_to_names

css21_hex_to_names = _reversedict(css21_names_to_hex)

css3_hex_to_names = _reversedict(css3_names_to_hex)


# Normalization routines.
#################################################################

def normalize_hex(hex_value):
    """
    Normalize a hexadecimal color value to the following form and
    return the result::

        #[a-f0-9]{6}

    In other words, the following transformations are applied as
    needed:

    * If the value contains only three hexadecimal digits, it is
      expanded to six.

    * The value is normalized to lower-case.

    If the supplied value cannot be interpreted as a hexadecimal color
    value, ``ValueError`` is raised.

    Examples:

    >>> normalize_hex('#0099cc')
    '#0099cc'
    >>> normalize_hex('#0099CC')
    '#0099cc'
    >>> normalize_hex('#09c')
    '#0099cc'
    >>> normalize_hex('#09C')
    '#0099cc'
    >>> normalize_hex('0099cc')
    Traceback (most recent call last):
        ...
    ValueError: '0099cc' is not a valid hexadecimal color value.

    """
    try:
        hex_digits = HEX_COLOR_RE.match(hex_value).groups()[0]
    except AttributeError:
        raise ValueError("'%s' is not a valid hexadecimal color value." % hex_value)
    if len(hex_digits) == 3:
        hex_digits = ''.join([2 * s for s in hex_digits])
    return '#%s' % hex_digits.lower()


def normalize_integer_triplet(rgb_triplet):
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    Examples:

    >>> normalize_integer_triplet((128, 128, 128))
    (128, 128, 128)
    >>> normalize_integer_triplet((0, 0, 0))
    (0, 0, 0)
    >>> normalize_integer_triplet((255, 255, 255))
    (255, 255, 255)
    >>> normalize_integer_triplet((270, -20, 128))
    (255, 0, 128)
    
    """
    return tuple([_normalize_integer_rgb(value) for value in rgb_triplet])


def _normalize_integer_rgb(value):
    """
    Normalize ``value`` for use in an integer ``rgb()`` triplet, as follows:
    
    * If ``value`` is less than 0, convert to 0.
    
    * If ``value`` is greater than 255, convert to 255.

    Examples:

    >>> _normalize_integer_rgb(0)
    0
    >>> _normalize_integer_rgb(255)
    255
    >>> _normalize_integer_rgb(128)
    128
    >>> _normalize_integer_rgb(-20)
    0
    >>> _normalize_integer_rgb(270)
    255
    
    """
    if 0 <= value <= 255:
        return value
    if value < 0:
        return 0
    if value > 255:
        return 255


def normalize_percent_triplet(rgb_triplet):
    """
    Normalize a percentage ``rgb()`` triplet to that all values are
    within the range 0%-100% inclusive.

    Examples:

    >>> normalize_percent_triplet(('50%', '50%', '50%'))
    ('50%', '50%', '50%')
    >>> normalize_percent_triplet(('0%', '100%', '0%'))
    ('0%', '100%', '0%')
    >>> normalize_percent_triplet(('-10%', '250%', '500%'))
    ('0%', '100%', '100%')
    
    """
    return tuple([_normalize_percent_rgb(value) for value in rgb_triplet])
    

def _normalize_percent_rgb(value):
    """
    Normalize ``value`` for use in a percentage ``rgb()`` triplet, as
    follows:

    * If ``value`` is less than 0%, convert to 0%.

    * If ``value`` is greater than 100%, convert to 100%.

    Examples:

    >>> _normalize_percent_rgb('0%')
    '0%'
    >>> _normalize_percent_rgb('100%')
    '100%'
    >>> _normalize_percent_rgb('62%')
    '62%'
    >>> _normalize_percent_rgb('-5%')
    '0%'
    >>> _normalize_percent_rgb('250%')
    '100%'
    >>> _normalize_percent_rgb('85.49%')
    '85.49%'
    
    """
    percent = value.split('%')[0]
    percent = float(percent) if '.' in percent else int(percent)
    
    if 0 <= percent <= 100:
        return '%s%%' % percent
    if percent < 0:
        return '0%'
    if percent > 100:
        return '100%'
    

# Conversions from color names to various formats.
#################################################################

def name_to_hex(name, spec='css3'):
    """
    Convert a color name to a normalized hexadecimal color value.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    The color name will be normalized to lower-case before being
    looked up, and when no color of that name exists in the given
    specification, ``ValueError`` is raised.

    Examples:

    >>> name_to_hex('white')
    '#ffffff'
    >>> name_to_hex('navy')
    '#000080'
    >>> name_to_hex('goldenrod')
    '#daa520'
    >>> name_to_hex('goldenrod', spec='html4')
    Traceback (most recent call last):
        ...
    ValueError: 'goldenrod' is not defined as a named color in html4.
    >>> name_to_hex('goldenrod', spec='css5')
    Traceback (most recent call last):
        ...
    TypeError: 'css5' is not a supported specification for color name lookups; supported specifications are: html4, css2, css21, css3.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise TypeError("'%s' is not a supported specification for color name lookups; supported specifications are: %s." % (spec,
                                                                                                                             ', '.join(SUPPORTED_SPECIFICATIONS)))
    normalized = name.lower()
    try:
        hex_value = globals()['%s_names_to_hex' % spec][normalized]
    except KeyError:
        raise ValueError("'%s' is not defined as a named color in %s." % (name, spec))
    return hex_value


def name_to_rgb(name, spec='css3'):
    """
    Convert a color name to a 3-tuple of integers suitable for use in
    an ``rgb()`` triplet specifying that color.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    The color name will be normalized to lower-case before being
    looked up, and when no color of that name exists in the given
    specification, ``ValueError`` is raised.

    Examples:

    >>> name_to_rgb('white')
    (255, 255, 255)
    >>> name_to_rgb('navy')
    (0, 0, 128)
    >>> name_to_rgb('goldenrod')
    (218, 165, 32)

    """
    return hex_to_rgb(name_to_hex(name, spec=spec))


def name_to_rgb_percent(name, spec='css3'):
    """
    Convert a color name to a 3-tuple of percentages suitable for use
    in an ``rgb()`` triplet specifying that color.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    The color name will be normalized to lower-case before being
    looked up, and when no color of that name exists in the given
    specification, ``ValueError`` is raised.

    Examples:

    >>> name_to_rgb_percent('white')
    ('100%', '100%', '100%')
    >>> name_to_rgb_percent('navy')
    ('0%', '0%', '50%')
    >>> name_to_rgb_percent('goldenrod')
    ('85.49%', '64.71%', '12.5%')

    """
    return rgb_to_rgb_percent(name_to_rgb(name, spec=spec))


# Conversions from hexadecimal color values to various formats.
#################################################################

def hex_to_name(hex_value, spec='css3'):
    """
    Convert a hexadecimal color value to its corresponding normalized
    color name, if any such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    The hexadecimal value will be normalized before being looked up,
    and when no color name for the value is found in the given
    specification, ``ValueError`` is raised.

    Examples:

    >>> hex_to_name('#ffffff')
    'white'
    >>> hex_to_name('#fff')
    'white'
    >>> hex_to_name('#000080')
    'navy'
    >>> hex_to_name('#daa520')
    'goldenrod'
    >>> hex_to_name('#daa520', spec='html4')
    Traceback (most recent call last):
        ...
    ValueError: '#daa520' has no defined color name in html4.
    >>> hex_to_name('#daa520', spec='css5')
    Traceback (most recent call last):
        ...
    TypeError: 'css5' is not a supported specification for color name lookups; supported specifications are: html4, css2, css21, css3.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise TypeError("'%s' is not a supported specification for color name lookups; supported specifications are: %s." % (spec,
                                                                                                                             ', '.join(SUPPORTED_SPECIFICATIONS)))
    normalized = normalize_hex(hex_value)
    try:
        name = globals()['%s_hex_to_names' % spec][normalized]
    except KeyError:
        raise ValueError("'%s' has no defined color name in %s." % (hex_value, spec))
    return name


def hex_to_rgb(hex_value):
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.

    The hexadecimal value will be normalized before being converted.

    Examples:

    >>> hex_to_rgb('#fff')
    (255, 255, 255)
    >>> hex_to_rgb('#000080')
    (0, 0, 128)

    """
    hex_digits = normalize_hex(hex_value)
    return tuple([int(s, 16) for s in (hex_digits[1:3], hex_digits[3:5], hex_digits[5:7])])


def hex_to_rgb_percent(hex_value):
    """
    Convert a hexadecimal color value to a 3-tuple of percentages
    suitable for use in an ``rgb()`` triplet representing that color.

    The hexadecimal value will be normalized before converting.

    Examples:

    >>> hex_to_rgb_percent('#ffffff')
    ('100%', '100%', '100%')
    >>> hex_to_rgb_percent('#000080')
    ('0%', '0%', '50%')

    """
    return rgb_to_rgb_percent(hex_to_rgb(hex_value))


# Conversions from  integer rgb() triplets to various formats.
#################################################################

def rgb_to_name(rgb_triplet, spec='css3'):
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    If there is no matching name, ``ValueError`` is raised.

    Examples:

    >>> rgb_to_name((255, 255, 255))
    'white'
    >>> rgb_to_name((0, 0, 128))
    'navy'

    """
    return hex_to_name(rgb_to_hex(normalize_integer_triplet(rgb_triplet)), spec=spec)


def rgb_to_hex(rgb_triplet):
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.

    Examples:

    >>> rgb_to_hex((255, 255, 255))
    '#ffffff'
    >>> rgb_to_hex((0, 0, 128))
    '#000080'

    """
    return '#%02x%02x%02x' % normalize_integer_triplet(rgb_triplet)


def rgb_to_rgb_percent(rgb_triplet):
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of percentages suitable for use in
    representing that color.

    This function makes some trade-offs in terms of the accuracy of
    the final representation; for some common integer values,
    special-case logic is used to ensure a precise result (e.g.,
    integer 128 will always convert to '50%', integer 32 will always
    convert to '12.5%'), but for all other values a standard Python
    ``float`` is used and rounded to two decimal places, which may
    result in a loss of precision for some values.

    Examples:

    >>> rgb_to_rgb_percent((255, 255, 255))
    ('100%', '100%', '100%')
    >>> rgb_to_rgb_percent((0, 0, 128))
    ('0%', '0%', '50%')
    >>> rgb_to_rgb_percent((218, 165, 32))
    ('85.49%', '64.71%', '12.5%')

    """
    # In order to maintain precision for common values,
    # 256 / 2**n is special-cased for values of n
    # from 0 through 4, as well as 0 itself.
    specials = {255: '100%', 128: '50%', 64: '25%',
                 32: '12.5%', 16: '6.25%', 0: '0%'}
    return tuple([specials.get(d, '%.02f%%' % ((d / 255.0) * 100)) \
                  for d in normalize_integer_triplet(rgb_triplet)])


# Conversions from percentage rgb() triplets to various formats.
#################################################################

def rgb_percent_to_name(rgb_percent_triplet, spec='css3'):
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used; valid values are
    ``html4``, ``css2``, ``css21`` and ``css3``, and the default is
    ``css3``.

    If there is no matching name, ``ValueError`` is raised.

    Examples:

    >>> rgb_percent_to_name(('100%', '100%', '100%'))
    'white'
    >>> rgb_percent_to_name(('0%', '0%', '50%'))
    'navy'
    >>> rgb_percent_to_name(('85.49%', '64.71%', '12.5%'))
    'goldenrod'

    """
    return rgb_to_name(rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet)), spec=spec)


def rgb_percent_to_hex(rgb_percent_triplet):
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal color value for that
    color.

    Examples:

    >>> rgb_percent_to_hex(('100%', '100%', '0%'))
    '#ffff00'
    >>> rgb_percent_to_hex(('0%', '0%', '50%'))
    '#000080'
    >>> rgb_percent_to_hex(('85.49%', '64.71%', '12.5%'))
    '#daa520'

    """
    return rgb_to_hex(rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet)))


def _percent_to_integer(percent):
    """
    Internal helper for converting a percentage value to an integer
    between 0 and 255 inclusive.

    """
    num = float(percent.split('%')[0]) / 100.0 * 255
    e = num - math.floor(num)
    return e < 0.5 and int(math.floor(num)) or int(math.ceil(num))


def rgb_percent_to_rgb(rgb_percent_triplet):
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of integers suitable for use in
    representing that color.

    Some precision may be lost in this conversion. See the note
    regarding precision for ``rgb_to_rgb_percent()`` for details;
    generally speaking, the following is true for any 3-tuple ``t`` of
    integers in the range 0...255 inclusive::

        t == rgb_percent_to_rgb(rgb_to_rgb_percent(t))

    Examples:

    >>> rgb_percent_to_rgb(('100%', '100%', '100%'))
    (255, 255, 255)
    >>> rgb_percent_to_rgb(('0%', '0%', '50%'))
    (0, 0, 128)
    >>> rgb_percent_to_rgb(('85.49%', '64.71%', '12.5%'))
    (218, 165, 32)

    """
    return tuple(map(_percent_to_integer, normalize_percent_triplet(rgb_percent_triplet)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
