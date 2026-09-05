async function fetchSupportedCurrencies() {
    try {
        const response = await fetch("https://v6.exchangerate-api.com/v6/70d85c2fd3650203209fe917/codes");
        const data = await response.json();
        const supportedCodesArray = data["supported_codes"];
        return supportedCodesArray;
    } catch (error) {
        console.log(error);
    }
}

function populateDropdowns(data) {
    for (item of data) {
        let currencyOption = document.createElement("option");
        currencyOption.innerText = item[1];
        currencyOption.value = item[0];
        let currencyOptionDuplicate = document.createElement("option");
        currencyOptionDuplicate.innerText = item[1];
        currencyOptionDuplicate.value = item[0];
        let currrentCurrencyDropdown = document.getElementById("current-currency");
        let desiredCurrencyDropdown = document.getElementById("desired-currency");
        currrentCurrencyDropdown.append(currencyOption);
        desiredCurrencyDropdown.append(currencyOptionDuplicate);
    }

}

async function fetchToPopulate() {
    let result = await fetchSupportedCurrencies();
    populateDropdowns(result);
}
fetchToPopulate();

async function fetchConversionRate (currentCurrency, desiredCurrency, amount) {
    try {
        const response = await fetch(`https://v6.exchangerate-api.com/v6/70d85c2fd3650203209fe917/pair/${currentCurrency}/${desiredCurrency}/${amount}`);
        const data = await response.json();
        let result = data["conversion_result"];
        return result;
    } catch (error) {
        console.log(error);
    }
}

async function formSubmission(e) {
    e.preventDefault();
    let currentCurrency = document.getElementById("current-currency");
    let desiredCurrency = document.getElementById("desired-currency");
    let amount = document.getElementById("amount");
    let currentCurrencyValue = currentCurrency.value;
    let desiredCurrencyValue = desiredCurrency.value;
    let amountValue = amount.value;
    let convertedAmount = await fetchConversionRate(currentCurrencyValue, desiredCurrencyValue, amountValue);
    const resultDiv = document.querySelector("#result-div");
    resultDiv.innerHTML = "";
    const h3 = document.createElement("h3");
    h3.innerText = convertedAmount;
    resultDiv.append(h3);
}

let form = document.querySelector("#currency-converter-input");
form.addEventListener("submit", formSubmission)