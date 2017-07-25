import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=str, help="xlsx-файл в который будут выгружены данные")
    parser.add_argument("-q", "--quantity", type=int, help="Колличество спарсеных курсов. Изначально – 20", default=20)
    return parser.parse_args()