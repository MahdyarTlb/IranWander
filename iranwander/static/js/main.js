document.addEventListener("DOMContentLoaded", function () {

    const allCities = ["Tehran", "Isfahan", "Shiraz", "Mashhad", "Karaj"];

    const randomBtn = document.getElementById("random-trip-btn");
    const popup = document.getElementById("random-popup");
    const destinationText = document.getElementById("random-destination");
    const goLink = document.getElementById("go-to-city");
    const closePopupBtn = document.getElementById("close-popup");

    if (randomBtn && popup && destinationText && goLink) {
        randomBtn.addEventListener("click", () => {
            const randomCity = allCities[Math.floor(Math.random() * allCities.length)];
            destinationText.textContent = randomCity;
            goLink.href = `/city?q=${encodeURIComponent(randomCity)}`;
            popup.classList.add("active");
        });

        closePopupBtn?.addEventListener("click", () => {
            popup.classList.remove("active");
        });

        popup.addEventListener("click", (e) => {
            if (e.target === popup) popup.classList.remove("active");
        });
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && popup.classList.contains("active")) {
                popup.classList.remove("active");
            }
        });
    }

    const popularCities = ["Tehran", "Isfahan", "Shiraz", "Mashhad", "Karaj", "Yazd", "Tabriz"];
    const searchInput = document.getElementById("heroSearch");
    const suggestionsBox = document.getElementById("suggestions");
    const searchBtn = document.querySelector(".search-btn");

    if (searchInput && suggestionsBox) {
        searchInput.addEventListener("input", function () {
            const query = this.value.trim().toLowerCase();
            if (!query) {
                suggestionsBox.classList.remove("active");
                suggestionsBox.innerHTML = "";
                return;
            }

            const matches = popularCities.filter(city =>
                city.toLowerCase().includes(query)
            ).slice(0, 6);

            if (matches.length > 0) {
                suggestionsBox.innerHTML = matches.map(city => `
                    <div class="suggestion-item" data-city="${city}">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <circle cx="11" cy="11" r="8"/>
                            <path d="m21 21-4.35-4.35"/>
                        </svg>
                        <span>city <strong>${city}</strong></span>
                    </div>
                `).join("");
                suggestionsBox.classList.add("active");
            } else {
                suggestionsBox.classList.remove("active");
            }
        });

        suggestionsBox.addEventListener("click", (e) => {
            const item = e.target.closest(".suggestion-item");
            if (item) {
                window.location.href = `/city?q=${encodeURIComponent(item.dataset.city)}`;
            }
        });

        const performSearch = () => {
            const query = searchInput.value.trim();
            if (query) window.location.href = `/city?q=${encodeURIComponent(query)}`;
        };

        searchBtn?.addEventListener("click", (e) => { e.preventDefault(); performSearch(); });
        searchInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") { e.preventDefault(); performSearch(); }
        });

        document.addEventListener("click", (e) => {
            if (!e.target.closest(".search-container")) {
                suggestionsBox.classList.remove("active");
            }
        });
    }

    window.onload = function() {
    const avatarBtn = document.getElementById("avatarBtn");
    const userMenu = document.querySelector(".user-menu");
    const dropdown = document.getElementById("dropdownMenu");

    console.log("avatarBtn:", avatarBtn); 

    if (!avatarBtn) {
        console.error("avatarBtn NOT FOUND!");
        return;
    }

    let isOpen = false;

    avatarBtn.onclick = function(e) {
        e.stopPropagation();
        isOpen = !isOpen;

        if (isOpen) userMenu.classList.add("active");
        else userMenu.classList.remove("active");
    };

    document.onclick = function(e) {
        if (
            isOpen &&
            !avatarBtn.contains(e.target) &&
            !dropdown.contains(e.target)
        ) {
            userMenu.classList.remove("active");
            isOpen = false;
        }
    };
};

    const avatar = document.querySelector(".avatar-placeholder[data-username]");
    if (avatar) {
        const username = avatar.getAttribute("data-username") || "A";
        let hash = 0;
        for (let i = 0; i < username.length; i++) {
            hash = username.charCodeAt(i) + ((hash << 5) - hash);
        }

        const colors = [
            ["#23a6a6", "#198f8f"],
            ["#e91e63", "#c2185b"],
            ["#9c27b0", "#7b1fa2"],
            ["#673ab7", "#512da8"],
            ["#3f51b5", "#303f9f"],
            ["#2196f3", "#1976d2"],
            ["#00bcd4", "#0097a7"],
            ["#ff9800", "#f57c00"],
            ["#f44336", "#d32f2f"],
            ["#4caf50", "#388e3c"],
        ];

        const colorPair = colors[Math.abs(hash % colors.length)];
        avatar.style.background = `linear-gradient(135deg, ${colorPair[0]}, ${colorPair[1]})`;
    }
});

    document.getElementById("newsletterForm")?.addEventListener("submit", async function(e) {
    e.preventDefault();

    const email = document.getElementById("emailInput").value.trim();
    const messageEl = document.getElementById("formMessage");

    if (!email || !email.includes("@")) {
        messageEl.innerHTML = "email isn't correct!";
        messageEl.className = "form-message error";
        return;
    }

    messageEl.innerHTML = "sending...";
    messageEl.className = "form-message loading";

    try {
        const response = await fetch("/api/subscribe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email })
        });

        const data = await response.json();

        if (data.success) {
            messageEl.innerHTML = "That sound great, now we have your mail:))";
            messageEl.className = "form-message success";
            document.getElementById("emailInput").value = "";
        } else {
            messageEl.innerHTML = data.error || "we have a problem";
            messageEl.className = "form-message error";
        }
    } catch (err) {
        messageEl.innerHTML = "api error";
        messageEl.className = "form-message error";
    }
});

const mobileToggle = document.getElementById("mobileMenuToggle");
const overlay = document.getElementById("mobileNavOverlay");
const mobileMenu = document.querySelector('.mobile-menu');

mobileToggle.addEventListener("click", () => {
  mobileToggle.classList.toggle("active");
  overlay.classList.toggle("active");
  mobileMenu.classList.toggle("active");
});

overlay.addEventListener("click", (e) => {
  if (e.target === overlay) {
    mobileToggle.classList.remove("active");
    overlay.classList.remove("active");
  }
});
