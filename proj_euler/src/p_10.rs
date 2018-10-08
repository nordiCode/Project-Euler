fn sum_primes(x:i64)->i64{
    let mut sum:i64 = 0;

    for i in 2..x{
        if is_prime(i){
            sum = sum + i;
        }
    }
    sum
}
fn is_prime(x: i64)->bool{
    let z = x as f64;
    let z = z.sqrt();
    let mut abs_upper = z as i64;
    abs_upper = abs_upper + 1;
//    println!("Upper limit {}",abs_upper);

    for y in 2..abs_upper{
        if x %y ==0{
            return false;
        }
    }
    return true;
}
fn main(){
  let  sum = sum_primes(2000001);
  println!("{}",sum);
}
