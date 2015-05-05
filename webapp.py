#
# Run sudo pip install bottle in terminal before running program
#
from bottle import route, run, template, static_file, get, request
# Loading up the Redis database for the game. Run once.
#
# run the following in terminal before running this program:
#
#sudo service redis-server start
#sudo pip install redis
#

import redis
r = redis.Redis()
import os

# Initialize boolean to process first pass differently
is_first_pass = True
user = ''

#Returns static image files whenever a request is made to /images
@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

@get('/css/<filename:re:.*\.(css)>')
def css(filename):
    return static_file(filename, root='css')
    
@route('/')
@route('/index.html')
def index():
    return static_file("index.html", root='./')

@route('/Command', method='POST')
def Command():
    global is_first_pass
    global user
    if is_first_pass:
        # Is first time loading page. Use first-time commmands
        user = str(request.forms.get('user'))
        room = 'hallway'
        r.set(user + ':room',room)
        newgraphic= r.get(room + ':graphic')
        is_first_pass = False
        inventory = ['bandaids','baling wire']
        r.set(user + ':inventory',inventory)
        return template('getcommand',text=r.get(room + ':description'),user=user, graphic=newgraphic, inventory=inventory,error='')
    else:
        # Is not first time loading page. Get and use commmands
        command = request.forms.get('command')
        if command == 'go north':
            room = r.get(r.get(user + ':room') + ':north')
            newgraphic= r.get(room + ':graphic')
            text = r.get(room + ':description')
            inventory = ['apple', 'mango']
            return template('getcommand',text=text, user=user, graphic=newgraphic, inventory=inventory,error='')
        elif command == 'quit':
            return template('GameOver',user=user)
        else:
            # Pretend it is an invalid command
            error_text = 'Please enter valid command of either go north or quit'
            room = r.get(user + ':room')
            newgraphic= r.get(room + ':graphic')
            text = r.get(room + ':description')
            inventory = ['apple', 'mango','tomato']
            return template('getcommand',text=r.get(room + ':description'),user=user, graphic=newgraphic, inventory=inventory,error=error_text)
        
    

# start server and listen for requests on Cloud9 - Don't Change This
run(host=os.environ["IP"], port=int(os.environ["PORT"]), debug=True)
