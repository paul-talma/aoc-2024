#ifndef PQ_H
#define PQ_H

#include "utils.h"
#include <functional>
#include <queue>
#include <utility>
#include <vector>

struct StateCost {
  State state;
  int cost;

  StateCost(const State &s, int c) : state(s), cost(c) {}
  bool operator>(const StateCost &other) const { return cost > other.cost; }
};

class PQ {
private:
  std::priority_queue<StateCost, std::vector<StateCost>,
                      std::greater<StateCost>>
      pq;

public:
  bool empty() const;
  size_t size() const;
  void push(const State &state, int cost);
  StateCost peek() const;
  std::pair<State, int> pop();
};

#endif
