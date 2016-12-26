function gameStart(){

    var characterName = $("#character-name").val();
    var characterClass = $("#character-class").val();
    var characterAge = $("#character-age").val();
    var player = new character(characterName, characterAge, characterClass);
    
    player.verify();

    if(characterClass == "Hunter"){
        player.hunter();
    }else if(characterClass == "Titan"){
        player.titan();
    }else if (characterClass == "Warlock"){
        player.warlock();
    };

    player.statement();
    console.log(player.classItem);
};
