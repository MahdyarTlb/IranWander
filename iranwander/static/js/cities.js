const cityData = {
  // 💡 نکته: نام شهرها باید دقیقاً با City.name در دیتابیس مطابقت داشته باشد
  Tehran: {
    attractions: [
      // 👈 آدرس‌های اصلاح شده
      { title: "Milad Tower", img: "/static/img/miladmodal.jpg", link: "/city/Milad-Tower" },
      { title: "Golestan Palace", img: "/static/img/golestanmodal.jpg", link: "/city/Golestan-Palace" },
    ],
  },
  Isfahan: {
    attractions: [
      { title: "Naqsh-e Jahan Square", img: "/static/img/naqshemodal.jpg", link: "/city/Naqsh-e-Jahan-Square" },
      { title: "Si-o-se-pol Bridge", img: "/static/img/Si-o-se-polmodal.jpg", link: "/city/Si-o-se-pol-Bridge" },
    ],
  },
  Shiraz: {
    attractions: [
      { title: "Hafez Mausoleum", img: "/static/img/hafezmodal.jpg", link: "/city/Hafez-Mausoleum" },
      { title: "Persepolis", img: "/static/img/jamshidmodal.jpg", link: "/city/Persepolis" },
    ],
  },
  Karaj: {
    attractions: [
      { title: "Chamran Park", img: "/static/img/chamranmodal.jpg", link: "/city/Chamran-Park" },
      { title: "Little Iran Park", img: "/static/img/littleiranmodal.jpg", link: "/city/Little-Iran-Park" },
    ],
  },
  Mashhad: {
    attractions: [
      { title: "Imam Reza Shrine", img: "/static/img/emammodal.jpg", link: "/city/Imam-Reza-Shrine" },
      { title: "Ferdosi Mausoleum", img: "/static/img/ferdosimodal.jpg", link: "/city/Ferdosi-Mausoleum" },
    ],
  },
};

const buttons = document.querySelectorAll(".btn");
const overlay = document.getElementById("overlay");
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modal-content");

buttons.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    e.preventDefault();

    // 👈 از textContent.trim() استفاده کنید تا نام شهر بدون فاصله اضافی گرفته شود
    const cityName = btn.parentElement.querySelector("h3").textContent.trim();
    const cityInfo = cityData[cityName];

    if (!cityInfo) return;

    modalContent.innerHTML = cityInfo.attractions
      .map(
        (a) => `
            <div class="attraction-card">
                <img src="${a.img}">
                <h4>${a.title}</h4>
                <a class="more-btn" href="${a.link}">More Info</a>
            </div>
        `
      )
      .join("");

    overlay.classList.remove("hidden");
    modal.classList.remove("hidden");
  });
});

overlay.addEventListener("click", () => {
  overlay.classList.add("hidden");
  modal.classList.add("hidden");
});

document.querySelectorAll(".like-icon").forEach((icon) => {
  icon.addEventListener("click", () => {
    icon.classList.toggle("liked");
  });
});
