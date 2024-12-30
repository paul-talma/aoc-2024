#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#include "pq.h"
#include "utils.h"

// Globals
Map map;

Dir N = Dir(-1, 0);
Dir S = Dir(1, 0);
Dir E = Dir(0, 1);
Dir W = Dir(0, -1);

std::vector<Dir> dirs = {N, S, E, W};

Action L = Action('L', 1000);
Action R = Action('R', 1000);
Action F = Action('F', 1);

std::vector<Action> actions = {L, R, F};

std::map<std::pair<Dir, Action>, Dir> turns = {
    {{N, L}, W}, {{N, R}, E}, {{S, L}, E}, {{S, R}, W},
    {{E, L}, N}, {{E, R}, S}, {{W, L}, S}, {{W, R}, N},
};

void getMap(const std::string &path, Map &map, Pos &start_pos, Pos &end_pos) {
  std::ifstream input(path);
  std::string line;
  if (!input.is_open()) {
    throw std::runtime_error("Could not open file: " + path);
  }
  int x_val = 0;
  while (std::getline(input, line)) {
    std::vector<char> currLine;
    int y_val = 0;
    for (char ch : line) {
      currLine.push_back(ch);
      if (ch == 'S') {
        start_pos.x = x_val;
        start_pos.y = y_val;
      } else if (ch == 'E') {
        end_pos.x = x_val;
        end_pos.y = y_val;
      }
    }
    map.push_back(currLine);
    x_val++;
  }
}

bool clear(const State &state, const Dir &dir) {
  return map[state.pos.x + dir.x][state.pos.y + dir.y] == '.';
}

bool valid(const Action &action, const State &state) {
  if (action == F) {
    return clear(state, state.dir);
  }
  return clear(state, turns[{state.dir, action}]);
}

State updateState(State &state, const Action &action) {
  if (action == F) {
    int x = state.pos.x + state.dir.x;
    int y = state.pos.y + state.dir.y;
    return State(Pos(x, y), state.dir);
  }
  return State(state.pos, turns[{state.dir, action}]);
}

bool isGoal(State s, Pos end_pos) {
  int x = s.pos.x;
  int y = s.pos.y;
  return (x == end_pos.x) && (y == end_pos.y);
}

int UCS(Pos &start_pos, Pos end_pos) {
  State currState = State(start_pos, E);
  std::set<Pos> visited;
  PQ pq;
  pq.push(currState, 0);

  while (!pq.empty()) {
    auto [state, cost] = pq.pop();
    visited.insert(state.pos);
    for (Action action : actions) {
      if (valid(action, state)) {
        State next_state = updateState(state, action);
        if (isGoal(next_state, end_pos)) {
          return cost + 1;
        }
        if (!visited.contains(state.pos)) {
          int next_cost = cost += action.cost;
          pq.push(next_state, next_cost);
        }
      }
    }
  }
  return -1;
}

int main() {
  std::string path = "test.txt";
  Pos start_pos;
  Pos end_pos;

  getMap(path, map, start_pos, end_pos);
  int cost = UCS(start_pos, end_pos);
  std::cout << "Minimal path cost: " << cost << std::endl;

  return 0;
}
