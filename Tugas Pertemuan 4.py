from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/karyawan', methods=['GET','POST','PUT','DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama' : 'Putra GET',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        elif request.method == 'POST':
            data = [{
                'nama' : 'Sulaiman POST',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama' : 'Wawan PUT',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        else:
            data = [{
                'nama' : 'Iwan DELETE',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)
app.run()
