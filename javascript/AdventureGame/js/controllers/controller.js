function newGame(){

    var characterName = $("#character-name").val();
    var characterClass = $("#character-class").val();
    var characterAge = $("#character-age").val();
    var player = new character(characterName, characterAge, characterClass);
    
    if(characterClass == "Hunter"){
        player.hunter();
    }else if(characterClass == "Titan"){
        player.titan();
    }else if (characterClass == "Warlock"){
        player.warlock();
    };
    player.cardCreate();
    $("form").hide();
    function oldManMeet (){
        alert("You meet an old man on your journy...");
        alert("Pick a weapon!");
        var weaponSelection = prompt("Pick your weapon now");
        if(weaponSelection == "Thorn"){
            player.thorn();
        }else if(weaponSelection == "Last Word"){
            player.LastWord();
        }
    }
    $(".continue").click(function(){
        oldManMeet();
    });
};

