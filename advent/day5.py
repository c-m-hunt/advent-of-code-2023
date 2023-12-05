from typing import List

from advent import utils


class Solution(utils.DaySolution):
    day = 5

    def solve_part_1(self):
        seeds = self.data["seeds"]
        min_location = None
        for location in seeds:
            location = self.get_location_for_seed(location)
            if min_location is None or location < min_location:
                min_location = location
        return min_location

    def solve_part_2(self):
        count = 0
        seed_ranges = self.data["seeds"]
        min_location = None
        for i in range(0, len(seed_ranges) - 1, 2):
            for seed in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1] + 1):
                count += 1
                location = self.get_location_for_seed(seed)
                if min_location is None or location < min_location:
                    min_location = location
                # if count % 100000 == 0:
                #     print(count, min_location)
        return min_location

    def get_location_for_seed(self, seed: int) -> int:
        location = seed
        maps = self.data["maps"]
        for map in maps.keys():
            location = self.get_location(location, map)
        return location

    def get_location(self, source: int, map_title: str) -> int:
        location = source
        map = self.data["maps"][map_title]
        for map_entry in map["map"]:
            if (
                map_entry["source_start"]
                <= location
                <= map_entry["source_start"] + map_entry["length"]
            ):
                location = map_entry["dest_start"] + (
                    location - map_entry["source_start"]
                )
                break
        return location

    def parse_data(self, data: List[str]) -> any:
        maps = {}

        source = None
        dest = None
        map = []
        map_title = None

        for i, line in enumerate(data):
            if i == 0:
                continue

            if line == "":
                if source is not None:
                    maps[map_title] = {
                        "source": source,
                        "dest": dest,
                        "map": map,
                    }
                    source = None
                    dest = None
                    map = []
                continue
            if line[0].isdigit():
                dest_start, source_start, length = line.split()
                map.append(
                    {
                        "source_start": int(source_start),
                        "dest_start": int(dest_start),
                        "length": int(length),
                    }
                )

            else:
                map_title = line.split(" ")[0]
                parts = line.split(" ")[0].split("-")
                source = parts[0]
                dest = parts[2]

        maps[map_title] = {
            "source": source,
            "dest": dest,
            "map": map,
        }

        return {
            "seeds": [int(i) for i in data[0].split(":")[1].split()],
            "maps": maps,
        }
