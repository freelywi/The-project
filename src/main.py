import time

# Для использования в качестве бесконечного процесса

while True:
    print("Current time:", time.strftime("%H:%M:%S"))
    time.sleep(5)