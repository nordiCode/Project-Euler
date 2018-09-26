// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?
// use std::num;
use std::f64;

fn main(){
    largest_prime_factor(600851475143 );
}

fn largest_prime_factor(x: i64){
    let z = x as f64;
    let z = z.sqrt();
    let mut upper_limit = z as i64;
    upper_limit = upper_limit + 1;
    let mut factor = 0;
    for y in 1..upper_limit{
        if x % y == 0{
            println!("Factor {}", y);
            if is_prime(y)==true{
            factor = y;}
        }

    }
    println!("Largest prime factor {}", factor);

}

fn is_prime(x: i64)->bool{
    let z = x as f64;
    let z = z.sqrt();
    let mut abs_upper = z as i64;
    abs_upper = abs_upper + 1;
    println!("Upper limit {}",abs_upper);

    for y in 2..abs_upper{
        if x %y ==0{
            return false;
        }
    }
    return true;
}
