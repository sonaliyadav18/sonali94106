from flask import Flask, request, jsonify
from datetime import datetime
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Smart Home Monitoring System</h1></body></html>"

@server.route('/smart_home', methods=['POST'])
def create_smart_home():
    device_id = request.get_json().get('device_id')
    light_status = request.get_json().get('light_status')
    fan_status = request.get_json().get('fan_status')
    temperature = request.get_json().get('temperature')
    date_time = datetime.now()

    query = f"""
    INSERT INTO smart_home 
    VALUES ({device_id}, '{light_status}', '{fan_status}', {temperature}, '{date_time}');
    """
    executeQuery(query=query)

    return "Smart home data added successfully"

@server.route('/smart_home', methods=['GET'])
def retrieve_smart_home():
    query = "SELECT * FROM smart_home;"
    data = executeSelectQuery(query=query)

    formatted_data = []
    for row in data:
        device_id = row[0]
        light_status = row[1]
        fan_status = row[2]
        temperature = row[3]
        date_time = row[4].strftime("%Y-%m-%d %H:%M:%S")
        formatted_data.append((device_id, light_status, fan_status, temperature, date_time))

    return f"Smart Home Data: {formatted_data}"

@server.route('/smart_home', methods=['PUT'])
def update_smart_home():
    device_id = request.get_json().get('device_id')
    light_status = request.get_json().get('light_status')
    fan_status = request.get_json().get('fan_status')

    query = f"""
    UPDATE smart_home
    SET light_status = '{light_status}', fan_status = '{fan_status}'
    WHERE device_id = '{device_id}';
    """
    executeQuery(query=query)

    return "Smart home status updated successfully"

@server.route('/smart_home', methods=['DELETE'])
def delete_smart_home():
    device_id = request.get_json().get('device_id')

    query = f"DELETE FROM smart_home WHERE device_id = '{device_id}';"
    executeQuery(query=query)

    return "Smart home device deleted successfully"

@server.post('/smart_home/high_temperature')
def get_high_temperature():
    data = request.get_json()
    if not data or 'temperature' not in data:
        return {"error": "temperature is required"}, 400

    temperature = data['temperature']
    query = f"""
    SELECT device_id, light_status, fan_status, temperature, date_time
    FROM smart_home
    WHERE temperature > {temperature};
    """
    result = executeSelectQuery(query=query)

    formatted_data = []
    for row in result:
        formatted_data.append(
            (row[0], row[1], row[2], row[3], row[4].strftime("%Y-%m-%d %H:%M:%S"))
        )

    return f"High Temperature Devices: {formatted_data}"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)