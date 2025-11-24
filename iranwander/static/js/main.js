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
// User dropdown menu
document.addEventListener('DOMContentLoaded', () => {
    const avatarBtn = document.getElementById('avatarBtn');
    const dropdownMenu = document.getElementById('dropdownMenu');
    const userMenu = document.querySelector('.user-menu');

    if (avatarBtn && dropdownMenu) {
        avatarBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            userMenu.classList.toggle('active');
        });

        // بستن منو با کلیک بیرون
        document.addEventListener('click', (e) => {
            if (!userMenu.contains(e.target)) {
                userMenu.classList.remove('active');
            }
        });
    }
});
// آواتار رنگی بر اساس اسم کاربر (همه کاربرا رنگ متفاوت اما ثابت دارن!)
document.addEventListener('DOMContentLoaded', () => {
    const avatar = document.querySelector('.avatar-placeholder[data-username]');

    if (avatar) {
        const username = avatar.getAttribute('data-username') || 'A';
        let hash = 0;
        for (let i = 0; i < username.length; i++) {
            hash = username.charCodeAt(i) + ((hash << 5) - hash);
        }

        // ۸ تا رنگ خفن انتخاب کردیم (مثل دیسکورد و نوتین)
        const colors = [
            ['#23a6a6', '#198f8f'],  // فیروزه‌ای (پیش‌فرض)
            ['#e91e63', '#c2185b'],  // صورتی
            ['#9c27b0', '#7b1fa2'],  // بنفش
            ['#673ab7', '#512da8'],  // بنفش تیره
            ['#3f51b5', '#303f9f'],  // آبی ایندیگو
            ['#2196f3', '#1976d2'],  // آبی
            ['#00bcd4', '#0097a7'],  // سیان
            ['#ff9800', '#f57c00'],  // نارنجی
            ['#f44336', '#d32f2f'],  // قرمز
            ['#4caf50', '#388e3c'],  // سبز
        ];

        const colorPair = colors[Math.abs(hash % colors.length)];

        avatar.style.background = `linear-gradient(135deg, ${colorPair[0]}, ${colorPair[1]})`;
    }
});