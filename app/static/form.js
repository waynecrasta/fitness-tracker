const plusTenButton = document.getElementById("plusTenButton");
const quantityInput = document.getElementById("quantity");
let quantityValue = quantityInput.value;
quantityValue =
  quantityValue === ""
    ? (quantityValue = 0)
    : (quantityValue = parseInt(quantityValue));

plusTenButton.onclick = () => {
  quantityValue += 10;
  quantityInput.value = quantityValue;
};
