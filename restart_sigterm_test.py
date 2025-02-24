import sys
import time
import signal

# STDOUT을 즉시 flush하도록 설정
sys.stdout.reconfigure(line_buffering=True)

print("Starting up")

# SIGTERM 시그널을 처리하는 핸들러 정의
def graceful_shutdown(signum, frame):
    print("Graceful shutdown")
    sys.exit(0)

# SIGTERM 시그널 핸들러 등록
signal.signal(signal.SIGTERM, graceful_shutdown)

# 무한 루프 실행 (작업 수행을 가장함)
while True:
    print("Pretending to do work")
    time.sleep(3)
