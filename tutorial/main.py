# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from mongoengine import *
from schema import *
app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 決定要回傳什麼 Component 到 Channel
    connect(os.environ['MONGODB_DB'], host=os.environ['MONGODB_HOST'], username=os.environ['MONGODB_USERNAME'], password=os.environ['MONGODB_PASSWORD'])
    try:
        user = Users.objects.get(user_id=event.message.id)
        user.tracked_courses.append(event.message.text)
    except DoesNotExist: 
        user = Users(
            user_id=event.source.id,
            username=line_bot_api.get_profile(event.source.id).display_name,
            tracked_course=[event.message.text]
        )
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text + "successful added"))

if __name__ == "__main__":
    app.run()