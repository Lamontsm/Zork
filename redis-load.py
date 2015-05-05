# Loading up the Redis database for the game. Run once.
#
# run the following in terminal before running this program:
#
#sudo service redis-server start
#sudo pip install redis
#
import os

import redis

r = redis.Redis()
#
#wipe out earlier entries to Redis
#
r.flushdb()
#
#show a simple assignment
#

#
room="hallway"
r.set(room + ":north", 'ballroom')
r.set(room + ':description', 'You are in a large hallway in a stone castle. You see a large and ferocious \
dragon guarding a golden key. You see a large doorway on the north wall.')
r.set(room + ':graphic','/images/hallway.jpg')
room='ballroom'
r.set(room + ":south", 'hallway')
r.set(room + ':description', 'You are in a large ballroom with many hanging curtains. There is a huge ogre \
guarding a golden sword. There is a door on the south wall and another on the east wall.')
r.set(room + ':graphic', '/images/ballroom.jpg')
