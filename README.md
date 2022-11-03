# hng_stage_2# HNG-Stage2-Task
## Task Description
#### Using the same server setup from stage one
#### Create an (POST) api endoint that takes the following sample json

{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
<br>
Operation can either be addition, subtraction or mutiplication
<br>
x can be a number and Integer datatype
y can be a number and Integer datatype
<br>
Based on the operation sent, perform a simple arithmetic operation on x and y
Return a response with the result of the operation and your slack username
{ “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }
