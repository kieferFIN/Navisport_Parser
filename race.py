from typing import Optional, Iterator
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Athlete:
    name: str
    club: str


@dataclass(frozen=True)
class RaceClass:
    name: str
    results: [(Athlete, int)]

    @property
    def points(self) -> [(Athlete, int, int)]:

        return list(self.points_iter())

    def points_iter(self) -> Iterator[tuple[Athlete, int, int]]:
        (_, winner_time) = self.results[0]
        for (athlete, time) in self.results:
            if time > 0:
                yield athlete, winner_time * 1000 // time, time


@dataclass
class Race:
    name: str
    classes: list[RaceClass] = field(default_factory=list)

    def add_class(self, race_class: RaceClass):
        self.classes.append(race_class)

    def get_class(self, name: str) -> Optional[RaceClass]:
        for c in self.classes:
            if c.name == name:
                return c
        return None

    @property
    def class_names(self) -> list[str]:
        return [rc.name for rc in self.classes]



