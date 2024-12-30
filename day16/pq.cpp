#include "pq.h"
#include "utils.h"
#include <stdexcept>
#include <utility>

bool PQ::empty() const { return pq.empty(); }

size_t PQ::size() const { return pq.size(); }

void PQ::push(const State &state, int cost) { pq.push(StateCost(state, cost)); }

StateCost PQ::peek() const {
  if (empty()) {
    throw std::runtime_error("Priority queue is empty!");
  }

  return pq.top();
}

std::pair<State, int> PQ::pop() {
  if (empty()) {
    throw std::runtime_error("Priority queue is empty!");
  }

  StateCost s = peek();
  pq.pop();
  return std::make_pair(s.state, s.cost);
}
