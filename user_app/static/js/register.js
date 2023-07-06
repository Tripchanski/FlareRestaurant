let numberInput = document.querySelector('.phone-number')
let nameInput = document.querySelector('.username')
let passwordInput = document.querySelector('.password')
console.log(nameInput)
numberInput.addEventListener('input', function(event) {
    let inputValue = event.target.value;
    let numericValue = parseFloat(inputValue);
    if (isNaN(numericValue)) {
        event.target.value = '';
    } else {
        event.target.value = numericValue;
    }
})

nameInput.addEventListener('input', function(event) {
    let inputValue = event.target.value;
    let filteredValue = inputValue.replace(/[^a-zA-Z]/g, '');
    if (filteredValue !== inputValue)  {
        event.target.value = filteredValue;
    }
})

passwordInput.addEventListener('input', function(event) {
    let inputValue = event.target.value;
    let filteredValue = inputValue.replace(/[^a-zA-Z0-9]/g, '');
    if (filteredValue !== inputValue)  {
        event.target.value = filteredValue;
    }
})