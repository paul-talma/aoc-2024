#ifndef UTILS_H
#define UTILS_H

#include <map>
#include <string>
#include <vector>
typedef std::vector<std::vector<char>> Map;

struct Pos {
  int x, y;
  auto operator<=>(const Pos &) const = default;
};

struct Dir {
  int x, y;
  auto operator<=>(const Dir &) const = default;
};

struct Action {
  char name;
  int cost;
  auto operator<=>(const Action &) const = default;

  Action(char name, int cost) : name(name), cost(cost) {}
};

struct State {
  Pos pos;
  Dir dir;

  State(Pos p, Dir d) : pos(p), dir(d) {}
};

#endif
