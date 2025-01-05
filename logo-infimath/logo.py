from manim import *
#este logo es fondo negro, lineas blancas y sin relleno
class Triangles(Scene):
    def construct(self):
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.89, 0])
        t1p3 = np.array([0.03, 1.15, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.05, 1.13, 0])
        t3p2 = np.array([-0.075, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.522, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.558, 0])
        t9p2 = np.array([0.813, -0.484, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color=WHITE)
        tri2 = Polygon(t2p1, t2p2, t2p3, color=WHITE)
        tri3 = Polygon(t3p1, t3p2, t3p3, color=WHITE)
        tri4 = Polygon(t4p1, t4p2, t4p3, color=WHITE)
        tri5 = Polygon(t5p1, t5p2, t5p3, color=WHITE)
        tri6 = Polygon(t6p1, t6p2, t6p3, color=WHITE)
        tri7 = Polygon(t7p1, t7p2, t7p3, color=WHITE)
        tri8 = Polygon(t8p1, t8p2, t8p3, color=WHITE)
        tri9 = Polygon(t9p1, t9p2, t9p3, color=WHITE)
        tri10 = Polygon(t10p1, t10p2, t10p3, color=WHITE)
        #tri.set_fill(opacity=0.5)
        
        # Añadir el triángulo a la escena
        self.play(Create(tri1), Create(tri2), Create(tri3), Create(tri4), Create(tri5), Create(tri6), Create(tri7), Create(tri8), Create(tri9), Create(tri10))

        # Mostrar la escena
        self.wait()

#este logo es fondo blanco y lineas y relleno con azul de infimath    
class logo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.89, 0])
        t1p3 = np.array([0.03, 1.15, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.05, 1.13, 0])
        t3p2 = np.array([-0.075, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.522, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.558, 0])
        t9p2 = np.array([0.813, -0.484, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color="#165CFF")
        tri2 = Polygon(t2p1, t2p2, t2p3, color="#165CFF")
        tri3 = Polygon(t3p1, t3p2, t3p3, color="#165CFF")
        tri4 = Polygon(t4p1, t4p2, t4p3, color="#165CFF")
        tri5 = Polygon(t5p1, t5p2, t5p3, color="#165CFF")
        tri6 = Polygon(t6p1, t6p2, t6p3, color="#165CFF")
        tri7 = Polygon(t7p1, t7p2, t7p3, color="#165CFF")
        tri8 = Polygon(t8p1, t8p2, t8p3, color="#165CFF")
        tri9 = Polygon(t9p1, t9p2, t9p3, color="#165CFF")
        tri10 = Polygon(t10p1, t10p2, t10p3, color="#165CFF")
        tri1.set_fill(color="#165CFF", opacity=0)
        tri2.set_fill(color="#165CFF", opacity=0)
        tri3.set_fill(color="#165CFF", opacity=0)
        tri4.set_fill(color="#165CFF", opacity=0)
        tri5.set_fill(color="#165CFF", opacity=0)
        tri6.set_fill(color="#165CFF", opacity=0)
        tri7.set_fill(color="#165CFF", opacity=0)
        tri8.set_fill(color="#165CFF", opacity=0)
        tri9.set_fill(color="#165CFF", opacity=0)
        tri10.set_fill(color="#165CFF", opacity=0)
        
        # Añadir el triángulo a la escena
        self.play(Create(tri1), Create(tri2), Create(tri3), Create(tri4), Create(tri5), Create(tri6), Create(tri7), Create(tri8), Create(tri9), Create(tri10))
        self.wait(1)
        self.play(tri1.animate.set_fill(color="#165CFF", opacity=1)
        , tri2.animate.set_fill(color="#165CFF", opacity=1)
        , tri3.animate.set_fill(color="#165CFF", opacity=1)
        , tri4.animate.set_fill(color="#165CFF", opacity=1)
        ,tri5.animate.set_fill(color="#165CFF", opacity=1)
        , tri6.animate.set_fill(color="#165CFF", opacity=1)
        , tri7.animate.set_fill(color="#165CFF", opacity=1)
        , tri8.animate.set_fill(color="#165CFF", opacity=1)
        , tri9.animate.set_fill(color="#165CFF", opacity=1)
        , tri10.animate.set_fill(color="#165CFF", opacity=1), run_time=0.3)
        # Mostrar la escena
        self.wait()

#este logo fondo blanco y lineas azules infimath sin relleno, lineas mas delgadas
class logo2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.89, 0])
        t1p3 = np.array([0.03, 1.15, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.05, 1.13, 0])
        t3p2 = np.array([-0.065, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.522, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.558, 0])
        t9p2 = np.array([0.813, -0.484, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color="#165CFF")
        tri2 = Polygon(t2p1, t2p2, t2p3, color="#165CFF")
        tri3 = Polygon(t3p1, t3p2, t3p3, color="#165CFF")
        tri4 = Polygon(t4p1, t4p2, t4p3, color="#165CFF")
        tri5 = Polygon(t5p1, t5p2, t5p3, color="#165CFF")
        tri6 = Polygon(t6p1, t6p2, t6p3, color="#165CFF")
        tri7 = Polygon(t7p1, t7p2, t7p3, color="#165CFF")
        tri8 = Polygon(t8p1, t8p2, t8p3, color="#165CFF")
        tri9 = Polygon(t9p1, t9p2, t9p3, color="#165CFF")
        tri10 = Polygon(t10p1, t10p2, t10p3, color="#165CFF")

        tri1.set_stroke(width=2)
        tri2.set_stroke(width=2)
        tri3.set_stroke(width=2)
        tri4.set_stroke(width=2)
        tri5.set_stroke(width=2)
        tri6.set_stroke(width=2)
        tri7.set_stroke(width=2)
        tri8.set_stroke(width=2)
        tri9.set_stroke(width=2)
        tri10.set_stroke(width=2)
        
        # Añadir el triángulo a la escena
        self.play(Create(tri1), Create(tri2), Create(tri3), Create(tri4), Create(tri5), Create(tri6), Create(tri7), Create(tri8), Create(tri9), Create(tri10))
        self.wait(1)
        self.play(tri1.animate.set_fill(color="#165CFF", opacity=1)
        , tri2.animate.set_fill(color="#165CFF", opacity=1)
        , tri3.animate.set_fill(color="#165CFF", opacity=1)
        , tri4.animate.set_fill(color="#165CFF", opacity=1)
        ,tri5.animate.set_fill(color="#165CFF", opacity=1)
        , tri6.animate.set_fill(color="#165CFF", opacity=1)
        , tri7.animate.set_fill(color="#165CFF", opacity=1)
        , tri8.animate.set_fill(color="#165CFF", opacity=1)
        , tri9.animate.set_fill(color="#165CFF", opacity=1)
        , tri10.animate.set_fill(color="#165CFF", opacity=1), run_time=0.3)
        # Mostrar la escena
        self.wait()        

#aqui creamos el logo como un VGroup y lo animamos junto a las palabras infimath// logo final1 con fondo blanco
class logo3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.89, 0])
        t1p3 = np.array([0.03, 1.15, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.05, 1.13, 0])
        t3p2 = np.array([-0.065, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.522, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.558, 0])
        t9p2 = np.array([0.813, -0.484, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color="#165CFF")
        tri2 = Polygon(t2p1, t2p2, t2p3, color="#165CFF")
        tri3 = Polygon(t3p1, t3p2, t3p3, color="#165CFF")
        tri4 = Polygon(t4p1, t4p2, t4p3, color="#165CFF")
        tri5 = Polygon(t5p1, t5p2, t5p3, color="#165CFF")
        tri6 = Polygon(t6p1, t6p2, t6p3, color="#165CFF")
        tri7 = Polygon(t7p1, t7p2, t7p3, color="#165CFF")
        tri8 = Polygon(t8p1, t8p2, t8p3, color="#165CFF")
        tri9 = Polygon(t9p1, t9p2, t9p3, color="#165CFF")
        tri10 = Polygon(t10p1, t10p2, t10p3, color="#165CFF")

        triangulos = [tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10]
        #con esto disminuimos el ancho de las lineas de los triangulos
        for triangulo in triangulos:
            triangulo.set_stroke(width=1)
        
        logo = VGroup(tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10)
        logo.scale(0.5)
        
        # Crear animaciones para cada polígono
        animations = [Create(polygon) for polygon in logo]
        # Ejecutar todas las animaciones a la vez
        self.play(AnimationGroup(*animations, lag_ratio=0))

        animations2 = [polygon.animate.set_fill(color="#165CFF", opacity=1) for polygon in logo]
        self.play(AnimationGroup(*animations2, lag_ratio=0), run_time=0.5)
        
        logo.set_fill(color="#165CFF", opacity=1)
        self.play(logo.animate.shift(LEFT * 2))
        texto = Text("InfiMath", font_size=72, color="#09083B", font="Poppins SemiBold", t2w={'Math': BOLD})
        texto.next_to(logo, RIGHT)
        self.play(Write(texto.set_stroke("#09083B")))
        #creamos el logo como un todo, agrupamos todos los triangulos
        
        # Mostrar la escena
        self.wait()        

#logo final con fondo negro y logo con letras blancas
class logo4(Scene):
    def construct(self):
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.87, 0])
        t1p3 = np.array([0.03, 1.13, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.04, 1.13, 0])
        t3p2 = np.array([-0.055, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.53, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.548, 0])
        t9p2 = np.array([0.823, -0.474, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color=WHITE)
        tri2 = Polygon(t2p1, t2p2, t2p3, color=WHITE)
        tri3 = Polygon(t3p1, t3p2, t3p3, color=WHITE)
        tri4 = Polygon(t4p1, t4p2, t4p3, color=WHITE)
        tri5 = Polygon(t5p1, t5p2, t5p3, color=WHITE)
        tri6 = Polygon(t6p1, t6p2, t6p3, color=WHITE)
        tri7 = Polygon(t7p1, t7p2, t7p3, color=WHITE)
        tri8 = Polygon(t8p1, t8p2, t8p3, color=WHITE)
        tri9 = Polygon(t9p1, t9p2, t9p3, color=WHITE)
        tri10 = Polygon(t10p1, t10p2, t10p3, color=WHITE)

        triangulos = [tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10]
        #con esto disminuimos el ancho de las lineas de los triangulos
        for triangulo in triangulos:
            triangulo.set_stroke(width=1)
        
        logo = VGroup(tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10)
        logo.scale(0.5)
        
        # Crear animaciones para cada polígono
        animations = [Create(polygon) for polygon in logo]
        # Ejecutar todas las animaciones a la vez
        self.play(AnimationGroup(*animations, lag_ratio=0))

        animations2 = [polygon.animate.set_fill(color=WHITE, opacity=1) for polygon in logo]
        self.play(AnimationGroup(*animations2, lag_ratio=0), run_time=0.5)
        
        #logo.set_fill(color="#165CFF", opacity=1)
        self.play(logo.animate.shift(LEFT * 2))
        texto = Text("InfiMath", font_size=72, color=WHITE, font="Poppins SemiBold", t2w={'Math': BOLD})
        texto.next_to(logo, RIGHT)
        self.play(Write(texto))
        #creamos el logo como un todo, agrupamos todos los triangulos
        
        # Mostrar la escena
        self.wait()        

#logo sin letras
class logo5(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Definir los puntos triangulo 1
        t1p1 = np.array([0.03, 1.97, 0])
        t1p2 = np.array([1.48, 0.89, 0])
        t1p3 = np.array([0.03, 1.15, 0])

        # Definir los puntos triangulo 2
        t2p1 = np.array([1.48, 0.79, 0])
        t2p2 = np.array([0.91, -0.36, 0])
        t2p3 = np.array([0.036, 1.06, 0])
        # Definir los puntos triangulo 3
        t3p1 = np.array([-0.05, 1.13, 0])
        t3p2 = np.array([-0.065, 1.97, 0])
        t3p3 = np.array([-1.48, 0.84, 0])
        # Definir los puntos triangulo 4
        t4p1 = np.array([-0.084, 1.056, 0])
        t4p2 = np.array([-1.486, 0.768, 0])
        t4p3 = np.array([-0.882, -0.443, 0])
        # Definir los puntos triangulo 5
        t5p1 = np.array([-0.931, -0.496, 0])
        t5p2 = np.array([-1.513, 0.685, 0])
        t5p3 = np.array([-1.501, -0.818, 0])
        # Definir los puntos triangulo 6
        t6p1 = np.array([-0.015, 1.028, 0])
        t6p2 = np.array([0.83, -0.403, 0])
        t6p3 = np.array([-0.815, -0.473, 0])
        # Definir los puntos triangulo 7
        t7p1 = np.array([0.971, -0.425, 0])
        t7p2 = np.array([1.522, 0.754, 0])
        t7p3 = np.array([1.526, -0.684, 0])
        # Definir los puntos triangulo 8
        t8p1 = np.array([-0.862, -0.559, 0])
        t8p2 = np.array([-1.468, -0.894, 0])
        t8p3 = np.array([-0.004, -1.829, 0])
        # Definir los puntos triangulo 9
        t9p1 = np.array([-0.776, -0.558, 0])
        t9p2 = np.array([0.813, -0.484, 0])
        t9p3 = np.array([0.06, -1.798, 0])
        # Definir los puntos triangulo 10
        t10p1 = np.array([0.91, -0.48, 0])
        t10p2 = np.array([1.487, -0.743, 0])
        t10p3 = np.array([0.132, -1.81, 0])
  
  
        # Crear los triángulos con los puntos como argumentos
        tri1 = Polygon(t1p1, t1p2, t1p3, color="#165CFF")
        tri2 = Polygon(t2p1, t2p2, t2p3, color="#165CFF")
        tri3 = Polygon(t3p1, t3p2, t3p3, color="#165CFF")
        tri4 = Polygon(t4p1, t4p2, t4p3, color="#165CFF")
        tri5 = Polygon(t5p1, t5p2, t5p3, color="#165CFF")
        tri6 = Polygon(t6p1, t6p2, t6p3, color="#165CFF")
        tri7 = Polygon(t7p1, t7p2, t7p3, color="#165CFF")
        tri8 = Polygon(t8p1, t8p2, t8p3, color="#165CFF")
        tri9 = Polygon(t9p1, t9p2, t9p3, color="#165CFF")
        tri10 = Polygon(t10p1, t10p2, t10p3, color="#165CFF")

        triangulos = [tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10]
        #con esto disminuimos el ancho de las lineas de los triangulos
        for triangulo in triangulos:
            triangulo.set_stroke(width=1)
        
        logo = VGroup(tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9, tri10)
        logo.scale(1)
        
        # Crear animaciones para cada polígono
        animations = [Create(polygon) for polygon in logo]
        # Ejecutar todas las animaciones a la vez
        self.play(AnimationGroup(*animations, lag_ratio=0))

        animations2 = [polygon.animate.set_fill(color="#165CFF", opacity=1) for polygon in logo]
        self.play(AnimationGroup(*animations2, lag_ratio=0), run_time=0.5)
        
        logo.set_fill(color="#165CFF", opacity=1)
        
        
        # Mostrar la escena
        self.wait()        