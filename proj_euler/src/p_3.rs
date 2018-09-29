// By considering the terms in the Fibonacci sequence
//  whose values do not exceed
//  four million, find the sum of the even-valued terms.


fn main(){
//    let mut i = 4000000;
    let mut x_1  = 1;
    let mut x_2  = 1;
    let mut x_3 = 0;
    let mut sum = 0;

//    println!("Fib series 1 {}", 1);

    loop{
        x_3 = x_2 + x_1;
        x_1 = x_2;
        x_2 = x_3;

//        println!("Fib series {} ", x_2);
        if x_3 % 2 == 0 {
//            println!("It's even! {}", x_3);
        sum = sum + x_3;
        }
        if x_3 > 4000000{
            break;
        }


    }
    println!("here's your sum {} ", sum);

}
