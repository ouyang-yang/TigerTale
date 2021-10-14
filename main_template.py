from linebot.models import FlexSendMessage
def main_panel_flex():
    flex_message = FlexSendMessage(
                    alt_text='推薦餐廳/景點',
                    contents= {
                                "type": "bubble",
                                "hero": {
                                  "type": "image",
                                  "url": "https://github.com/ouyang-yang/TigerTale/blob/master/images/%E6%8E%A8.png?raw=true",
                                  "size": "full",
                                  "aspectRatio": "20:13",
                                  "aspectMode": "cover",
                                  "position": "relative"
                                },
                                "body": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "想找哪裡的圖書館呢？",
                                      "weight": "bold",
                                      "size": "xl",
                                      "contents": [],
                                      "color": "#6e3e1e"
                                    },
                                    {
                                      "type": "text",
                                      "text": "請幫助我選擇圖書館在台灣的哪個位置：）",
                                      "size": "xs",
                                      "margin": "sm"
                                    },
                                    {
                                      "type": "separator",
                                      "margin": "lg"
                                    },
                                    {
                                      "type": "box",
                                      "layout": "horizontal",
                                      "contents": [
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "找景點",
                                            "text": "找景點"
                                          },
                                          "style": "primary",
                                          "height": "sm",
                                          "color": "#806408"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "找美食",
                                            "text": "找美食"
                                          },
                                          "style": "primary",
                                          "margin": "xxl",
                                          "height": "sm",
                                          "color": "#806408"
                                        }
                                      ],
                                      "margin": "lg"
                                    },
                                    ]                     
                                }
                    }
    )
    return flex_message