
fn sum_squares(x:i64)-> i64{
      let y = x + 1;
      let mut sum = 0;
      for i in 1..y{
          sum = sum + (i*i);
      }
      sum
  }

fn nat_squared(x:f64)-> i64{
    let mut sum: f64 = x * (x+1.0)*(0.5);
    sum = sum * sum;
    sum as i64
}

fn main(){
    let z = sum_squares(100);
    let t = nat_squared(100.0);
    let difference = t - z;
    println!("Sum of squares {} {} {}",t, z, difference);
}
