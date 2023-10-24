from flask import Flask, request
app = Flask(__name__)


@app.route('/messages')
def get_messages():
    return {
        'messages': [
            {
                'id': 1,
                'isOutgoing': True,
                'text': 'Kolik paralenu si muzu dat'
            },
            {
                'id': 2,
                'isOutgoing': False,
                'text': 'Zadny ty magore'
            }
        ]
    }

@app.route('/post-message', methods=['POST'])
def post_message():
    data = request.json
    return data