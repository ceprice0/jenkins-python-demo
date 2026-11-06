from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Snake Game</title>

<style>
body{
    background:#111;
    color:white;
    font-family:Arial,sans-serif;
    text-align:center;
}

#score{
    font-size:24px;
    margin:10px;
}

canvas{
    background:black;
    border:3px solid lime;
}
</style>

</head>
<body>

<h1>🐍 Calum's Snake Game</h1>

<div id="score">Score: 0</div>

<canvas id="game" width="400" height="400"></canvas>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const box = 20;

let snake = [
    {x: 200, y: 200}
];

let score = 0;

let food = {
    x: Math.floor(Math.random()*20)*20,
    y: Math.floor(Math.random()*20)*20
};

let dx = 0;
let dy = 0;

document.addEventListener("keydown",(e)=>{

    if(e.key==="ArrowUp" && dy===0){
        dx=0;
        dy=-box;
    }

    if(e.key==="ArrowDown" && dy===0){
        dx=0;
        dy=box;
    }

    if(e.key==="ArrowLeft" && dx===0){
        dx=-box;
        dy=0;
    }

    if(e.key==="ArrowRight" && dx===0){
        dx=box;
        dy=0;
    }

});

function game(){

    if(dx===0 && dy===0){
        return;
    }

    ctx.clearRect(0,0,400,400);

    ctx.fillStyle="red";
    ctx.fillRect(food.x,food.y,box,box);

    ctx.fillStyle="lime";

    snake.forEach(part=>{
        ctx.fillRect(part.x,part.y,box,box);
    });

    const head = {
        x: snake[0].x + dx,
        y: snake[0].y + dy
    };

    if(
        head.x < 0 ||
        head.y < 0 ||
        head.x >= 400 ||
        head.y >= 400
    ){
        clearInterval(loop);
        alert("Game Over! Score: " + score);
        return;
    }

    for(let i=0;i<snake.length;i++){
        if(head.x===snake[i].x && head.y===snake[i].y){
            clearInterval(loop);
            alert("Game Over! Score: " + score);
            return;
        }
    }

    snake.unshift(head);

    if(head.x===food.x && head.y===food.y){

        score++;

        document.getElementById("score").innerHTML =
        "Score: " + score;

        food = {
            x: Math.floor(Math.random()*20)*20,
            y: Math.floor(Math.random()*20)*20
        };

    } else {
        snake.pop();
    }
}

const loop = setInterval(game,120);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
