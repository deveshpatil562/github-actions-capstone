const canvas = document.getElementById("bg")
const ctx = canvas.getContext("2d")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

let particles = []

for(let i=0;i<80;i++){
particles.push({
x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
size:2
})
}

function animate(){

ctx.clearRect(0,0,canvas.width,canvas.height)

particles.forEach(p=>{
ctx.fillStyle="#2563eb"
ctx.beginPath()
ctx.arc(p.x,p.y,p.size,0,Math.PI*2)
ctx.fill()
p.y+=0.5
if(p.y>canvas.height)p.y=0
})

requestAnimationFrame(animate)
}

animate()