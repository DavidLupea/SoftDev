//factorial function
var fact = function(n) {
  if (n > 1){
    return n * fact(n-1);
  }
    return 1;
}

//fibonocci function
var fib = function(n) {
  if (n == 0) {
    return 0;
  }
  if (n > 2) {
    return fib(n-1) + fib(n-2);
  }
  return 1;
}

// gcd(a,b) returns the greatest common divisor of the input numbers a and b
var gcd = function(a,b) {
  if (a == 0) {
    return b;
  }
  return gcd(b % a, a)
}

// array of students in SoftDev period 2
var studentsInPeriod2 = ["abedinM", "avrahamiB", "bhuiyanS", "caoW", "chanM", "chenE", "chenJ", "friedH",
"huangP", "huangT", "linD", "linW", "lupeaD", "mosesB", "niA", "olinJ", "olteanuA",
"rahmanM", "sontagC", "thompsonA", "wangD", "wuJ", "yusufovJ", "zenH"];

// randomStudent() returns a random student from the array studentsInPeriod2
var randomStudent = function() {
  randomNumber = Math.floor(Math.random() * studentsInPeriod2.length)
  return studentsInPeriod2[randomNumber]
}
//-----------------------------------------------------------------------------
//PRINTING fact(5)
var test1 = document.getElementById("a");
function firstCons1() {
  console.log(fact(5));
}
function firstPage1() {
  document.write(fact(5));
}
test1.addEventListener("click", firstCons1);
test1.addEventListener("click", firstPage1);

//PRINTING fib(5)
var test2 = document.getElementById("b");
function firstCons2() {
  console.log(fib(5));
}
function firstPage2() {
  document.write(fib(5));
}
test2.addEventListener("click", firstCons2);
test2.addEventListener("click", firstPage2);

//PRINTING gcd(10,15)
var test3 = document.getElementById("c");
function firstCons3() {
  console.log(gcd(10,15));
}
function firstPage3() {
  document.write(gcd(10,15));
}
test3.addEventListener("click", firstCons3);
test3.addEventListener("click", firstPage3);

//PRINTING randomStudent()
var test4 = document.getElementById("d");
var ans = randomStudent();
function firstCons4() {
  console.log(ans);
}
function firstPage4() {
  document.write(ans);
}
test4.addEventListener("click", firstCons4);
test4.addEventListener("click", firstPage4);
