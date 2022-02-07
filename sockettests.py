import websocket
import _thread
import time
import rel

rel.safe_read()

recvt = []

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    pass

def on_message(ws, message):
    recvt.append(message)
    print(recvt)
    ws.send("recorded")


websocket.enableTrace(False)
ws = websocket.WebSocketApp("wss://8000-dpallot-simplewebsocket-8e4km0igdur.ws-us29.gitpod.io/",
                              on_message=on_message
                              )

ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection

print(recvt)
rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()