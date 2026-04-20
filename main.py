import threading
import time

class Timer:
    def __init__(self):
        self.is_running = False
        self.seconds = 0

    def start(self):
        self.is_running = True
        threading.Thread(target=self.countdown).start()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.seconds = 0
        self.is_running = False

    def countdown(self):
        while self.is_running:
            print(f"Qolgan vaqt: {self.seconds} sekund", end='\r')
            time.sleep(1)
            self.seconds += 1

timer = Timer()
timer.start()

# 10 sekunddan keyin timer to'xtatiladi
time.sleep(10)
timer.stop()
