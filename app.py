# 載入需要的模組
from __future__ import unicode_literals
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *
import json
import main_template
from flask import Flask, request, abort

app = Flask(__name__)

# LINE 聊天機器人的基本資料
# line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
# handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
line_bot_api = LineBotApi(
    'I5Rd5Ztc9T7/nfC9uLuFOO98Uk/cvo/muCi6LJit0AcSk2HvoZ2qqsgN/3jE1jIize+CzfmZPxaHO0CVnQSBTXbHytrvrdPNQX7MTJmUclWsMDlqJfLMD4EsbnLfcy5j1e3j8sbcMg3Dbnll2hUnOwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4ddc0271caebe33ad9f47cdc1c8d0c1b')
# test
# line_bot_api = LineBotApi(
#     'pI2RMOmFid7t4LcAXLD6xtINIdt1GTk47SV+/3VObyfqrnEO+OVv/1NiJGDmv5nldjF6fzXrwZ+uMie+Hil5rjD1UhstcCOYtNrOuR0b5OXWIKEt1L7D83YlWEaRRwSw39lUY9CxEzpqeduShuc6EQdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('0583d8005933cf8d466126a3649b1952')

# 打個招呼 :)
@app.route("/", methods=['GET'])
def hello():
    return "Hi!"

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

# ----------------設定回覆訊息介面-----------------
@handler.add(MessageEvent, message=TextMessage)
def test1(event):
    # ----------------取得userid-----------------
    user_id = event.source.user_id
    if user_id == '':
        user_id = event.source.user_id

    # --------------------點餐---------------------
    if event.message.text == "點餐":
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text='沿用並優化「招財虎玩數位」點餐系統')
        )        

    # ----------------推薦餐廳/景點-----------------
    elif event.message.text == "推薦餐廳/景點":
        flex_message0 = main_template.main_panel_flex()
        line_bot_api.reply_message(event.reply_token, flex_message0) 

    elif event.message.text == "找美食":
        flex_message1 = main_template.eat_imagemap_flex()
        line_bot_api.reply_message(event.reply_token, flex_message1) 

    elif event.message.text == "找景點":
        flex_message2 = main_template.main_panel_flex()
        line_bot_api.reply_message(event.reply_token, flex_message2) 

    # ----------------優惠專區-----------------
    elif event.message.text == "優惠專區":
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text='優惠券&集點卡')
        )

    # ----------------我的訂單/預約查詢-----------------
    elif event.message.text == "我的訂單/預約查詢":
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text='提供訂單與預約查詢服務')
        )

    # ----------------找老虎！-----------------
    elif event.message.text == "找老虎！":
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text='交由有老虎燈箱的店家進行集點認證')
        )      

     # ----------------主題地圖-----------------
    elif event.message.text == "主題地圖":
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text='利用LIFF跳出做好標記的地圖')
        )          
                     

if __name__ == "__main__":
    app.run(debug=True)                    