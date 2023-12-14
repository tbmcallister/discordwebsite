from flask import Flask, render_template, request, jsonify
import asyncio
from bot import is_user_online

app = Flask(__name__)

@app.route('/check_bot_status')
async def check_bot_status():
    bot_online = await is_user_online(1078181191204732928)  # Replace BOT_USER_ID with your bot's user ID
    return jsonify({'status': bot_online})

@app.route('/')
def index():
    user_id = 1078181191204732928  # Replace with your bot's user ID
    bot_online_task = asyncio.run(is_user_online(user_id))
    return render_template('index.html', bot_online_task=bot_online_task)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check_online_status', methods=['POST'])
async def check_online_status():
    user_id = request.form.get('user_id')
    try:
        user_online = await is_user_online(int(user_id))
        return jsonify({'online': user_online})
    except ValueError:
        return jsonify({'error': 'Invalid user ID'}), 400

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run(host='192.168.0.48', port=5000))
