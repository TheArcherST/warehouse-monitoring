from typing import Iterable
from dataclasses import dataclass
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos
from pydantic import BaseModel


# Справочник маршрутов погрузчиков по складу.
# Каждый маршрут имеет id, id целевого стеллажа, а также набор контрольных точек.
# Каждая контрольная точка имеет свой id, имя, а также расстояние до следующей КТ
path_lib = {
    1: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 10},
            {"check_point_id": 3,
             "check_point_name": "K3",
             "next_check_point_distance": 10}
        ],
        "target_rack_id": "X1"},
    2: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 10},
            {"check_point_id": 3,
             "check_point_name": "K3",
             "next_check_point_distance": 15},
            {"check_point_id": 4,
             "check_point_name": "K4",
             "next_check_point_distance": 10}
        ],
        "target_rack_id": "X2"},
    3: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 5},
            {"check_point_id": 5,
             "check_point_name": "K5",
             "next_check_point_distance": 10},
            {"check_point_id": 6,
             "check_point_name": "K6",
             "next_check_point_distance": 10}
        ],
        "target_rack_id": "X3"},
    4: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 5},
            {"check_point_id": 5,
             "check_point_name": "K5",
             "next_check_point_distance": 10},
            {"check_point_id": 6,
             "check_point_name": "K6",
             "next_check_point_distance": 15},
            {"check_point_id": 7,
             "check_point_name": "K7",
             "next_check_point_distance": 10}
        ],
        "target_rack_id": "X4"},
    5: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 5},
            {"check_point_id": 5,
             "check_point_name": "K5",
             "next_check_point_distance": 5},
            {"check_point_id": 8,
             "check_point_name": "K8",
             "next_check_point_distance": 10},
            {"check_point_id": 9,
             "check_point_name": "K9",
             "next_check_point_distance": 5}
        ],
        "target_rack_id": "X5"},
    6: {"path_sequence": [
            {"check_point_id": 1,
             "check_point_name": "K1",
             "next_check_point_distance": 5},
            {"check_point_id": 2,
             "check_point_name": "K2",
             "next_check_point_distance": 5},
            {"check_point_id": 5,
             "check_point_name": "K5",
             "next_check_point_distance": 5},
            {"check_point_id": 8,
             "check_point_name": "K8",
             "next_check_point_distance": 10},
            {"check_point_id": 9,
             "check_point_name": "K9",
             "next_check_point_distance": 15},
            {"check_point_id": 10,
             "check_point_name": "K10",
             "next_check_point_distance": 10}
        ],
        "target_rack_id": "X6"}
}

# cities list
cities = [
    "Rostov-on-Don",
    "Moscow",
    "Krasnodar",
    "Tver",
    "Saint Petersburg",
    "Almaty"
]


class Configuration(BaseModel):
    warehouses: list[dtos.WarehouseDTO]


class Location(BaseModel):
    x: float
    y: float


checkpoints = {
    "K1": Location(x=35, y=0),
    "K2": Location(x=35, y=5),
    "K3": Location(x=25, y=5),
    "K4": Location(x=10, y=5),
    "K5": Location(x=35, y=10),
    "K6": Location(x=25, y=10),
    "K7": Location(x=10, y=10),
    "K8": Location(x=35, y=15),
    "K9": Location(x=25, y=15),
}


racks = {
    "K10": Location(x=10, y=15),
    "X1": Location(x=15, y=5),
    "X2": Location(x=0, y=5),
    "X3": Location(x=15, y=10),
    "X4": Location(x=0, y=10),
    "X5": Location(x=15, y=15),
    "X6": Location(x=0, y=15),
}


objects_on_map = checkpoints | racks


def get_object_location(unified_identifier: str):
    return objects_on_map[unified_identifier]


def sort_path(path: Iterable[str]) -> list[str]:
    rack_id = None
    n_path = []
    for i in path:
        label, number = i[0], i[1:]
        if label == 'X':
            rack_id = number
        else:
            n_path.append(int(number))
    return (['K{}'.format(i) for i in sorted(n_path)]
            + ([f'X{rack_id}'] if rack_id is not None else [] ))


def get_path_length(path: Iterable[str]):
    path = sort_path(path)
    it = map(get_object_location, path)
    current = next(it)
    result = 0
    for next_ in it:
        simplified_path_edge_length = (
            abs(current.x - next_.x)
            + abs(current.y - next_.y)
        )
        current = next_
        result += simplified_path_edge_length
    return result


def main():
    print(get_path_length(["K1", "K2", "K3", "X1"]))


if __name__ == '__main__':
    main()


class ParsedUnifiedIdentifier(BaseModel):
    literal: str
    identifier: int


def parse_unified_identifier(unif_id: str):
    return ParsedUnifiedIdentifier(
        literal=unif_id[0],
        identifier=int(unif_id[1:]),
    )
