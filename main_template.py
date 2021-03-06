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

def order_panel_flex():
    flex_message = FlexSendMessage(
                    alt_text='點餐',
                    contents= {
                                "type": "bubble",
                                "hero": {
                                  "type": "image",
                                  "url": "https://github.com/ouyang-yang/TigerTale/blob/master/images/%E5%90%83.png?raw=true",
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
                                      "text": "想吃點什麼呢：）",
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
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "我的最愛",
                                            "text": "我的最愛"
                                          },
                                          "style": "primary",
                                          "height": "sm",
                                          "color": "#806408"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "直接輸入店家",
                                            "text": "直接輸入店家"
                                          },
                                          "style": "primary",
                                          "margin": "xxl",
                                          "height": "sm",
                                          "color": "#806408"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "找新店家",
                                            "text": "找新店家"
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

def find_new_panel_flex():
  flex_message = FlexSendMessage(
                  alt_text='找新店家',
                  contents= {
                              "type": "bubble",
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "想吃什麼類型的食物呢：）",
                                    "weight": "bold",
                                    "size": "xl",
                                    "contents": [],
                                    "color": "#6e3e1e"
                                  },
                                  {
                                    "type": "separator",
                                    "margin": "lg"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "中式",
                                          "text": "中式"
                                        },
                                        "style": "primary",
                                        "height": "sm",
                                        "color": "#806408"
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "異國",
                                          "text": "異國"
                                        },
                                        "style": "primary",
                                        "margin": "xxl",
                                        "height": "sm",
                                        "color": "#806408"
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "點心",
                                          "text": "點心"
                                        },
                                        "style": "primary",
                                        "margin": "xxl",
                                        "height": "sm",
                                        "color": "#806408"
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "飲料",
                                          "text": "飲料"
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

def check_order_panel_flex():
  flex_message = FlexSendMessage(
                  alt_text='我的訂單/預約查詢',
                  contents= {
                              "type": "bubble",
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "取消訂單",
                                          "text": "取消訂單"
                                        },
                                        "style": "primary",
                                        "height": "sm",
                                        "color": "#806408"
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "查看訂單",
                                          "text": "查看訂單"
                                        },
                                        "style": "primary",
                                        "margin": "xxl",
                                        "height": "sm",
                                        "color": "#806408"
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "message",
                                          "label": "定位資訊",
                                          "text": "定位資訊"
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

def order_panel_flex():
    flex_message = FlexSendMessage(
                    alt_text='找老虎',
                    contents= {
                                "type": "bubble",
                                "hero": {
                                  "type": "image",
                                  "url": "https://github.com/ouyang-yang/TigerTale/blob/master/images/%E5%90%83.png?raw=true",
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
                                      "text": "想吃點什麼呢：）",
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
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "我的最愛",
                                            "text": "我的最愛"
                                          },
                                          "style": "primary",
                                          "height": "sm",
                                          "color": "#806408"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "直接輸入店家",
                                            "text": "直接輸入店家"
                                          },
                                          "style": "primary",
                                          "margin": "xxl",
                                          "height": "sm",
                                          "color": "#806408"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "message",
                                            "label": "找新店家",
                                            "text": "找新店家"
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