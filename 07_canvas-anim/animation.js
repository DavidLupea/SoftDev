//David Lupea
//SoftDev2 pd2
//K07 -- Canvas Animation
//2020-02-12

var animateButton = document.getElementById('animate');
var stopButton = document.getElementById('stop');
var canvas = document.getElementById('playground');
const ctx = canvas.getContext('2d');

var maxRad = 100;
var radius = 10;
var inc = true;

var animationID = 0;
var animationRunning = false;

var animate = function() {
    animationID = requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (inc) {
        radius++;
        if (radius > maxRad)
            inc = false;
    } else {
        radius--;
        if (radius < 1)
            inc = true;
    }

    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
}

animateButton.addEventListener("click", function(e) {
    if (!animationRunning) {
        animationRunning = true;
        requestAnimationFrame(animate);
    }
});

stopButton.addEventListener("click", function(e) {
    animationRunning = false;
    cancelAnimationFrame(animationID);
})
