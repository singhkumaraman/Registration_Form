const submitButton = document.querySelector(".submit");

submitButton.addEventListener("click", () => {
  const firstName = document.querySelector("#firstName").value;
  const lastName = document.querySelector("#lastName").value;
  const Address = document.querySelector(".address").value;
  const gender = document.querySelector(".gender").value;
  const state = document.querySelector(".state").value;
  const city = document.querySelector(".city").value;
  const Dob = document.querySelector(".dob").value;
  const pinCode = document.querySelector(".pincode").value;
  const course = document.querySelector(".course").value;
  const Email = document.querySelector(".emailid").value;

  fetch(
    "http://127.0.0.1:8000/login/create_user" +
      `?firstName=${firstName}&lastName=${lastName}&Address=${Address}&gender=${gender}` +
      `&state=${state}&city=${city}&Dob=${Dob}&pinCode=${pinCode}&course=${course}&Email=${Email}`
  )
    .then((data) => data.text())
    .then((value) => console.log(value))
    .catch((e) => console.log(e));
});
const reset = document.querySelector(".reset");
reset.addEventListener("click", () => {
  const form = document.querySelector("form");
  form.reset();
});
