xTiro = 200
yTiro = 400
xAlvo = -20
yAlvo = 40
vyTiro = 0
score = 0
def setup():
    size(400, 500);
def draw():
    global xTiro, yTiro, xAlvo, yAlvo, vyTiro, score; #serve para dizer que dentro do draw todas essas var serão utilizadas
    background(0)
    ellipse(xTiro, yTiro, 10, 10)
    ellipse(xAlvo, yAlvo, 20, 20)
    text(score, 300, 40)   #funcao para exibir texto
    xAlvo = xAlvo + 1
    if xAlvo > 401:
        xAlvo = -20
    yTiro = yTiro + vyTiro
    if yTiro < 0:
        yTiro = 400
        vyTiro = 0
    if dist(xTiro, yTiro, xAlvo ,yAlvo) < 15:
        score = score + 1
        xAlvo = -20
        
def keyPressed():
    global vyTiro
    vyTiro = - 5
