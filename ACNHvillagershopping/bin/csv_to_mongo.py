import csv
import os


def convert_csv_to_mongodb():
    root_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_path, 'npc.csv')

    with open(file_path, 'r', encoding='utf-8', newline='') as nf:
        sr = csv.reader(nf, delimiter=' ', quotechar='|')

        for row in sr:
            print(', '.join(row))

    return

def convert_npc_image_to_csv():
    root_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_path, 'npc.csv')
    image_path = os.path.join(os.path.join(root_path, 'static'), 'villagers')

    onlyfiles = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]

    with open(file_path, 'w', encoding='utf-8') as csvfile:
        
        for image_file in onlyfiles:
            file_name = "".join(image_file.split())
            print(file_name)
            csvfile.write("{}\n".format(file_name))

    return

if __name__ == '__main__':
    # convert_csv_to_mongodb() 
    convert_npc_image_to_csv() 