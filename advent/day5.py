from typing import List

from advent import utils


class Solution(utils.DaySolution):
    day = 5

    def solve_part_1(self):
        seeds = self.data["seeds"]
        return self.get_min_location(seeds)

    def solve_part_2(self):
        seed_ranges = self.data["seeds"]
        min_for_ranges = []
        for i in range(0, len(seed_ranges) - 1, 2):
            seed_range = [
                *range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1] + 1)
            ]
            min_for_ranges.append(self.get_min_location(seed_range))
        return min(min_for_ranges)

    def get_min_location(self, seeds: List[int]) -> int:
        maps = self.data["maps"]
        locations = []

        for location in seeds:
            for map in maps:
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
                if location in map["map"]:
                    location = map["map"][location]
            locations.append(location)
        return min(locations)

    def parse_data(self, data: List[str]) -> any:
        maps = []

        source = None
        dest = None
        map = []

        for i, line in enumerate(data):
            if i == 0:
                continue

            if line == "":
                if source is not None:
                    maps.append(
                        {
                            "source": source,
                            "dest": dest,
                            "map": map,
                        }
                    )
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
                parts = line.split(" ")[0].split("-")
                source = parts[0]
                dest = parts[2]

        maps.append(
            {
                "source": source,
                "dest": dest,
                "map": map,
            }
        )

        return {
            "seeds": [int(i) for i in data[0].split(":")[1].split()],
            "maps": maps,
        }
