#include "aoc17-utils.h"
#include <string>

int main() {
  Registers registers;
  Program program;
  Output output;
  InstructionPointer IP = 0;
  std::string path = "test.txt";
  parseInput(path, program, registers);
  int programLength = program.size();
  while (IP < programLength) {
    Instruction inst = program[IP];
    execute(inst, registers, IP, output);
  }
  printOutput(output);
  return 0;
}
