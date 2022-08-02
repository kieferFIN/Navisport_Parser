from race_series import RaceSeries
from typing import TextIO


def print_total_points(race_series: RaceSeries, out: TextIO, class_name: str):
    points = race_series.calculate_points(class_name)
    for i, pr in enumerate(points):
        out.write(f"{(i+1):3} {pr.athlete.name:30} {pr.total:4}  ")
        for j, p in enumerate(pr.points):
            if j in pr.skipped:
                p_txt = f"*{p}*"
                out.write(f"{p_txt:>6}")
            else:
                out.write(f" {p:4} ")
        out.write(f"  {pr.athlete.club}")
        out.write("\n")
