from flask import Flask
server = Flask(__name__)
@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Temperature and Light Intensity</h1></body></html>"

@server.post('/temperature/<float:temp>')
def post_temperature(temp):
    print(f"temp = {temp}")

    with open("temperature.txt", "a") as t:
        t.write(str(temp) + "\n")

    return f"{temp} is received"

@server.post('/light/<int:light>')
def post_light(light):
    print(f"light = {light}")

    with open("light.txt", "a") as l:
        l.write(str(light) + "\n")

    return f"{light} is received"

@server.get('/temperature')
def get_temperature():
    with open("temperature.txt", "r") as t:
        return "<br>".join(t.readlines())

@server.get('/light')
def get_light():
    with open("light.txt", "r") as l:
        return "<br>".join(l.readlines())

server.run(host='0.0.0.0', port=4000, debug=True)