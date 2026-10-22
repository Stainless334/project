document.addEventListener("DOMContentLoaded", function () {
    const quizForm = document.getElementById("quiz-form");
    const loadingScreen = document.getElementById("loading-screen");

    if (quizForm && loadingScreen) {
        quizForm.addEventListener("submit", function () {
            loadingScreen.classList.add("active");
        });
    }
});

const durationRadios = document.querySelectorAll(
    'input[name="duration"]'
);

const customDuration = document.getElementById("custom-duration");

if (customDuration && durationRadios.length > 0) {

    customDuration.addEventListener("input", function () {
        if (this.value !== "") {
            durationRadios.forEach(function (radio) {
                radio.checked = false;
            });
        } else {
            document.querySelector(
                'input[name="duration"][value="5"]'
            ).checked = true;
        }
    });

    durationRadios.forEach(function (radio) {
        radio.addEventListener("change", function () {
            customDuration.value = "";
        });
    });
}