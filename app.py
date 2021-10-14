from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

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
    return "Hi! Wanna find some InTeREsTInG books?"

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

    # ----------------實用小功能-----------------
    if event.message.text == "實用小功能":
        flex_message0 = flex_template.main_panel_flex()
        line_bot_api.reply_message(event.reply_token, flex_message0)    