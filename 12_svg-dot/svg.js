var pic = document.getElementById("vimage");
pic.addEventListener('click', draw);
var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");

c.setAttribute("cx", 0);
c.setAttribute("cy", 0);
c.setAttribute("r", 100);
c.setAttribute("fill", "rect");
c.setAttribute("stroke", "black");


var prev = [-1,-1];

function draw(e) {
    x=e.clientX-8;
    y=e.clientY-8;
    console.log(x + ",", y);
    var dot = document.createElementNS("http://www.w3.org/2000/svg",'circle');
    dot.setAttribute("cx",x);
    dot.setAttribute("cy",y);
    dot.setAttribute("r",5);
    dot.setAttribute("fill","blue");
    pic.appendChild(dot);
    if(prev[0] != -1) {
        var line = document.createElementNS("http://www.w3.org/2000/svg",'line');
        line.setAttribute('x1', prev[0]);
        line.setAttribute('y1', prev[1]);
        line.setAttribute('x2',x);
        line.setAttribute('y2',y);
        line.setAttribute('stroke','black');
        pic.appendChild(line);
    }
    prev[0]=x;
    prev[1]=y;
}
