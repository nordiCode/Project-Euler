fn factors(x:i64)->Vec<i64>{
    let mut limit = x/2 +1 ;
    let mut factors = Vec::new();

    for y in 1..limit{
        if x%y==0{factors.push(y);}
    }
    factors.push(x);
    factors
}
fn num_factors(x:i64)->i64{
    let mut limit = x as f64 ;
    limit = limit.sqrt().ceil();
    let upper = limit as i64;
//    println!("Limit {}",limit);
    let mut sum = 0;
    if upper * upper ==x{sum +=1;}
    for y in 1..upper{
        if x%y==0{sum +=2;}
    }

    sum

}

fn main(){
    let mut number = 1.0;
    let mut divisors = 1;
    let mut current =1 ;
    let mut tri_num = 1.0;
    while divisors < 500{
        tri_num = number*(number+1.0)*(0.5);
        let mut tri = tri_num as i64;
        divisors = num_factors(tri);
        current = tri;
        number +=1.0;
    }
    println!("the number {}", current);
}
