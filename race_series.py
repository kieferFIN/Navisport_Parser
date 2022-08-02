from dataclasses import dataclass, field
from collections import defaultdict
from race import Race, Athlete


@dataclass(order=True, frozen=True)
class PointResult:
    total: int
    athlete: Athlete
    points: list[int]
    skipped: list[int]

    def __str__(self):
        result = f"{self.athlete.name}\t{self.total}"
        for i, p in enumerate(self.points):
            result += f"\t{p}"
        return result


@dataclass
class RaceSeries:
    name: str
    races: list[Race]
    skipped_races: int = 0

    def calculate_points(self, class_name: str) -> list[PointResult]:
        points = defaultdict(lambda: [0] * len(self.races))
        for i, race in enumerate(self.races):
            results = race.get_class(class_name)
            for (athlete, p, _) in results.points_iter():
                points[athlete][i] = p

        points_results = []

        for athlete, points in points.items():
            t_p = sum(points)
            sorted_points = sorted(points)
            skipped = []
            for a in range(self.skipped_races):
                t_p -= sorted_points[a]
                skipped.append(points.index(sorted_points[a]))
            points_results.append(PointResult(t_p, athlete, points, skipped))

        return sorted(points_results, reverse=True)
