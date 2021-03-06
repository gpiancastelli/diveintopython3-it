#!/usr/bin/python2.6

from pyquery import PyQuery as pq
import glob
import sys

# These selectors are kept regardless of whether this script thinks they are used.
# Most of these match nodes that are dynamically inserted or manipulated by script
# after the page has loaded, which is why a static analysis thinks they're unused.
SELECTOR_EXCEPTIONS = ('.w', '.b', '.str', '.kwd', '.com', '.typ', '.lit', '.pun', '.tag', '.atn', '.atv', '.dec', 'pre .u', 'pre .u span', 'td .u', 'li ol', 'a.hl:link', 'a.hl:visited', 'a.hl:hover', 'h2[id]:hover a.hl', 'h3[id]:hover a.hl')

filename = sys.argv[1]
cssfilename = sys.argv[2]
pqd = pq(filename=filename)

with open(filename, 'rb') as fopen:
    raw_data = fopen.read()

#if raw_data.count('</a><script src=j/'): # HACK HACK HACK
if raw_data.count('<pre'): # revert HACK because it doesn't work for me
    def keep(s):
        for selector in SELECTOR_EXCEPTIONS:
            if s == selector: return True
            if s.startswith(selector + ' '): return True
        return False
else:
    def keep(s):
        return False

with open(cssfilename, 'rb') as fopen:
    original_css = fopen.read()

new_css = ''
for rule in original_css.split('}')[:-1]:
    selectors, properties = rule.split('{', 1)
    selectors = ','.join([s for s in selectors.split(',') if keep(s) or pqd(s.split(':', 1)[0])])
    if selectors:
        new_css += '%s{%s}' % (selectors, properties)

sys.stdout.write(new_css)
