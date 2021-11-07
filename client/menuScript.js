let numberOfIngredient = 0;
async function addToMenu() {
  // console.log(numberOfIngredient);
  let ingredientArray = [];
  for (let i = 1; i <= numberOfIngredient; i++) {
    let ingredient = document.getElementById(i).value;
    ingredientArray.push(ingredient);
  }
  console.log(ingredientArray);
  let obj = {};
  obj["name"] = document.getElementById("itemName").value;
  obj["price"] = document.getElementById("itemPrice").value;
  obj["ingredientArray"] = ingredientArray;
  const response = await fetch("http://localhost:8000/api/add_to_menu", {
    method: "POST",
    mode: "cors",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(obj),
  })
    .then((res) => {
      console.log(res);
      location.reload();
      return false;
    })
    .catch((e) => console.log(e));
}
async function addIngredientTile() {
  numberOfIngredient++;
  let elem = document.getElementById("input-tile");
  let newDiv = document.createElement("div");
  newDiv.setAttribute("id", "ingredient-list");
  let newInputField = document.createElement("input");
  newInputField.setAttribute("id", `${numberOfIngredient}`);
  newInputField.setAttribute("type", "text");
  newInputField.setAttribute("placeholder", "Add Ingredients");
  let newButton = document.createElement("button");
  newButton.innerHTML = "X";
  newButton.setAttribute("onClick", "removeIngredientTile()");
  elem.appendChild(newDiv);
  newDiv.appendChild(newInputField);
  newDiv.appendChild(newButton);
}

async function removeIngredientTile() {
  let elem = document.getElementById("input-tile");
  elem.removeChild(elem.lastChild);
}
