function bannerPopUp() {
    alert("the sale ends in ten minutes")
}

function bannerTimer(banner) {
    setTimeout(banner, 5000);
}
// setTimeout(() => {
//     clearInterval(myInterval);
// };

bannerTimer(bannerPopUp);