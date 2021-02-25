#!/usr/bin/env python

import psutil
import argparse
import datetime
import json

parser = argparse.ArgumentParser(description='System monitoring')
parser.add_argument('-i', '--interval', type=int, default=300, dest='interval',
                    help='time interval between snapshots (sec)')
parser.add_argument('-o', '--output', type=str, dest='output',
                    help='output format: txt or json')
args = parser.parse_args()


class Snapshot:
    def __init__(self):
        self.mem = self.memstate().percent
        self.vmem = self.vmemstate().percent
        self.io = self.iostate()
        self.network = self.networkstate()

    def cpustate(self, i):
        return psutil.cpu_percent(i)

    def memstate(self):
        return psutil.virtual_memory()

    def vmemstate(self):
        return psutil.swap_memory()

    def iostate(self):
        return psutil.disk_usage('/')

    def networkstate(self):
        return psutil.net_io_counters()


def output_json(num, timestamp):
    snap_dict = dict()
    time_dict = dict()
    json_key = dict()
    network_dict = dict()
    io_dict = dict()
    json_key['Overall CPU load'] = '{} %'.format(Snapshot().cpustate(args.interval))
    json_key['Overall memory usage'] = '{} %'.format(Snapshot().mem)
    json_key['Overall virtual memory usage'] = '{} %'.format(Snapshot().vmem)
    for name, value in Snapshot().io._asdict().items():
        io_dict[name] = value
    json_key['IO information'] = io_dict
    for name, value in Snapshot().network._asdict().items():
        network_dict[name] = int(value)
    json_key['Network information'] = network_dict
    time_dict[timestamp] = json_key
    snap_dict['SNAPSHOT {}'.format(num)] = time_dict
    with open('snapshots.json', 'a') as json_file:
        json_file.write(json.dumps(snap_dict, indent=4))
        json_file.write('\n\n')


def output_txt(num, timestamp):
    io_list = list()
    for name, value in Snapshot().io._asdict().items():
        io_list.append('{}={}'.format(name, value))
    io_str = ' '.join(io_list)
    net_list = list()
    for name, value in Snapshot().network._asdict().items():
        net_list.append('{}={}'.format(name, value))
    net_str = ' '.join(net_list)
    snap_record = 'SNAPSHOT {}: {}: Overall CPU load: {} % Overall memory usage: {} % \
Overall virtual memory usage: {} % IO information: {} Network information: {}'.format(
        num,
        timestamp,
        Snapshot().cpustate(args.interval),
        Snapshot().mem,
        Snapshot().vmem,
        io_str,
        net_str
    )
    with open('snapshots.txt', 'a') as txt_file:
        txt_file.write(snap_record + '\n')


def main():
    snapshot_counter = 0
    try:
        while True:
            snapshot_counter += 1
            if args.output == 'txt':
                output_txt(snapshot_counter, str(datetime.datetime.now()))
            elif args.output == 'json':
                output_json(snapshot_counter, str(datetime.datetime.now()))
            else:
                print('Wrong output format, use -h for help')
                break
    except KeyboardInterrupt:
        pass


if __name__ == 'main':
    main()
