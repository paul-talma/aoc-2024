#include <fstream>
#include <regex>
#include <stdexcept>
#include <string>
#include <vector>

enum Register { a, b, c };

enum Name {
  adv,
  bxl,
  bst,
  jnz,
  bxc,
  out,
  bdv,
  cdv,
};

struct Instruction {
  Name name;
  int operand;

  Instruction(Name name, int input) : name(name), operand(input) {};
};

typedef std::vector<Instruction> Program;
typedef int InstructionPointer;
typedef std::vector<int> Registers;
typedef std::vector<int> Output;

void parseInput(std::string &path, Program &program, Registers &registers);

int getNum(std::string &line);
void getProgram(std::string &line, Program &program);
int matchToInt(std::smatch &match, int index);
int combo(int val, Registers &registers);
void write(int res, Registers &registers, Register reg);
void jump(int val, InstructionPointer &IP);
void execute(Instruction &inst, Registers &registers, InstructionPointer &IP,
             Output &output);
void printOutput(Output &output);
