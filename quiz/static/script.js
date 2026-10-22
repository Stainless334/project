// const timer = document.getElementById("timer");
// let timeLeft = 600;
// setInterval(function() {
//     const minutes = Math.floor(timeLeft/60);
//     const seconds = timeLeft%60;
//     timer.textContent = `Time Remaining: ${minutes}:${String(seconds).padStart(2, "0")}`;
//     timeLeft -= 1;
    
    
// }, 1000);

const timer = document.getElementById("timer");

const TIMER_DURATION = 600;

// Restore the remaining time, or start at 10 minutes.
let timeLeft = sessionStorage.getItem("timeLeft");

if (timeLeft === null) {
    timeLeft = TIMER_DURATION;
} else {
    timeLeft = Number(timeLeft);
}

const interval = setInterval(function() {
    if (timeLeft <= 0) {
        clearInterval(interval);
        sessionStorage.removeItem("timeLeft");
        timer.textContent = "00:00";

        // TODO: Handle quiz timeout here.
        return;
    }

    timeLeft--;

    sessionStorage.setItem("timeLeft", timeLeft);

    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;

    timer.textContent =
        `Time Remaining: ${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}, 1000);