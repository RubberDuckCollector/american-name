const prompt = require("prompt-sync")();

function main() {
  let american_dict = {
    a: "freedom",
    b: "spray cheese",
    c: "smith",
    d: "guns",
    e: "bill",
    f: "hudson",
    g: "cultural appropriation",
    h: "beer",
    i: "war",
    j: "corn",
    k: "football",
    l: "burger",
    m: "ayden",
    n: "shooting",
    o: "military",
    p: "mcdonald's",
    q: "walmart",
    r: "johnson",
    s: "fried chicken",
    t: "nationalism",
    u: "racism",
    v: "leigh",
    w: "thanksgiving",
    x: "nascar",
    y: "ie",
    z: "capitalism",
  };

  let user_input_name = prompt("Enter your name: ");
  let new_name = "";

  for (var i in user_input_name) {
    new_name += american_dict[user_input_name[i]];
  }
  console.log(new_name);
}

main();
