import os
import csv

path="data"

def analyze():
    with open('artifacts/analyze_artifact.csv', 'w+') as f_obj:
        csv_writer = csv.writer(f_obj, delimiter=",")
        for root, dirs, files in os.walk(path):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                if file_extension == '.wav':
                    is_valid = 1
                else:
                    is_valid = 0
                csv_writer.writerow([filename, is_valid])
                print(filename+',', is_valid)
                # print("name = {}, extension = {}".format(filename, file_extension))

if __name__ == "__main__":
    print('Start validation:\n')
    analyze()
    print('\nValidation ended')
