def helloWorld():
    print("Hello, World!")
#end procedure

def helloName(name):
    print(f'Hello {name}')
#end procedure

helloName(__name__)
helloWorld()