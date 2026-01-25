const modal = document.getElementById("myModal");
  const btn = document.getElementById("addCard");
  const span = document.querySelector(".close");

  btn.onclick = () => modal.style.display = "block";
  span.onclick = () => modal.style.display = "none";
  window.onclick = (event) => {
    if (event.target == modal) modal.style.display = "none";
  };

  document.getElementById("popupForm").onsubmit = (e) => {
    e.preventDefault();
    alert("Form submitted!");
    modal.style.display = "none";
  };
