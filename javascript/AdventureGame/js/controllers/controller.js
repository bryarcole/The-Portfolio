function newGame(){
    //Prompt for Class and name
    var characterName = $("#character-name").val();
    var characterClass = $("#character-class").val();
    var Player = new character(characterName, characterClass);
    
    // Get class selection
    if(characterClass == "Hunter"){
        Player.hunter();
    }else if(characterClass == "Titan"){
        Player.titan();
    }else if (characterClass == "Warlock"){
        Player.warlock();
    };
    //Show Class selection - Hide form
    Player.cardCreate();
    $("form").hide();

    //Phase one, add Damage per to character
    function oldManMeet (){
        console.log("You meet an old man on your journy...");
        var weaponSelection = prompt("Pick your weapon now");
        
        if(weaponSelection == "Last Word"){
            Player.lastWord();
        }else if(weaponSelection == "Thorn"){
            Player.thorn();
        };
        $(".card-block").append("<p> You have selected ", Player.weaponName ," don't go madd with power! </p>");


    };
    $(".continue").click(function(){
        oldManMeet();
        console.log(Player.weaponName + Player.damagePer);
    });

    //Encounter first Boss
    function firstBoss(){
        $(".character-card").hide();
        var fighting = true;
        var hitRate = Math.floor(Math.random(Player.accuracy) *100);
        var damage = Player.damagePer;
        var totalDamage = 0;
        var bossDamage = 0;
        var playerHealth = Player.health + Player.armour + (Player.agility / 2);
        var Golg = new Golgoroth();

        while(fighting){
            if(hitRate > 30){ //Decrease to make easier, Increase to make more difficult
                console.log("You got a hit on him!");
                totalDamage += damage;
                if(totalDamage > Golg.health){
                    console.log("Nice you killed Golgoroth!");
                    fighting = false;
                }else{
                    hitRate = Math.floor(Math.random(hitRate) *100);
                    console.log(hitRate);
                };
            }else{
                console.log("You missed, Golg attacks!");
                bossDamage += Golg.attack;
                if(bossDamage > playerHealth){
                    console.log("Oh no Golg killed you!");
                    console.log(totalDamage);
                    fighting = false;
                }else{
                    hitRate = Math.floor(Math.random(hitRate) *100);
                };
            };
        }
    };
    $("section").append($fightButton);

    $(".fight").click(function(){
        firstBoss();
    })
    

    

};

/*

------- Boss fight engine ----------
        while(fighting){
            if(hitRate > 30){
                console.log("You got a hit on him!");
                totalDamage += damage;
                if(totalDamage > badguy.health){
                    console.log("Nice you killed BadGuy!");
                    fighting = false;
                }else{
                    hitRate = Math.floor(Math.random(hitRate) *100);
                    console.log(hitRate);
                };
            }else{
                console.log("You missed, Badguy attacks!");
                bossDamage += Badguy.attack;
                if(bossDamage > playerHealth){
                    console.log("Oh no Badguy killed you!");
                    console.log(totalDamage);
                    fighting = false;
                }else{
                    hitRate = Math.floor(Math.random(hitRate) *100);
                };
            };
        }
*/


