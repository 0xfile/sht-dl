#!/usr/bin/python3
import requests

tracker_url = "https://trackerslist.com/best_aria2.txt"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}


def parse_task():
    task = open('task.txt', 'r')
    url = open('url.txt', 'w')
    video = open('video.txt', 'w')
    info = task.read().splitlines()
    url.write(info[0])
    video.write(info[1])
    task.close()
    url.close()
    print(info[0], info[1], "task parsed!")


def add_tracker(url):
    r = requests.get(url)
    trackers = r.text
    conf = open('aria2.conf', 'a+')
    conf.write(f'bt-tracker={trackers}')
    conf.close()
    print("tracker added!")

if __name__ == '__main__':
    vid = parse_task()
    add_tracker(tracker_url)
