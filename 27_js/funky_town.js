// fact(10)
var fact = function(n){
   if (n == 1){
      return 1;
   }
   return n*fact(n-1);
};

// fib(10)
var fib = function(n){
    if (n == 1){
        return 1;
    }
    if (n == 2){
        return 1;
    }
    return fib(n - 1) + fib(n - 2)
};

// gcd(100, 1000)
var gcd = function(a, b){
    if (a == 0){
        return b;
    }
    return gcd(b % a, a)
};

// Helper function that returns a random integer from 0 to n-1
var rand = function(n){
    return Math.floor(Math.random() * n)
};

// get_rand_entry(new Array("a", "b", "c", "d", "e"))
var get_rand_entry = function(arr){
    return arr[rand(arr.length)];
};
