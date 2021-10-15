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

def spot_imagemap_flex():
    flex_message = ImagemapSendMessage(
                      type= "imagemap",
                      base_url='https://github.com/ouyang-yang/TigerTale/tree/master/images',
                      alt_text='虎尾景點地圖',
                      base_size=base_size(width = 1040, height = 1040),
                      actions=[
                          URIImagemapAction(
                              link_uri='https://github.com/ouyang-yang/TigerTale/blob/master/images/%E5%90%88%E5%90%8C%E5%BB%B3%E8%88%8D700px.jpg?raw=true',
                              area=ImagemapArea(
                                  x=174, y=65, width=707, height=416)
                          ),
                          MessageImagemapAction(
                              text='測試',
                              area=ImagemapArea(
                                  x=520, y=0, width=520, height=520
                              )
                          )
                      ]
                  )
    return flex_message
