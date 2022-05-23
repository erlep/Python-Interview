# Is asyncio too hard to use? Try Trio! - https://bit.ly/37yRrZN

import requests
import time

urls = [
    # 'http://www.facebook.com',
    # 'http://www.twitter.com',
    # 'http://www.instagram.com',
    # 'http://www.google.com',
    # 'http://www.youtube.com',
    'http://www.medium.com',
    'https://git-scm.com',
    'http://www.github.com',
    'http://www.gitlab.com',
    'http://www.python.org',
    'http://python-requests.org',
    'http://trio.readthedocs.io'
]

start_time = time.time()
for url in urls:
  print("Start: ", url)
  response = requests.get(url)
  print("Finished: ", url, len(response.content))

print("Total time:", time.time() - start_time)
