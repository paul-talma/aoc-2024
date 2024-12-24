#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <ostream>
#include <string>
#include <type_traits>
#include <utility>
#include <vector>

typedef std::vector<std::vector<char>> Map;
typedef std::vector<char> Directions;
typedef char Direction;

struct Position {
  int x;
  int y;

  Position(int x_val, int y_val) : x(x_val), y(y_val) {}
};

std::pair<Map, Directions> mapAndDirections(std::string path) {
  Map map;
  Directions dirs;
  bool processingMap = true;
  std::ifstream input(path);
  std::string line;
  if (input.is_open()) {
    while (std::getline(input, line)) {
      if (line.empty()) {
        processingMap = false;
      }
      std::vector<char> currLine;
      for (char ch : line) {
        currLine.push_back(ch);
      }
      if (processingMap) {
        map.push_back(currLine);
      } else {
        dirs = currLine;
      }
    }
    return {map, dirs};
  } else {
  }
}

Position nextPos(Map &map, Position pos, Direction dir) {
  int x = pos.x;
  int y = pos.y;
  if (dir == '^') {
    return Position(x, y - 1);
  }
  if (dir == 'v') {
    return Position(x, y + 1);
  }
  if (dir == '>') {
    return Position(x + 1, y);
  }
  return Position(x - 1, y);
}

char readMap(Map &map, Position pos) { return map[pos.y][pos.x]; }

int numMoves(Map &map, Position pos, Direction dir) {
  int count = 0;
  Position currPos = pos;
  while (readMap(map, currPos) != '#' && readMap(map, currPos) != '.') {
    currPos = nextPos(map, currPos, dir);
    count++;
  }
  if (readMap(map, currPos) == '#') {
    return 0;
  }
  return count;
}

Position shiftUp(Map &map, Position pos, int moves) {
  int x = pos.x;
  int y = pos.y;
  for (int i = moves; i >= 0; i--) {
    map[y - i][x] = map[y - (i - 1)][x];
  }
  return Position(x, y - 1);
}

Position shiftDown(Map &map, Position pos, int moves) {
  int x = pos.x;
  int y = pos.y;
  for (int i = moves; i >= 0; i--) {
    map[y + i][x] = map[y + (i - 1)][x];
  }
  return Position(x, y + 1);
}

Position shiftLeft(Map &map, Position pos, int moves) {
  int x = pos.x;
  int y = pos.y;
  for (int i = moves; i >= 0; i--) {
    map[y][x - i] = map[y][x - (i - 1)];
  }
  return Position(x - 1, y);
}

Position shiftRight(Map &map, Position pos, int moves) {
  int x = pos.x;
  int y = pos.y;
  for (int i = moves; i >= 0; i--) {
    map[y][x + i] = map[y][x + (i - 1)];
  }
  return Position(x + 1, y);
}

Position updateMap(Map &map, Position pos, Direction dir) {
  int moves = numMoves(map, pos, dir);
  if (dir == '^') {
    return shiftUp(map, pos, moves);
  } else if (dir == '>') {
    return shiftRight(map, pos, moves);
  } else if (dir == 'v') {
    return shiftDown(map, pos, moves);
  } else {
    return shiftLeft(map, pos, moves);
  }
}

void printMap(Map &map) {
  for (std::vector<char> line : map) {
    for (char ch : line) {
      std::cout << ch;
    }
    std::cout << std::endl;
  }
}

Position getRobotPos(Map &map) {
  int x = 0, y = 0;
  for (std::vector<char> row : map) {
    for (char ch : row) {
      if (ch == '@') {
        return Position(x, y);
      }
      x++;
    }
    y++;
  }
}

void computeFinalMap(Map &map, Directions dirs) {
  Position currPos = getRobotPos(map);
  for (Direction dir : dirs) {
    currPos = updateMap(map, currPos, dir);
  }
}

int main() {
  std::string path = "test.txt";
  std::pair<Map, Directions> mAndD = mapAndDirections(path);
  Map map = mAndD.first;
  Directions dirs = mAndD.second;
  computeFinalMap(map, dirs);
  printMap(map);
}
