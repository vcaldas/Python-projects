
import collections

# Creating Dictionaries
lookup = {}
lookup = dict()
lookup = {'age':42, 'loc':'Italy'}
lookup = dict(age=42, loc='Italy')

print(lookup)
print(lookup['loc'])

cat = 'cat'
lookup['cat'] = 'Fun code demos'
if cat in lookup:
    print(lookup[cat])

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

mage = Wizard('mage', 10)
print(mage)
print(mage.__dict__)



User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
    ]


lookup = dict()

for u in users:
    lookup[u.id] = u

print(lookup[1])
