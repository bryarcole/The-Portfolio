//Create Objet or player 


//Buttons
var $button = "<div class='btn btn-default'>Click here to get things started!</div>";
var $continueButton = "<div class='btn btn-default continue'>Click here to get things started!</div>";
var $fightButton = "<div class='btn btn-default fight'>Click here to start the show!</div>";

var p = $("<p></p>");

var character = function(name, des){
    this.health = 20;
    this.name = name;
    this.des = des;
};



//Testing to make sure object works
character.prototype.verify = function(){
    $("section").append("<p> You're character name is ", this.name, "You're characters age is, ", this.age, "And finally youre characters class is ", this.des, "</p>");
};

// Characters with cards

character.prototype.hunter = function () {
    this.agility = 9;
    this.recovery = 2;
    this.armour = 6;
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='https://danfasulo.files.wordpress.com/2014/09/destiny-goldengun.jpg'/></div></div>";
    this.classItem = "Cloak";
    this.cardCreate= function () {
        $("section").append($holderElem);
        $("section").append($continueButton)
    };
};

character.prototype.warlock = function () {
    this.health = 5;
    this.agility = 4;
    this.recovery = 8;
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='http://vignette1.wikia.nocookie.net/video151/images/a/aa/Destiny_Legendary_Warlock_vs._Ogre_-_Gamescom_2014/revision/latest?cb=20140816182310'/></div></div>";
    this.classItem = "Bond";
    this.cardCreate = function () {
        $("section").append($holderElem);
        $("section").text
    };
};

character.prototype.titan = function () {
    this.health = 8;
    this.agility = 2;
    this.recovery = 5;
    var $holderElem = "<div class='card character-card'><div class='card-block'><img class='card-img' src='http://static5.gamespot.com/uploads/screen_kubrick/1352/13527689/2653237-destiny_titan.jpg'/></div></div>";
    this.classItem = "Mark";
    this.cardCreate = function () {
        $("section").append($holderElem);
        $("section").append("<p>", "You're character name is ", this.name, "And youre characters class is ", this.des, "</p>")
        $(".card").append($continueButton)
    };
};

//Weapons choice //
character.prototype.thorn = function() {
    this.weaponName = "Thorn";
    this.damagePer = 6.6;
    this.accuracy = Math.floor((Math.random() * 85));
};

character.prototype.lastWord = function(){
    this.weaponName = "The Last Word";
    this.damagePer = 9.4;
    this.accuracy = Math.floor((Math.random() * 70));
};



// bosses //

var Golgoroth = function(){
    this.attack = 8;
    this.health = 28;
};

var Variks = function(){
    this.attack = 11;
    this.health = 22;

};

