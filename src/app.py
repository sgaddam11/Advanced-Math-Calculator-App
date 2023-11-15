#!/usr/bin/python
from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def getindex():
        return render_template('index.html')

@app.route('/api/rsdl', methods=['GET'])
def getrsdl():
        return render_template('rsdl')



class generatelucas(Resource):
    def get(self,number):

       result = "2, 1"
       a = 2
       b = 1
       i = 0
       while i < number - 2:
           i = i + 1
           tmp_var = b
           b = a + b
           a = tmp_var
           result = result + ", " + str(b)
            # print(a)
       return {"lucas" : result}

class generatefact(Resource):
    def get(self,n):
        num = 1
        while n >= 1:
            num = num * n
            n = n - 1
        return {"factorial" : num }
class apiRSDL(Resource):
    def get(self):
         y = '<?xml version="1.0" encoding="UTF-8" ?><rsdl><description>This webservice lets you find the lucas series of the number which user has passed. User can also find fibonacci series  of the number and user can also find the factorial of the  number. This webservice will accept input as a integer values and gives ouput in JSON format. User has to pass parameter in the url itself. This web service uses path parameters.</description><version major="1" minor="0" build="0" revision="12"/><links><link rel="get" href="/lucas/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>Number</name><value>Number of element wanted in lucas series.</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link><link rel="get" href="/fibonacci/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>number</name><value>Number of integers in the fibonacci series needed by user.</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link><link rel="get" href="/fact/number"><request><url><parameters_set><parameter type="xs:int" required="true"><name>number</name><value>Number for which user needs the factorial</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link></links></rsdl>'

         rsdl = request.args.get('rsdl')
         if(rsdl == ""):
            x = 'rsdl.xml'
           #y = ET.parse(x)

            return Response(y, mimetype='text/plain')        #print(BeautifulSoup(x, "xml").prettify())         
         return Response(y, mimetype='text/xml')

class generatefibonacci(Resource):
    def get(self,number):

       result = "0, 1"
       a = 0
       b = 1
       i = 0
       while i < number - 2:
           i = i + 1
           tmp_var = b
           b = a + b
           a = tmp_var
           result = result + ", " + str(b)
            # print(a)
       return {"fibonacci" : result}

api.add_resource(generatelucas, '/lucas/<int:number>')
api.add_resource(generatefibonacci, '/fibonacci/<int:number>')
api.add_resource(generatefact, '/fact/<int:n>')
api.add_resource(apiRSDL,'/api/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
                                          
                                                    
