import time


def main():
    for i in range(1, 10):
        print(f"Task {i} of process completed")
        time.sleep(2)


if __name__ == "__main__":
    main()