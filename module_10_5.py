import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        data = file.readline()
        while data:
            all_data.append(data.strip())
            data = file.readline()
    return all_data


filenames = [f'./file{number}.txt' for number in range(1, 5)]
start_time = time.time()

# for filename in filenames:
#     read_info(filename)
# print("Линейное выполнение:", time.time() - start_time)

if __name__ == '__main__':
    start_time = time.time()
    pool = multiprocessing.Pool(4)
    pool.map(read_info, filenames)
    print("Параллельное выполнение:", time.time() - start_time)
