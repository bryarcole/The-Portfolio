<!DOctype HTML>
<html>
    <head>
        <link type='text/css' rel='stylesheet' href='main.css'/>
        <title>While loop Excersise from CodeAcedemy</title>

    </head>
    <body>
        <p>Make a coin flip we reach 5 tails in a row</p>
        <?php
        $tailsCount = 0;
        $flipCount = 0;
        while ($tailsCount < 5) {
            $flip = rand(0, 1);
            $flipCount ++;
            if ($flip){
                $tailsCount ++;
                echo "<div class=\"coin\">T</div>";
            }
            else {
                $tailsCount = 0;
                echo "<div class=\"coin\">H</div>";
            }
        }
        echo "<p> It took {$flipCount} flips</p>";
        ?>
        <div class="coin"></div>

    </body>
</html>
