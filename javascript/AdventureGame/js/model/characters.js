//Create Objet or player 

var $button = "<div class='btn btn-default'>Click here to get things started!</div>"
var $continueButton = "<div class='btn btn-default continue'>Click here to get things started!</div>"

var character = function(name, age, des){
    this.name = name;
    this.age = age;
    this.des = des;
};



character.prototype.verify = function(){
    $("section").append("<p>","You're character name is ", this.name, "You're characters age is, ", this.age, "And finally youre characters class is ", this.des, "</p>");
};

// Characters with cards

character.prototype.hunter = function () {
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='https://danfasulo.files.wordpress.com/2014/09/destiny-goldengun.jpg'/></div></div>";
    this.classItem = "Cloak";
    this.cardCreate= function () {
        $("section").append($holderElem);
        $("section").append("<p>", "You're character name is ", this.name, "And youre characters class is ", this.des, "</p>")
        $(".card").append($continueButton)
    };
};

character.prototype.warlock = function () {
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='http://vignette1.wikia.nocookie.net/video151/images/a/aa/Destiny_Legendary_Warlock_vs._Ogre_-_Gamescom_2014/revision/latest?cb=20140816182310'/></div></div>";
    this.classItem = "Bond";
    this.cardCreate = function () {
        $("section").append($holderElem);
        $("section").append("<p>", "You're character name is ", this.name, "And youre characters class is ", this.des, "</p>")
        $(".card").append($continueButton)
    };
};

character.prototype.titan = function () {
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='http://static5.gamespot.com/uploads/screen_kubrick/1352/13527689/2653237-destiny_titan.jpg'/></div></div>";
    this.classItem = "Mark";
    this.cardCreate = function () {
        $("section").append($holderElem);
        $("section").append("<p>", "You're character name is ", this.name, "And youre characters class is ", this.des, "</p>")
        $(".card").append($continueButton)
    };
};


character.prototype.thorn = function() {
    this.damagePer = 22;
    this.accuracy = Math.floor((Math.random() * 10));
};

character.prototype.LastWord = function(){
    this.damagePer = 30;
    this.accuracy = Math.floor((Math.random() * 10));
}
