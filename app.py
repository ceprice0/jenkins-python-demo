from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Calum's Snake Game</title>

<style>

body{
    margin:0;
    background:#0e0e0e;
    font-family:Arial,sans-serif;
    text-align:center;
    color:white;
}

h1{
    color:#00ff88;
    text-shadow:0 0 15px #00ff88;
}

#score{
    font-size:24px;
    margin:10px;
}

button{
    background:#00ff88;
    border:none;
    padding:12px 24px;
    font-size:18px;
    border-radius:8px;
    cursor:pointer;
}

canvas{
    background:#000;
    border:4px solid #00ff88;
    box-shadow:0 0 20px #00ff88;
}

</style>
</head>

<body>

<h1>🐍 Calum's Snake Game</h1>

<div id="score">Score: 0</div>

<button onclick="startGame()">Start Game</button>

<br><br>

<canvas id="game" width="500" height="500"></canvas>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const box = 20;

let snake;
let food;
let dx;
let dy;
let score;
let gameLoop;

function resetGame(){

    snake = [{x:240,y:240}];

    food = {
        x:Math.floor(Math.random()*25)*20,
        y:Math.floor(Math.random()*25)*20
    };

    dx = 20;
    dy = 0;

    score = 0;

    document.getElementById("score").innerHTML =
    "Score: 0";
}

function startGame(){

    clearInterval(gameLoop);

    resetGame();

    gameLoop = setInterval(draw,120);
}

document.addEventListener("keydown",(e)=>{

    if(e.key==="ArrowUp" && dy===0){
        dx=0;
        dy=-20;
    }

    if(e.key==="ArrowDown" && dy===0){
        dx=0;
        dy=20;
    }

    if(e.key==="ArrowLeft" && dx===0){
        dx=-20;
        dy=0;
    }

    if(e.key==="ArrowRight" && dx===0){
        dx=20;
        dy=0;
    }

});

function draw(){

    ctx.clearRect(0,0,500,500);

    ctx.fillStyle="red";
    ctx.fillRect(food.x,food.y,box,box);

    snake.forEach((part,index)=>{

        if(index===0){
            ctx.fillStyle="#00ff88";
        }else{
            ctx.fillStyle="lime";
        }

        ctx.fillRect(part.x,part.y,box,box);

    });

    let head = {
        x:snake[0].x + dx,
        y:snake[0].y + dy
    };

    if(
        head.x < 0 ||
        head.y < 0 ||
        head.x >= 500 ||
        head.y >= 500
    ){
        clearInterval(gameLoop);
        alert("Game Over! Score: "+score);
        return;
    }

    for(let i=1;i<snake.length;i++){

        if(
            head.x===snake[i].x &&
            head.y===snake[i].y
        ){
            clearInterval(gameLoop);
            alert("Game Over! Score: "+score);
            return;
        }
    }

    snake.unshift(head);

    if(
        head.x===food.x &&
        head.y===food.y
    ){

        score++;

        document.getElementById("score").innerHTML =
        "Score: " + score;

        food = {
            x:Math.floor(Math.random()*25)*20,
            y:Math.floor(Math.random()*25)*20
        };

    } else {

        snake.pop();

    }

}

resetGame();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
