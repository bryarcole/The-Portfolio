function gameStart(){
    var characterName = prompt("What is your name?");
    var characterClass = prompt("what Class would you like to use? Hunter, Warlock or Titan?");
    var characterAge = prompt("And how old are you?");

    var player = new character(characterName, characterAge, characterClass);
    
    player.verify();

    switch(characterClass){
        case "Titan":
        player.titan();
        player.statement();
        break;
        
        case "Hunter":
        player.hunter();
        player.statement();
        break;

        case "Warlock":
        player.warlock();
        player.statement();
        break;
    };

    return player;

};

function mainGame(player){
    
} 

