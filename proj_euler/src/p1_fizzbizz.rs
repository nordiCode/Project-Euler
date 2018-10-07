fn main() {
   
   for i in 1..101{
       println!("{}",i);
       if div_3(i) && div_5(i){println!("Fizzbizz");}
       else if div_3(i){println!("Fizz");}
       else if div_5(i){println!("Bizz");}
       
   }
}

fn div_3(x:i32) -> bool{
    x%3 ==0
}
fn div_5(x:i32) -> bool{
    x%5==0
}
