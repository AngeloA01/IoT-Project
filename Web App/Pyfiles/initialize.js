async function getResult() {
  const response = await fetch("http://localhost:5000/");
  const result = await response.json();
  document.getElementById("result").innerHTML = result;
}
