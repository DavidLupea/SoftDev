//David Lupea
//Softdev1 pd2
//K05: ...and I want to Paint It Better
//2020-02-06

// e.preventDefault(); - Prevents an action from the way it is normally executed.

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
      ctx.fillRect(event.offsetX,event.offsetY,50,100); //Modifies the x and y coordinates where you draw on the canvas relative to the position of the mouse. Follows a coordinate system where +x is to the right but +y is down
    }
    else{
      ctx.beginPath(); //Starts creating a path on the canvas. Similar to pen down in netlogo
      ctx.arc(event.offsetX, event.offsetY, 5, 0, 2 * Math.PI);
      ctx.fill();
    }
};

var canvas = document.getElementById("slate");
canvas.addEventListener('click',draw);
