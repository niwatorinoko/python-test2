from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://python.org/')

# Select an Element with a CSS Selector (learn more):
about = r.html.find('#about', first=True)

# Grab an Element’s text contents:
print(about.text)

# Introspect an Element’s attributes (learn more):
print(about.attrs)
# {'id': 'about', 'class': ('tier-1', 'element-1'), 'aria-haspopup': 'true'}

# Render out an Element’s HTML:
print(about.html)

# Crab an Element’s root tag name:
print(about.tag)

# Select an Element list within an Element
print(about.find('a'))

# Search for text on the page:
match = r.html.search('Python is a {} language')[0]
print(match)

# Select only elements containing certain text:
matches = r.html.find('a', containing='Started')
print(matches)