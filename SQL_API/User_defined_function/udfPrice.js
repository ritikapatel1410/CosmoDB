function userDefinedFunction(price){
    if(price == undefined)
        throw "no input";

    if (price < 100)
        return price * 0.1;
    else if (price < 200)
        return price * 0.2;
    else 
        return price * 0.4;            

}