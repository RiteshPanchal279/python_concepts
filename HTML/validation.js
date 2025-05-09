document.getElementById("regform").addEventListener("submit", function (event) {
  event.preventDefault();

  let valid = true;

  //name validation
  const name = document.getElementById("name").value;
  if (name === "" || !/^[a-zA-Z ]+$/.test(name)) {
    document.getElementById("nameError").textContent = "Enter valid name";
    valid = false;
  } else {
    document.getElementById("nameError").textContent = "";
  }

  //Email verification
  const email = document.getElementById("email").value;
  if (email === "" || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    document.getElementById("mailerror").textContent = "Enter valid email";
    valid = false;
  } else {
    document.getElementById("mailerror").textContent = "";
  }

  // Password and CNF Passowrd Validation
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("cpassword").value;
  const passwordError = document.getElementById("passworderror");
  const confirmPasswordError = document.getElementById("cpassworderror");
  if (
    password.length < 8 ||
    !/[A-Z]/.test(password) ||
    !/[a-z]/.test(password) ||
    !/[0-9]/.test(password)
  ) {
    passwordError.textContent =
      "Password must be at least 8 characters and include uppercase, lowercase, and a number.";
    valid = false;
  } else {
    passwordError.textContent = "";
  }
  if (password !== confirmPassword) {
    confirmPasswordError.textContent = "Passwords do not match.";
    valid = false;
  } else {
    confirmPasswordError.textContent = "";
  }

  //   ------------->
  const phone = document.getElementById("phone").value;
  if (phone === "" || !/^\d{10}$/.test(phone)) {
    document.getElementById("phoneError").textContent =
      "Please enter a valid 10-digit phone number.";
    valid = false;
  } else {
    document.getElementById("phoneError").textContent = "";
  }
  const dob = document.getElementById("dob").value;
  if (dob === "") {
    document.getElementById("dobError").textContent =
      "Please enter your date of birth.";
    valid = false;
  } else {
    document.getElementById("dobError").textContent = "";
  }
  const age = document.getElementById("age").value;
  if (age < 18 || age > 100) {
    document.getElementById("ageError").textContent =
      "Please enter a valid age between 18 and 100.";
    valid = false;
  } else {
    document.getElementById("ageError").textContent = "";
  }
  const genderMale = document.getElementById("male").checked;
  const genderFemale = document.getElementById("female").checked;
  if (!genderMale && !genderFemale) {
    document.getElementById("genderError").textContent =
      "Please select your gender.";
    valid = false;
  } else {
    document.getElementById("genderError").textContent = "";
  }
  // Website Validation
  const website = document.getElementById('website').value;
  if (website === '' || !/^https?:\/\/[^\s$.?#].[^\s]*$/.test(website)) {
    document.getElementById('websiteError').textContent = 'Please enter a valid website URL.';
    valid = false;
  } else {
    document.getElementById('websiteError').textContent = '';
  }

  const country = document.getElementById('country').value;
  if (country === '') {
    document.getElementById('countryError').textContent = 'Please select your country.';
    valid = false;
  } else {
    document.getElementById('countryError').textContent = '';
  }

  // Message (Textarea) Validation
  const message = document.getElementById('message').value.trim();
  if (message === '' || message.length < 10) {
    document.getElementById('messageError').textContent = 'Please enter a message with at least 10 characters.';
    valid = false;
  } else {
    document.getElementById('messageError').textContent = '';
  }

  // Terms and Conditions Validation
  const terms = document.getElementById('terms').checked;
  if (!terms) {
    document.getElementById('termsError').textContent = 'You must agree to the terms and conditions.';
    valid = false;
  } else {
    document.getElementById('termsError').textContent = '';
  }

  // Final Validation Check
  if (valid) {
    alert('Form submitted successfully!');
    // You can send the form data to the server here
  }

});
