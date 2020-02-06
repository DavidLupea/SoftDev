//Derek Leung and David Lupea
//Softdev1 pd2
//K04: I See a Red Door...
//2020-02-06

var rectMode = false

var clearScreen = function(e){
  var c = document.getElementById("slate");
  var ctx = c.getContext("2d");
  ctx.clearRect(0,0,c.width,c.height);
};

var button = document.getElementById('clear');
button.addEventListener('click',clearScreen);

var switchMode = function(e){
    if(rectMode == false){
        rectMode = true;
    }
    else{
        rectMode = false;
    }
};

var button1 = document.getElementById('switch');
button1.addEventListener('click',switchMode);

var draw = function(event){
    var c = document.getElementById("slate");
    var ctx = c.getContext("2d");
    if(rectMode == true){
      ctx.fillRect(event.clientX,event.clientY,50,100);
    }
    else{
      ctx.beginPath();
      ctx.arc(event.clientX, event.clientY, 5, 0, 2 * Math.PI);
      ctx.fill();
    }
};

var canvas = document.getElementById("slate");
canvas.addEventListener('click',draw);
