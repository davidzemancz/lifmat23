from flask import Flask
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