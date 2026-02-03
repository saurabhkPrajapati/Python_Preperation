const districtsByState = {
    karnataka: ["Bangalore", "Mysore", "Mangalore"],
    maharashtra: ["Mumbai", "Pune", "Nagpur"],
    tamilnadu: ["Chennai", "Coimbatore", "Madurai"],
    kerala: ["Kochi", "Trivandrum", "Kozhikode"],
    telangana: ["Hyderabad", "Warangal", "Nizamabad"]
};

const stateSelect = document.getElementById("state");
const districtSelect = document.getElementById("district");

stateSelect.addEventListener("change", function () {
    const selectedState = this.value;
    districtSelect.innerHTML = '<option value="">Select District</option>';

    if (districtsByState[selectedState]) {
        districtsByState[selectedState].forEach(district => {
            const option = document.createElement("option");
            option.value = district;
            option.textContent = district;
            districtSelect.appendChild(option);
        });
    }
});

function resetGender() {
    document.querySelectorAll('input[name="gender"]').forEach(radio => {
        radio.checked = false;
    });
}
