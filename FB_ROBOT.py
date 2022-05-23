#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os, sys
from flask import Flask, request
from pymessenger import Bot
app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAAZAt41d1JvQBAKQslsa4jqtx6mK2BDvGZAYBH0lEGWovPZC6948AUcns45cK2dKQyJRIUVufRR8h25Vbm79LV03Sf6HnhjsjFfc8YeKFwoUD5OfH43VozZCczCEhlykpEZAyy5xkfsizjm4QsktEo31amsD7WAA8tVRngDL5z4OIdWrX1gig"
bot = Bot(PAGE_ACCESS_TOKEN)
num1={"A":"營業時間","B":"連絡電話","C":"營業地址"}
str1="可以輸入以下代碼查詢資料：\n營業時間：A\n連絡電話：B\n營業地址：C"
@app.route('/', methods=['GET'])
def verify():
 # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "just":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                if messaging_event.get('message'):
                     # Extracting text message
                    if 'text' in messaging_event['message']:
                        text=messaging_event['message']['text']
                        print("ID:%s,Text:%s"%(messaging_event['sender']['id'],text))
                        
                        def handle_game_server_terminated_message(self, msg):
                            terminated_server = self.active_server if self.active_server.name == msg.server else self.pending_server
                            was_already_stopping = terminated_server.stopping
                            terminated_server.terminated()

                            if was_already_stopping:
                                self.logger.info(f'launcher: {terminated_server.name} process terminated.')
                            else:
                                if self.pending_server.running:
                                    self.logger.info(f'launcher: {terminated_server.name} process terminated unexpectedly; '
                                     f'{self.pending_server.name} already starting.')
                                else:
                                    self.logger.info(f'launcher: {terminated_server.name} process terminated unexpectedly; '
                                         f'starting {self.pending_server.name} to take over.')
                                    self.pending_server.start()

                                msg = Launcher2LoginServerReadyMessage(None, None)
                                if self.login_server:
                                    self.login_server.send(msg)
                                else:
                                    self.last_server_ready_message = msg
                        
                        
                        if text=="A" or text=="B" or text=="C":
                            bot.send_text_message(sender_id,num1[text])
                        else:
                            bot.send_text_message(sender_id,str1)
                    else:                        
                        messaging_text = 'no text'
                return "ok", 200
def log(message):
#     print(message)
    sys.stdout.flush()
if __name__ == "__main__":
    app.run(debug = 0, port = 3000)


# In[1]:


num1={" A ":"營業時間"," B ":"連絡電話"," C ":"營業地址"}
str1="可以輸入以下代碼查詢資料：\n：A\n油價查詢：B\n營業地址：C"

