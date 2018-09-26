// use std::cmp::Ordering;



fn main() {

    let mut sum = 0;

    for x in 1..1000{
        if x %3==0 || x % 5 == 0{
            sum = sum + x ;
        }
    }
    println!("Total sum of integers divisible by 5 and 3 is: {}", sum);

}
