import time


def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed')


if __name__ == '__main__':
    example(10)
