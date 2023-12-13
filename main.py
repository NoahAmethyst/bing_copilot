import os
from flask import Flask, request
from sydney import SydneyClient

app = Flask(__name__)


@app.route('/', methods=['POST'])
async def ask_copilot() -> {}:
    async with SydneyClient() as sydney:
        data = {}
        try:
            prompt = request.get_json().get('message', '')
            response = await sydney.ask(prompt, citations=False, suggestions=True)
            data = {
                'content': response[0],
                'suggestions': response[1],
            }
        except Exception as e:
            data = {
                'error': e.__str__()
            }
        return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
