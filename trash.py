from hardcodedrestaurants import trashArray
import copy
from flask import Flask

app = Flask(__name__)
global array1
global anotherArray
array1 = copy.deepcopy(trashArray)
anotherArray = copy.deepcopy(trashArray)
#global trashArray
@app.route('/')
def index():
    
    print(f' this is array1 in /: {array1}')
    array1.append(8)
    array1.append(9)
    print(f' this is array1 in / after append: {array1}')
    
    return 'This is route /'


@app.route('/a')
def index2():
    print(f' this is anotherArray in /a: {anotherArray}')
    anotherArray.pop(0)
    anotherArray.pop(0)
    print(f' this is anotherArray after delete: {anotherArray}')
    return 'This is route /a'


app.run()






