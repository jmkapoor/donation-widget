from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    amount = data.get('amount')

    # Process the donation amount
    # Your donation processing logic here

    return jsonify({'message': 'Donation received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
