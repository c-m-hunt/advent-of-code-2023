from typing import List

from advent import utils


class Solution(utils.DaySolution):
    day = 5

    def solve_part_1(self):
        seeds = self.data["seeds"]
        maps = self.data["maps"]
        locations = []
        
        for location in seeds:
            print(location)
            for map in maps:
                if location in map["map"]:
                    location = map["map"][location]
                print(location)
            print("----")
            locations.append(location)
        return min(locations)

    def solve_part_2(self):
        pass

    def parse_data(self, data: List[str]) -> any:
        maps = []
        
        source = None
        dest = None
        map = {}
        
        for i, line in enumerate(data):
            if i == 0:
                continue
            
            if line == "":
                if source is not None:
                    maps.append({
                        "source": source,
                        "dest": dest,
                        "map": map,
                    })
                    source = None
                    dest = None
                    map = {}
                continue
            if line[0].isdigit():
                source_start, dest_start, length = line.split()
                for i in range(0, int(length)):
                    map[int(dest_start) + i] = int(source_start) + i
                
            else:
                parts = line.split(" ")[0].split("-")
                source = parts[0]
                dest = parts[2]
            
        maps.append({
            "source": source,
            "dest": dest,
            "map": map,
        })
        
        return {
            "seeds": [ int(i) for i in data[0].split(":")[1].split()],
            "maps": maps,
        }


