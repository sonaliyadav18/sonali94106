from flask import Flask,request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery
server=Flask(__name__)

@server.get('/')
def gomepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor_readings')
def create_iot_data():
    id=request.form.get('id')
    temperature=request.form.get('temperature')
    humidity=request.form.get('humidity')
    timestamp=request.form.get('timestamp')
    query=f"insert into sensor_readings values({id},'{temperature}','{humidity}','{timestamp}');"
    executeQuery(query=query)
    return "sensor_readings is added successfully "

@server.get('/sensor_readings')
def retrieve_sensor_reading():
    query ="select * from sensor_readings ;"
    data=executeSelectQuery(query=query)
    return f"sensor_readings :{data}"


@server.put('/sensor_readings')
def update_sensor_readings():
    id=request.form.get('id')
    temperature=request.form.get('temperature')
    query=f"update sensor_readings SET temperature='{temperature}' where id='{id}';"
    executeQuery(query=query)  
    return "sensor_readings is updated successfully"

@server.delete('/sensor_readings')
def delete_sensor_readings():
    id=request.form.get('id')
    query=f"delete from sensor_readings where id='{id}';"
    executeQuery(query=query)  
    return "sensor_readings is deleted successfully" 

@server.get('/sensor_readings/below_temp')
def below_temp():
    temperature = request.args.get('temperature')
    query = f"""select * from sensor_readings
    where temperature < {temperature};
    """
    data = executeSelectQuery(query)
    return f"Below temperature readings: {data}"

if __name__ =='__main__':
   server.run(host='0.0.0.0',port=4000,debug=True)