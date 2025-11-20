const cityData = {
    "Tehran": {
        attractions: [
            { title: "Milad Tower", img: "../img/miladmodal.jpg", link: "miladtower.html" },
            { title: "Golestan Palace", img: "../img/golestanmodal.jpg", link: "golestanpalace.html" }
        ]
    },
    "Isfahan": {
        attractions: [
            { title: "Naqsh-e Jahan Square", img: "../img/naqshemodal.jpg", link: "naghshejahan.html" },
            { title: "Si-o-se-pol Bridge", img: "../img/Si-o-se-polmodal.jpg", link: "siosepol.html" }
        ]
    },
    "Shiraz": {
        attractions: [
            { title: "Hafez Mausoleum", img: "../img/hafezmodal.jpg", link: "hafeztomb.html" },
            { title: "Persepolis", img: "../img/jamshidmodal.jpg", link: "jamshid.html" }
        ]
    },
    "Karaj": {
        attractions: [
            { title: "Chamran Park", img: "../img/chamranmodal.jpg", link: "chamran.html" },
            { title: "Little Iran Park", img: "../img/littleiranmodal.jpg", link: "littleiranpark.html" }
        ]
    },
    "Mashhad": {
        attractions: [
            { title: "Imam Reza Shrine", img: "../img/emammodal.jpg", link: "emamreza.html" },
            { title: "Ferdosi Mausoleum", img: "../img/ferdosimodal.jpg", link: "ferdositomb.html" }
        ]
    }
};

const buttons = document.querySelectorAll(".btn");
const overlay = document.getElementById("overlay");
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modal-content");

buttons.forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();

        const cityName = btn.parentElement.querySelector("h3").textContent.trim();
        const cityInfo = cityData[cityName];

        if (!cityInfo) return;

        modalContent.innerHTML = cityInfo.attractions.map(a => `
            <div class="attraction-card">
                <img src="${a.img}">
                <h4>${a.title}</h4>
                <a class="more-btn" href="${a.link}">More Info</a>
            </div>
        `).join('');

        overlay.classList.remove("hidden");
        modal.classList.remove("hidden");
    });
});

overlay.addEventListener("click", () => {
    overlay.classList.add("hidden");
    modal.classList.add("hidden");
});
