function Cat(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    }
}
Cat.call({}, 1);
Cat.apply({}, [1, 2, 3]);
const another = new cat(1);