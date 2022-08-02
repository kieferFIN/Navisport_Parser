from loader import load_results
from race_series import RaceSeries
from printer import print_total_points
from multiprocessing import Pool

import argparse


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--races", "-r", action="extend", nargs="+", type=str)
    group.add_argument("--file", "-f")

    parser.add_argument("--skipped", "-s", type=int, default=0)

    parser.add_argument("--classes", "-c", required=True, nargs="+", type=str)

    parser.add_argument("--name", "-n", default="")

    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            event_ids = [line.rstrip() for line in f]
    else:
        event_ids = args.races

    # event_ids = ["6c88d812-39f7-4d9c-b549-83c1cf1115a3",
    #              "d53c85fa-e7a9-4abc-baa6-39f61db52079",
    #              "9513a74e-64b8-403a-b0e5-47341d8ebdaf",
    #              "40a64bf3-aa8c-48af-b8b8-f00e110dbc27",
    #              "a8c8510f-f30e-4998-af07-187bac292251"]

    pool = Pool()
    races = pool.map(load_results, event_ids)
    # races = list(map(load_results, event_ids))
    series = RaceSeries(args.name, races, skipped_races=args.skipped)
    # classes = ["A+", "B+", "B"]
    for c in args.classes:
        with open(f"{args.name}_{c}.txt", 'w') as f:
            print_total_points(series, f, c)


if __name__ == "__main__":
    main()
