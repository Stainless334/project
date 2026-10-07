const timer = document.getElementById("timer");
let timeLeft = 600;
setInterval(function() {
    const minutes = Math.floor(timeLeft/60);
    const seconds = timeLeft%60;
    timer.textContent = `Time Remaining: ${minutes}:${String(seconds).padStart(2, "0")}`;
    timeLeft -= 1;
    
    
}, 1000);
