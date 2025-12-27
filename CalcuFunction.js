const readline = require("readline");

const CalcuFunction = {
  add: (a, b) => a + b,
  sub: (a, b) => a - b,
  product: (a, b) => a * b,
  div: (a, b) => a / b,
  exp: (a, b) => a ** b,
  floor: (a, b) => Math.floor(a / b),

  calculator() {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    console.log("CalcuFunction Calculator");

    rl.question("ENTER OPERATOR (+, -, *, /, //, ^): ", op => {
      rl.question("ENTER 1st NUMBER: ", n1 => {
        rl.question("ENTER 2nd NUMBER: ", n2 => {
          n1 = Number(n1);
          n2 = Number(n2);

          let result;
          switch (op) {
            case "+": result = this.add(n1, n2); break;
            case "-": result = this.sub(n1, n2); break;
            case "*": result = this.product(n1, n2); break;
            case "/": result = this.div(n1, n2); break;
            case "//": result = this.floor(n1, n2); break;
            case "^": result = this.exp(n1, n2); break;
            default:
              console.log("ERROR! Invalid operator!");
              rl.close();
              return;
          }

          console.log(result);
          rl.close();
        });
      });
    });
  }
};

module.exports = CalcuFunction;
