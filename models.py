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

# Comment and uncomment with "ctl" + "/""
# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         search_term = self.request.get('q')
#         if search_term:
#             lterm = search_term.lower()
#             # create key
#             key = ndb.Key('UserSearch', lterm)
#             # Read database
#             search = key.get()
#             if not search:
#                 # Create if not there
#                 search = UserSearch(
#                     key=key, count=0,
#                     term=search_term)
#             # Update count
#             search.increment()
#             # Save
#             search.put()
#         else:
#             search_term = "coffee"
#         params = {'term': search_term,
#                   'location': 'San Marcos, California'}
#         form_data = urllib.urlencode(params)
#         api_url = 'https://api.yelp.com/v3/businesses/search?' + form_data
#
#         # Add your own API key
#         request = urllib2.Request(api_url, headers={"Authorization" : "Bearer API_KEY"})
#         response = urllib2.urlopen(request).read()
#         content = json.loads(response)
#
#         template = jinja_environment.get_template('main.html')
#         variables = {'content': content,
#                      'q': search_term}
#         self.response.write(template.render(variables))
