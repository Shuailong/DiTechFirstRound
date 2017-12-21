import matplotlib.pyplot as plt
from csv import DictReader
import csv
from collections import defaultdict
from tqdm import tqdm
import numpy as np
import sys


DATA_PATH = '../data/trace_data.txt'


def main():
    row_count = len(list(csv.reader(open(DATA_PATH)))) - 1
    with open(DATA_PATH) as f:
        vehicle_trace = defaultdict(list)
        columns = ['vehicle-id', 'time', 'x-coordinate', 'y-coordinate', 'speed', 'category']
        reader = DictReader(f, fieldnames=columns)
        next(reader)
        for line in tqdm(reader, desc='Read vehicle traces', total=row_count):
            vehicle_trace[line['vehicle-id']].append([line['x-coordinate'], line['y-coordinate']])
        print(f'{row_count} rows read.')
        print(f'{len(vehicle_trace)} vehicles found.')
        print(f'{sum(map(len, vehicle_trace.values())) / len(vehicle_trace):.2f} samples per vehicle.')

        plt.figure()
        plt.ion()
        for vehicle_id, traces in vehicle_trace.items():
            trace = np.array(traces)
            print(f'vehicle {vehicle_id}: {len(traces)} samples.')
            plt.plot(trace[:, 0], trace[:, 1], 'ro')
            plt.show()
            u = input("Enter to continue...")
            if u:
                sys.exit()
            plt.close()


if __name__ == '__main__':
    main()
