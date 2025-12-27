import importlib
import os
import sys

class CalcuFunction:
    _extension_dir = os.path.dirname(os.path.abspath(__file__))

    # ----------------
    # Core math
    # ----------------
    @staticmethod
    def add(a, b): return a + b

    @staticmethod
    def sub(a, b): return a - b

    @staticmethod
    def product(a, b): return a * b

    @staticmethod
    def div(a, b): return a / b

    @staticmethod
    def exp(a, b): return a ** b

    @staticmethod
    def floor(a, b): return a // b

    # ----------------
    # CLI Calculator
    # ----------------
    @staticmethod
    def calculator():
        print("CalcuFunction Calculator")

        op = input("ENTER OPERATOR (+, -, *, /, //, ^): ")
        n1 = int(input("ENTER 1st NUMBER: "))
        n2 = int(input("ENTER 2nd NUMBER: "))

        if op == "+":
            print(CalcuFunction.add(n1, n2))
        elif op == "-":
            print(CalcuFunction.sub(n1, n2))
        elif op == "*":
            print(CalcuFunction.product(n1, n2))
        elif op == "/":
            print(CalcuFunction.div(n1, n2))
        elif op == "//":
            print(CalcuFunction.floor(n1, n2))
        elif op == "^":
            print(CalcuFunction.exp(n1, n2))
        else:
            print("ERROR! Invalid operator!")

    # ----------------
    # Extensions
    # ----------------
    @staticmethod
    def load(filename):
        if not filename.endswith(".py"):
            filename += ".py"

        module_name = filename[:-3]
        if CalcuFunction._extension_dir not in sys.path:
            sys.path.append(CalcuFunction._extension_dir)

        module = importlib.import_module(module_name)

        if hasattr(module, "CalcuFunction"):
            for attr in dir(module.CalcuFunction):
                if not attr.startswith("_"):
                    setattr(CalcuFunction, attr, getattr(module.CalcuFunction, attr))
