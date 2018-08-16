#
#   models.py
#   WelomeSanDiego
#
#   Created by Alexander Garcia on 8/13/18.
#   Copyright 2018 BreakingCode. All rights reserved.
#

import config
from google.appengine.ext import ndb

class UserSearch(ndb.Model):
    term = ndb.StringProperty(required=True)
    count = ndb.IntegerProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
    
    def increment(self):
        self.count = self.count + 1

    def encode_term(self):
        return urllib.urlencode({'q': self.term})

@ndb.transactional
def updateSearchCount(term):
    lterm = term.lower()
    # create key
    key = ndb.Key('UserSearch', lterm)
    # Read database
    search = key.get()
    if not search:
        # Create if not there
        search = UserSearch(key=key, count=0, term=term)
    # Update count
    search.increment()
    # Save
    search.put()


def increment(self):
    self.count = self.count + 1

def encode_term(self):
    return urllib.urlencode({'q': self.term})
