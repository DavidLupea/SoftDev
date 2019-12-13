var func = function(n){
  return n * 2;
}

var fib = function(n){
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
}

var gcd = function(a,b){
  if (b > a) {
    return gcd(b,a);
  }
  var num,i;
  for (i = 1; i < a; i++){
    if (a % i == 0 && b % i == 0){
      num = i;
    }
  }
  return num;
}

var students = ["coby","joseph","alex","tyler"]

var randomStudent = function(){
  var len = students.length;
  if (len > 1) len -= 1;
  //console.log(Math.round(Math.random() * len));
  return students[Math.round(Math.random() * len)];
}

var changeHeading = function(e){
  var h = document.getElementById("h");
  h.innerHTML = e;
}

var removeItem = function(e){
  e.remove();
}

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++){
  //console.log(lis[i].innerHTML);
  //console.log(lis[i]);
  lis[i].addEventListener('click', function(e){removeItem(this), console.log(e);});
  lis[i].addEventListener('mouseover', function(){changeHeading(this.innerHTML)});
  lis[i].addEventListener('mouseout', function(){changeHeading("Hello World!")});
}

var addItem = function() {
  var list = document.getElementById("thelist");
  var ele = document.createElement("li");
  ele.innerHTML = "WORD";
  list.append(ele);
  ele.addEventListener('click', function(e){removeItem(this), console.log(e);});
  ele.addEventListener('mouseover', function(){changeHeading(this.innerHTML)});
  ele.addEventListener('mouseout', function(){changeHeading("Hello World!")});
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var addFib = function(){
  var list = document.getElementById("fiblist");
  var len = list.getElementsByTagName("li").length;
  //console.log(len);
  var ele = document.createElement("li");
  ele.innerHTML = fib(len);
  //console.log(num);
  list.append(ele);
}

//var fb = document.getElementById("fb");
//fb.addEventListener('click', addFib);

var fibNums = [];

var addFibNoLag = function() {
  var list = document.getElementById("fiblist");
  //console.log(fibNums.length);
  //console.log(list);
  //console.log(list.getElementsByTagName("li"));
  //console.log(numsArr);
  //console.log(len);
  var ele = document.createElement("li");
  if (fibNums.length > 2){
    //console.log(numsArr);
    ele.innerHTML = fibNums[fibNums.length - 1] + fibNums[fibNums.length - 2];
    fibNums.push(fibNums[fibNums.length - 1] + fibNums[fibNums.length - 2]);
  }
  else {
    ele.innerHTML = fib(fibNums.length);
    fibNums.push(fib(fibNums.length));
  }
  //console.log(num);
  list.append(ele);
}

var fb = document.getElementById("fb");
fb.addEventListener('click', addFibNoLag);
