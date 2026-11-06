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
    text-align:center;
    font-family:Arial,sans-serif;
}

canvas{
    background:black;
    border:3px solid #00ff00;
}
</style>
</head>
<body>

<h1>Calum's Snake Game</h1>
<p>Use Arrow Keys To Start</p>

<canvas id="game" width="400" height="400"></canvas>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let snake=[{x:200,y:200}];

let dx=0;
let dy=0;

let score=0;

let food={
 x:Math.floor(Math.random()*20)*20,
 y:Math.floor(Math.random()*20)*20
};

document.addEventListener('keydown',(e)=>{

 if(e.key==='ArrowUp' && dy===0){
   dx=0;
   dy=-20;
 }

 if(e.key==='ArrowDown' && dy===0){
   dx=0;
   dy=20;
 }

 if(e.key==='ArrowLeft' && dx===0){
   dx=-20;
   dy=0;
 }

 if(e.key==='ArrowRight' && dx===0){
   dx=20;
   dy=0;
 }
});

function draw(){

 ctx.clearRect(0,0,400,400);

 ctx.fillStyle='lime';

 snake.forEach(part=>{
   ctx.fillRect(part.x,part.y,20,20);
 });

 ctx.fillStyle='red';
 ctx.fillRect(food.x,food.y,20,20);

 if(dx===0 && dy===0){
   return;
 }

 const head={
   x:snake[0].x+dx,
   y:snake[0].y+dy
 };

 if(
   head.x<0 ||
   head.y<0 ||
   head.x>=400 ||
   head.y>=400
 ){
   clearInterval(gameLoop);
   alert('Game Over! Score: '+score);
   return;
 }

 snake.unshift(head);

 if(head.x===food.x && head.y===food.y){

   score++;

   food={
      x:Math.floor(Math.random()*20)*20,
      y:Math.floor(Math.random()*20)*20
   };

 }else{
   snake.pop();
 }

}

const gameLoop=setInterval(draw,120);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
