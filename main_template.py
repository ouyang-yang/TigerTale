from linebot.models import FlexSendMessage, ImagemapSendMessage
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
                                      "text": "想被推推嗎：）",
                                      "weight": "bold",
                                      "size": "xl",
                                      "contents": [],
                                      "color": "#6e3e1e"
                                    },
                                    {
                                      "type": "text",
                                      "text": "RRRRRRR",
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

def eat_imagemap_flex():
    flex_message = ImagemapSendMessage(
                      base_url='',
                      alt_text='this is an imagemap',
                      base_size=BaseSize(height=520, width=520),
                      actions=[
                          URIImagemapAction(
                              link_uri='',
                              area=ImagemapArea(
                                  x=174, y=65, width=707, height=416
                              )
                          ),
                          MessageImagemapAction(
                              text='hello',
                              area=ImagemapArea(
                                  x=520, y=0, width=520, height=520
                              )
                          )
                      ]
                  )
    return flex_message
