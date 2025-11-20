const destinations = [
  { name: "Persepolis", region: "Fars Province" },
  { name: "Naqsh-e Jahan Square", region: "Isfahan" },
  { name: "Badab Soort", region: "Mazandaran" },
  { name: "Kandovan Village", region: "East Azerbaijan" },
  { name: "Lut Desert", region: "Kerman" },
  { name: "Caspian Forests", region: "Gilan" },
];

const btn = document.getElementById("random-trip-btn");
const popup = document.getElementById("random-popup");
const randomDestination = document.getElementById("random-destination");
const closeBtn = document.getElementById("close-popup");

btn.addEventListener("click", () => {
  const random = destinations[Math.floor(Math.random() * destinations.length)];
  randomDestination.textContent = `${random.name} – ${random.region}`;
  popup.classList.remove("hidden");
});

closeBtn.addEventListener("click", () => {
  popup.classList.add("hidden");
});

window.addEventListener("click", (e) => {
  if (e.target === popup) popup.classList.add("hidden");
});
