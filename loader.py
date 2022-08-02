import json
from urllib.request import urlopen, Request

from race import Race, RaceClass, Athlete


def load_results(event_id: str) -> Race:
    url = f"http://navisport.fi/api/events/{event_id}/results/parsed"
    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}
    print(f"loading from {url}")
    req = Request(url, headers=header)
    json_data = urlopen(req).read().decode('utf-8')
    data = json.loads(json_data)
    race = Race(data["name"])
    for d in data["courseClasses"]:
        name = d["name"]
        results = [(Athlete(runner["name"], runner["club"]), runner["time"])
                   for runner in d["results"] if runner["status"] == "Ok"]
        race.add_class(RaceClass(name, results))
    return race


def main():
    event_id = "6c88d812-39f7-4d9c-b549-83c1cf1115a3"
    race = load_results(event_id)
    for (name, time) in race.get_class("B+").results:
        minutes = time // 60
        secs = time % 60
        print(f"{name}, {minutes}:{secs}")


if __name__ == "__main__":
    main()
