const destinations = [
  { name: "Persepolis", region: "Shiraz" },
  { name: "Hafez Mausoleum", region: "Shiraz" },
  { name: "Naqsh-e Jahan Square", region: "Isfahan" },
  { name: "Si-o-se-pol Bridge", region: "Isfahan" },
  { name: "Milad Tower", region: "Tehran" },
  { name: "Golestan Palace", region: "Tehran" },
  { name: "Chamran Park", region: "Karaj" },
  { name: "Little Iran Park", region: "Karaj" },
  { name: "Imam Reza Shrine", region: "Mashhad" },
  { name: "Ferdosi Mausoleum", region: "Mashhad" },
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
