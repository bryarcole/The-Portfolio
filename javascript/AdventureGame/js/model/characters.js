//Create Objet or player 

var character = function(name, age, des){
    this.name = name;
    this.age = age;
    this.des = des;
};



character.prototype.verify = function(){
    $("section").append("<p>","You're character name is ", this.name, "You're characters age is, ", this.age, "And finally youre characters class is ", this.des, "</p>");
};

// Player class selection

character.prototype.hunter = function(){
    this.classItem = "Cloak";
    this.statement = function(){
        console.log("Now You're a hunter, now you have a", this.classItem, "and all the speed in the world");
    };

};

character.prototype.warlock = function(){
    this.classItem = "Bond";
    this.statement = function(){
        $(".input-result").text("Now you are a powrful warlock", this.classItem,"Don't go mad with power!")
    };
};

character.prototype.titan = function(){
    this.classItem = "Mark";
    this.statement = function(){
        $(".input-result").text("Feels great to be a Titan, with this Titan", this.classItem,"I am invincible")
    };
};

