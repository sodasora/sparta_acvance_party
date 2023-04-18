import os
import threading


# #코드로 스레드 만들기
# print('process id', os.getpid())
#
# def foo():
#     print('thread id', threading.get_native_id()) #thread id + 스레드 ID 형태
#     print('process id', os.getpid()) # process id + PID
# if __name__=='__main__':
#     print('process id', os.getpid())
#     thread = threading.Thread(target=foo).start() #foo 라는 함수를 실행하는 스레드를 만듥 실행하라

# #동일한 작업을 하는 스레드 생성하기
# def foo():
#     print('thread id', threading.get_native_id())
#     print('thread id', os.getpid())
# if __name__=='__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=foo).start()
#     thread2 = threading.Thread(target=foo).start()
#     thread3 = threading.Thread(target=foo).start()

# 각기 다른 작업을 하는 스레드 생성하기
def foo():
    print('this is foo')
def bar():
    print('this is bar')
def baz():
    print('this is baz')
if __name__=='__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()