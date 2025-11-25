// cities.js — نسخه نهایی، کامل، بدون باگ، با لایک و مودال رویایی
const cityData = {
  Tehran: {
    attractions: [
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
  // اگه شهر دیگه‌ای اضافه کردی، اینجا بذار
};

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".btn");
  const overlay = document.getElementById("overlay");
  const modal = document.getElementById("modal");
  const modalContent = document.getElementById("modal-content");

  // باز کردن مودال
  buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      // اگه روی قلب لایک کلیک کرد، مودال باز نشه
      if (e.target.closest(".like-icon")) return;

      e.preventDefault();

      const cityName = btn.parentElement.querySelector("h3").textContent.trim();
      const cityInfo = cityData[cityName];

      if (!cityInfo) {
        console.warn("شهر پیدا نشد:", cityName);
        return;
      }

      // پر کردن محتوای مودال
      modalContent.innerHTML = cityInfo.attractions
        .map(
          (a) => `
            <div class="attraction-card">
                <img src="${a.img}" alt="${a.title}" loading="lazy">
                <h4>${a.title}</h4>
                <a class="more-btn" href="${a.link}">More Info</a>
            </div>
          `
        )
        .join("");

      // نمایش مودال (اینجا باید add کنیم، نه remove!)
      overlay.classList.add("active");
      modal.classList.add("active");
    });
  });

  // بستن مودال با کلیک روی پس‌زمینه
  overlay.addEventListener("click", () => {
    overlay.classList.remove("active");
    modal.classList.remove("active");
  });

  // بستن با کلید Esc
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      overlay.classList.remove("active");
      modal.classList.remove("active");
    }
  });

  // لایک واقعی (همون کد قبلی، بدون تغییر — کاملاً درست کار می‌کنه)
  document.querySelectorAll(".like-icon").forEach((icon) => {
    icon.addEventListener("click", async function (e) {
      e.stopPropagation(); // جلوی باز شدن مودال رو بگیره

      const cityId = this.getAttribute("data-city-id");
      if (!cityId) return;

      // لودینگ
      this.style.opacity = "0.6";
      this.style.pointerEvents = "none";

      try {
        const response = await fetch("/api/like", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ city_id: parseInt(cityId) }),
        });

        const data = await response.json();

        if (data.ok) {
          this.classList.toggle("liked");
        } else {
          alert("خطا: " + (data.error || "دوباره امتحان کن"));
        }
      } catch (err) {
        console.error(err);
        alert("مشکل اتصال!");
      } finally {
        this.style.opacity = "1";
        this.style.pointerEvents = "auto";
      }
    });
  });
});

// search bar
const popularCities = [
    "Tehran", "Isfahan", "Shiraz", "Mashhad", "Karaj"];

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('heroSearch');
    const suggestionsBox = document.getElementById('suggestions');
    const searchBtn = document.querySelector('.search-btn');

    if (!searchInput || !suggestionsBox) return;

    searchInput.addEventListener('input', function() {
        const query = this.value.trim();

        if (query.length === 0) {
            suggestionsBox.classList.remove('active');
            suggestionsBox.innerHTML = '';
            return;
        }

        const matches = popularCities
            .filter(city => city.toLowerCase().includes(query.toLowerCase()))
            .slice(0, 6);
        if (matches.length > 0) {
            suggestionsBox.innerHTML = matches.map(city => `
                <div class="suggestion-item" data-city="${city}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <circle cx="11" cy="11" r="8"/>
                        <path d="m21 21-4.35-4.35"/>
                    </svg>
                    <span>City <strong>${city}</strong></span>
                </div>
            `).join('');
            suggestionsBox.classList.add('active');
        } else {
            suggestionsBox.classList.remove('active');
        }
    });

    suggestionsBox.addEventListener('click', function(e) {
        const item = e.target.closest('.suggestion-item');
        if (item) {
            const city = item.dataset.city;
            window.location.href = `/city?q=${encodeURIComponent(city)}`;
        }
    });

    const goSearch = () => {
        const query = searchInput.value.trim();
        if (query) {
            window.location.href = `/city?q=${encodeURIComponent(query)}`;
        }
    };

    searchBtn?.addEventListener('click', e => { e.preventDefault(); goSearch(); });
    searchInput.addEventListener('keypress', e => {
        if (e.key === 'Enter') { e.preventDefault(); goSearch(); }
    });

    document.addEventListener('click', e => {
        if (!e.target.closest('.search-container')) {
            suggestionsBox.classList.remove('active');
        }
    });
});
