#include "aoc17-utils.h"
#include <cmath>
#include <iostream>
#include <regex>
#include <string>

void parseInput(const std::string &path, Program &program,
                Registers &registers) {
  std::ifstream file(path);
  if (!file.is_open()) {
    throw std::runtime_error("Error: file not found " + path);
  }
  std::string line;
  while (std::getline(file, line)) {
    if (line[0] == 'R') {
      int reg = getNum(line);
      registers.push_back(reg);
    } else if (line[0] == 'P') {
      getProgram(line, program);
    }
  }
}

int getNum(std::string &line) {
  std::regex pattern(R"(\d+)");
  std::smatch match;
  std::regex_search(line, match, pattern);
  return std::stoi(match[0]);
}

void getProgram(std::string &line, Program &program) {
  std::regex pattern(R"((\d+),(\d+))");
  std::smatch match;
  while (std::regex_search(line, match, pattern)) {
    Name name = static_cast<Name>(matchToInt(match, 0));
    int input = matchToInt(match, 0);
    Instruction inst = Instruction(name, input);
    program.push_back(inst);
  }
}

int matchToInt(std::smatch &match, int index) {
  return std::stoi(match[index].str());
}

int combo(int val, Registers &registers) {
  switch (val) {
  case 4:
    return registers[a];
  case 5:
    return registers[b];
  case 6:
    return registers[c];
  default:
    return val;
  }
}

void write(int res, Registers &registers, Register reg) {
  registers[reg] = res;
}

void jump(int val, InstructionPointer &IP) { IP = val; }

void execute(Instruction &inst, Registers &registers, InstructionPointer &IP,
             Output &output) {
  Name name = inst.name;
  int operand;
  int res;
  switch (name) {
  case adv: {
    operand = combo(inst.operand, registers);
    int num = registers[a];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, a);
    IP++;
    break;
  }

  case bxl: {
    operand = inst.operand;
    int reg = registers[b];
    res = operand ^ reg;
    write(res, registers, b);
    IP++;
    break;
  }

  case bst: {
    operand = combo(inst.operand, registers);
    operand %= 8;
    write(operand, registers, b);
    IP++;
    break;
  }
  case jnz: {
    if (registers[a] == 0) {
      break;
    }
    jump(inst.operand, IP);
    break;
  }

  case bxc: {
    res = registers[b] ^ registers[c];
    write(res, registers, b);
    IP++;
    break;
  }

  case out: {
    operand = combo(inst.operand, registers);
    operand %= 8;
    output.push_back(operand);
    IP++;
    break;
  }

  case bdv: {
    operand = combo(inst.operand, registers);
    int num = registers[b];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, b);
    IP++;
    break;
  }

  case cdv: {
    operand = combo(inst.operand, registers);
    int num = registers[c];
    int div = pow(2, operand);
    res = num / div;
    write(res, registers, c);
    IP++;
    break;
  }
  }
}

void printOutput(Output &output) {
  for (int x : output) {
    std::cout << x << ',';
  }
  std::cout << '\n';
}
