import csv
import hashlib
import os
import pandas
import soundfile

path="data"

def stats():
    with open('artifacts/stats_artifact.csv', 'w+') as f_obj:
        print("available formats:\n", soundfile.available_formats())
        csv_writer = csv.writer(f_obj, delimiter=",")
        for root, dirs, files in os.walk(path):
            for file in files:
                print("MD5: ", hashlib.md5(file.encode()).hexdigest())
                data, sr = soundfile.read(f"./{path}/{file}")
                print('Data: ', data[:5])
                filename, _ = os.path.splitext(file)
                csv_writer.writerow([filename, sr, data.shape[1]])
                print(filename, ',', sr, ',', data.shape[1])
                print()


if __name__ == "__main__":
    print('Start collecting statistic:\n')
    stats()
    print('\nCollection ended')