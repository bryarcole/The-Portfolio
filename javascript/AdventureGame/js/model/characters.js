var character = function(name, age, des){
    this.name = name;
    this.age = age;
    this.des = des;
};



character.prototype.verify = function(){
    console.log("You're character name is ", this.name, "You're characters age is, ", this.age, "/nAnd finally youre characters class is ", this.des);
};

character.prototype.hunter = function(){
    this.classItem = "Cloak";
    this.statement = function(){
        $("h1").text("Now You're a hunter, now you have a", this.classItem, "");
    };
};

character.prototype.warlock = function(){
    this.classItem = "Bond";
    this.statement = function(){
        console.log("Feels great to be a Titan, with this Titan", this.classItem,"I am invincible")
    };
};

character.prototype.titan = function(){
    this.classItem = "Mark";
    this.statement = function(){
        console.log("Feels great to be a Titan, with this Titan", this.classItem,"I am invincible")
    };
};