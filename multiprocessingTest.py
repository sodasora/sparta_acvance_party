from multiprocessing import Process
import os


# print('hello os')
# print('my pid is', os.getpid())

# def foo():
#     print('child process', os.getpid())
#     print('my parent is', os.getpid())
#
# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child = Process(target=foo).start()

#동일한 작업을 하는 프로세스 만들기
# def foo():
#     print('hello, os')
#
# if __name__ == '__main__':
#     child1 = Process(target=foo).start()
#     child2 = Process(target=foo).start()
#     child3 = Process(target=foo).start()

# 각기 다른 작업을 하는 프로세스 생성하기
def foo():
    print('This is foo')
def bar():
    print('This is bar')
def baz():
    print('This is baz')
if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()