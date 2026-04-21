function validateForm() {
    let name = document.getElementById("name").value.trim();
    let phone = document.getElementById("phone").value.trim();

    // Name validation (only letters and spaces)
    if (name === "" || !/^[A-Za-z ]+$/.test(name)) {
        alert("Enter valid name");
        return false;
    }

    // Phone validation (exactly 10 digits)
    if (!/^[0-9]{10}$/.test(phone)) {
        alert("Enter valid 10-digit phone number");
        return false;
    }

    return true;
}