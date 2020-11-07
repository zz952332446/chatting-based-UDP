import socket
import threading
import tkinter as tk
import time
import inspect
import ctypes


mywspn=('10.**.***.**',8800)

#######停止线程的模块，来源于网上
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


########接收消息
def receive(s):

    print('re start')
    while True:
        data,add=s.recvfrom(1024)
        data=data.decode()
        if data=='bye':
            break
        else:
            print('from',add,'say:',data,'time is', time.asctime( time.localtime(time.time()) ))
    stop_thread(t2)#停止接收消息的线程
    if t1.isAlive():
        print('t1 alive')
    else:
        print('socket closed')
        s.close()
        

#######发送消息     
def send(s):
    print('send start')
   # inp=input('发送:')
    
    while True:
        inp=mygui("Enter data")
        print('I say:',inp,'time is', time.asctime( time.localtime(time.time()) ))
        s.sendto(inp.encode(),mydell) #注意逻辑，先send再break
        if inp=='bye':
            s.sendto('I am offline'.encode(),mydell) 
            break
    stop_thread(t1) #停止发送消息的线程       
    if t2.isAlive():
        print('t2 alive')
    else:
        print('socket closed')
        s.close()


#发送消息的GUI界面
def mygui(prompt=""):

    root = tk.Tk()
    tk.Label(root, text=prompt).pack()
    entry = tk.Entry(root)
    entry.pack()
    result = None
    def callback(event):
        nonlocal result
        result = entry.get()
        root.destroy()
    entry.bind("<Return>", callback)
    root.mainloop()
    return result


s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',8888))

t1=threading.Thread(target=send,args=(s,))
t2=threading.Thread(target=receive,args=(s,))
t1.start()
t2.start()
