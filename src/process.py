import time


def main():
    for i in range(1, 120):
        print(f"Task {i} of process completed")
        time.sleep(2)


if __name__ == "__main__":
    main()