
var button = document.getElementById('clear');
var pic = document.getElementById('vimage');

var plot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    if(e.target.getAttribute("id") == "vimage"){
  	     c.setAttribute("cx", e.clientX-8);
         c.setAttribute("cy", e.clientY-8);
         c.setAttribute("r", 20);
  	     c.setAttribute("fill", "blue");
		     c.addEventListener("click", doot)
  	     pic.appendChild(c);
    }
};

var doot = function(e){
    clickedDot=true;
    console.log(this.getAttribute("id"));
    if(this.getAttribute('fill') == 'blue'){
        this.setAttribute('fill','cyan');
    }
    else if(this.getAttribute('fill') == 'cyan'){
        moveRandom(e);
        this.remove();
    }
};

var moveRandom = function(e){
    x=Math.floor((Math.random() * 500));
    y=Math.floor((Math.random() * 500));
    var dot = document.createElementNS("http://www.w3.org/2000/svg",'circle');
    dot.setAttribute("cx",x);
    dot.setAttribute("cy",y);
    dot.setAttribute("r",20);
    dot.setAttribute("fill","blue");
    pic.appendChild(dot);
    dot.addEventListener('click',doot);
};

var clear = function(e) {
    while (pic.lastChild) {
        pic.removeChild(pic.lastChild);
    }
};

button.addEventListener("click", clear);
pic.addEventListener("click", plot)
