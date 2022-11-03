from rest_framework.response import Response
from rest_framework.decorators import api_view


# It returns a JSON object with the data specified in the data variable 
@api_view(['GET', 'POST'])
def getData(request):
    if request.method == 'GET':
        data = {"slackUsername": "ambroseotundo","backend":True, "age":24, "bio": "I'm a passionate developer whose aim is to develop scalable and efficient software" }
        return Response(data)

   # Checking if the request is a POST request and if it is, it is checking if the data sent is an
   # integer and if the operation type is one of the three specified.
    if request.method == 'POST':
        operation = request.data
        if (type(operation['x']) is not int or type(operation['y']) is not int):
            result = {"details": "X and Y must be integers only"}
            return Response(result)
        if (operation['operation_type'] not in ["addition", "subtraction", "multiplication"]):
            result = {"details": "invalid operation type"}
            return Response(result)
        
       # Getting the values of the keys operation_type, x and y from the data sent in the POST
       # request.
        operation_type = operation['operation_type']
        x = operation['x']
        y = operation['y']

      # Checking the operation type and performing the operation specified.
        if operation_type == "addition":
            result = x + y
        elif operation_type == "subtraction":
            result = x - y
        else:
            result = x * y
        result = {"slackUsername": "ambroseotundo", "operation_type" : operation_type, "result": result }
        return Response(result)

