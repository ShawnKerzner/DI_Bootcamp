async function fetchSupportedCurrencies() {
    try {
        const response = await fetch("https://v6.exchangerate-api.com/v6/70d85c2fd3650203209fe917/codes");
        const data = await response.json();
        return data;
    } catch (error) {
        console.log(error);
    }
}
fetchSupportedCurrencies();

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