from queue import Queue
from threading import Thread
import time

in_queue = Queue()

def consumer():
    print('소비자 대기')
    work = in_queue.get()  # 두 번째로 실행됨
    print('소비자 작업중')
    # Doing work
    print('소비자 완료')
    # 입력 큐가 다 소진될 때까지 기다릴 수 있다.
    in_queue.task_done()  # 세 번째로 실행됨

thread = Thread(target=consumer) # 병렬적으로 실행될 독립적인 스레드 생성(메인 스레드와 동시에 실행)
thread.start()

print('생산자 데이터 추가')
in_queue.put(object())    # 첫 번째로 실행됨
print('생산자 대기')
in_queue.join()           # 네 번째로 실행됨
print('생산자 완료')
thread.join() 

# 비동기적 실행
# 1. 스레드: 추가 스레드를 생성하지만 실제 병렬적으로 실행되진 않음(= 작업끼리 빠르게 교차 스위칭)
# 2. asyncio: 단일 스레드에서 실행되고, 실제 병렬적으로 실행되진 않지만 이벤트 루프를 사용하여 비동기적 실행(= 각 작업이 완료되거나 대기 상태에 들어갈 때 다른 작업으로 전환)
