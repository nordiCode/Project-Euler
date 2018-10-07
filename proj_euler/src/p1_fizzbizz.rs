fn main() {
   
   for i in 1..101{
      let mut answer =
       if div_3(i) && div_5(i){"FizzBizz"}
       else if div_3(i){"Fizz"}
       else if div_5(i){"Bizz"}
       else {""};
       println!("{} {}",i,answer);
       
   }
}

fn div_3(x:i32) -> bool{
    x%3 ==0
}
fn div_5(x:i32) -> bool{
    x%5==0
}
