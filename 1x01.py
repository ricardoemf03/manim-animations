from manim import *

class scene1(Scene): #Clasificar los números
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        texto = Tex("Clasificar los números", color = BLACK).scale(1.5)
        texto.set_stroke(BLACK)
        self.wait(1)
        self.play(Write(texto), run_time = 0.9)
        self.wait(3)

class scene2(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        names = [MathTex("\\text{1. Números naturales } ","\\mathbb{N}", color = BLACK), 
                 MathTex("\\text{2. Números enteros } ","\\mathbb{Z}", color = BLACK),
                 MathTex("\\text{3. Números racionales } ","\\mathbb{Q}", color = BLACK),
                 MathTex("\\text{4. Números irracionales } ","\\mathbb{I}", color = BLACK),
                 MathTex("\\text{5. Números reales } ","\\mathbb{R}", color = BLACK)]
        for i in range(len(names)):
            names[i].scale(1.5)
            names[i].set_stroke(BLACK)
        self.wait(1.5)
        self.play(FadeIn(names[0]))
        for i in range(len(names)-1):
            self.play(AnimationGroup(FadeOut(names[i], shift = UP*1.5),
                                     FadeIn(names[(i+1)%len(names)], shift = UP*1.5)))
            self.wait(0.8)
        self.wait(3)

class scene3(Scene): # números naturales
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        naturales = MathTex("\\text{1. Números naturales } ",
                            color = BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{N}", "= ", "\\{1,2,3,4,5,\\ldots \\} "
                            , color = BLACK).set_stroke(BLACK).scale(1.5)
        # Crear los textos
        suma = MathTex("\\text{ Suma:}", color=BLACK).set_stroke(BLACK)
        resta = MathTex("\\text{ Resta: }", color=BLACK).set_stroke(BLACK)
        multi = MathTex("\\text{ Multiplicación:}", color=BLACK).set_stroke(BLACK)
        divi = MathTex(" \\text{ División: }", color=BLACK).set_stroke(BLACK)
        # Crear las expresiones matemáticas
        suma_expr = MathTex("2 + 2 = 4 \\in \\mathbb{N}", color=BLACK).set_stroke(BLACK)
        resta_expr = MathTex("10 - 7 = 3 \\in \\mathbb{N}", color=BLACK).set_stroke(BLACK)
        multi_expr = MathTex("3 \\times 4 = 12 \\in \\mathbb{N}", color=BLACK).set_stroke(BLACK)
        divi_expr = MathTex("12 \\div 4 = 3 \\in \\mathbb{N}", color=BLACK).set_stroke(BLACK)
        N_1, N_2, N_3 = N[0], N[1], N[2]
        self.wait(1)
        self.play(Write(naturales), run_time = 0.9)
        self.wait(1)
        self.play(naturales.animate.shift(UP*3+LEFT*3.75))
        self.wait(1)
        # Inicialmente, mostrar solo N en el centro
        N_1.move_to(ORIGIN)
        self.play(Write(N_1))
        self.wait(1)
        
        # Mover N a la izquierda mientras se muestra el signo igual
        self.play(
            N_1.animate.shift(LEFT * 0.1),
            Write(N_2.next_to(N_1, RIGHT), buff = 0.1), run_time = 0.7            
        )
        self.wait(1)
        
        # Mover N y el signo igual a la izquierda mientras se muestra el resto de la expresión
        self.play(
            N_1.animate.shift(LEFT * 3),
            N_2.animate.shift(LEFT * 3)            
        )
        self.play(Write(N_3.next_to(N_2, RIGHT), buff = 0.1))
        self.wait(1)
        self.play(N.animate.scale(0.7), N.animate.next_to(naturales, DOWN).scale(0.7).shift(RIGHT*0.6), run_time = 0.6)
        self.wait(2)
        #ahora ponemos lo de la suma resta multiplicación y division        
        texts = VGroup(suma, resta, multi, divi).arrange(DOWN, aligned_edge=RIGHT, buff=0.5)
        texts.next_to(N, DOWN).shift(DOWN*0.5)
        texts.shift(RIGHT*1)
        expr = VGroup(suma_expr, resta_expr, multi_expr, divi_expr).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        expr.next_to(texts, RIGHT).shift(RIGHT*0.5)
        self.play(Write(texts), run_time = 2)
        for i, text in enumerate(expr):
            self.play(Write(expr[i]), run_time=1)
            self.wait(1)
        box1 = SurroundingRectangle(suma_expr[0][-2], buff=.1, color=RED)
        self.play(Create(box1))
        self.wait(1)
        self.play(FadeOut(box1))
        self.play(FadeOut(texts, expr))
        self.wait(1)
        pero = MathTex("\\text{ Pero... }", color = BLACK).set_stroke(BLACK)
        not_in = MathTex("9-10 = -1", color=BLACK).set_stroke(BLACK)
        exp_not_in = MathTex(" \\notin \mathbb{N}", color= BLACK).set_stroke(BLACK)
        self.play(Write(pero.next_to(N, DOWN).shift(LEFT*1.6+DOWN*0.5)))
        self.play(Write(not_in))
        self.wait(1)
        self.play(not_in.animate.shift(LEFT*0.5))
        self.play(Write(exp_not_in.next_to(not_in, RIGHT)))
        self.wait(2)
        self.play(FadeOut(N, naturales, pero, not_in, exp_not_in))
        self.wait(1)

class scene4(Scene): #números enteros
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        enteros = MathTex("\\text{2. Números enteros } ",
                            color = BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{Z}", "= ", "\\{\\ldots, -3,-2,-1,0,1,2,3,\\ldots \\} "
                            , color = BLACK).set_stroke(BLACK).scale(1)
        # Crear los textos
        suma = MathTex("\\text{ Suma:}", color=BLACK).set_stroke(BLACK)
        resta = MathTex("\\text{ Resta: }", color=BLACK).set_stroke(BLACK)
        multi = MathTex("\\text{ Multiplicación:}", color=BLACK).set_stroke(BLACK)
        divi = MathTex(" \\text{ División: }", color=BLACK).set_stroke(BLACK)
        # Crear las expresiones matemáticas
        suma_expr = MathTex("10 + 2 = 12 \\in \\mathbb{Z}", color=BLACK).set_stroke(BLACK)
        resta_expr = MathTex("9 - 10 = -1 \\in \\mathbb{Z}", color=BLACK).set_stroke(BLACK)
        multi_expr = MathTex("(-1) \\times 4 = -4 \\in \\mathbb{Z}", color=BLACK).set_stroke(BLACK)
        divi_expr = MathTex("15 \\div 3 = 5 \\in \\mathbb{Z}", color=BLACK).set_stroke(BLACK)
        N_1, N_2, N_3 = N[0], N[1], N[2]
        self.wait(1)
        self.play(Write(enteros), run_time = 0.9)
        self.wait(1)
        self.play(enteros.animate.shift(UP*3+LEFT*3.75))
        self.wait(1)
        # Inicialmente, mostrar solo N en el centro
        N_1.move_to(ORIGIN)
        self.play(Write(N_1))
        self.wait(1)
        
        # Mover N a la izquierda mientras se muestra el signo igual
        self.play(
            N_1.animate.shift(LEFT * 0.1),
            Write(N_2.next_to(N_1, RIGHT), buff = 0.1), run_time = 0.7            
        )
        self.wait(1)
        
        # Mover N y el signo igual a la izquierda mientras se muestra el resto de la expresión
        self.play(
            N_1.animate.shift(LEFT * 3),
            N_2.animate.shift(LEFT * 3)            
        )
        self.play(Write(N_3.next_to(N_2, RIGHT), buff = 0.1))
        self.wait(1)
        self.play(N.animate.scale(0.7), N.animate.next_to(enteros, DOWN).scale(0.7).shift(RIGHT*0.6), run_time = 0.6)
        self.wait(2)
        #ahora ponemos lo de la suma resta multiplicación y division        
        texts = VGroup(suma, resta, multi, divi).arrange(DOWN, aligned_edge=RIGHT, buff=0.5)
        texts.next_to(N, DOWN).shift(DOWN*0.5)
        texts.shift(RIGHT*1)
        expr = VGroup(suma_expr, resta_expr, multi_expr, divi_expr).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        expr.next_to(texts, RIGHT).shift(RIGHT*0.5)
        self.play(Write(texts), run_time = 2)
        for i, text in enumerate(expr):
            self.play(Write(expr[i]), run_time=1)
            self.wait(1)
        self.play(FadeOut(texts, expr))
        self.wait(1)
        pero = MathTex("\\text{ Pero... }", color = BLACK).set_stroke(BLACK)
        not_in = MathTex("9 \\div 2 = 4.5", color=BLACK).set_stroke(BLACK)
        exp_not_in = MathTex(" \\notin \mathbb{Z}", color= BLACK).set_stroke(BLACK)
        self.play(Write(pero.next_to(N, DOWN).shift(LEFT*1.6+DOWN*0.5)))
        self.play(Write(not_in))
        self.wait(1)
        self.play(not_in.animate.shift(LEFT*0.5))
        self.play(Write(exp_not_in.next_to(not_in, RIGHT)))
        self.wait(2)
        self.play(FadeOut(N, enteros, pero, not_in, exp_not_in))
        self.wait(1)

class scene5(Scene): #números racionales
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        racional = MathTex("\\text{3. Números racionales } ",
                            color = BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{Q}", "= ", "\\left\\{\\frac{p}{q}\\Big| p \\in \\mathbb{Z}, q \\in \\mathbb{Z}\\backslash\\{0\\} \\right\\} "
                            , color = BLACK).set_stroke(BLACK).scale(1)
        N[2][1].set_color(RED)
        N[2][3].set_color(GREEN)
        N[2][7].set_color(RED)
        N[2][11].set_color(GREEN)
        # Crear los textos
        suma = MathTex("\\text{ Suma:}", color=BLACK).set_stroke(BLACK).scale(0.8)
        resta = MathTex("\\text{ Resta: }", color=BLACK).set_stroke(BLACK).scale(0.8)
        multi = MathTex("\\text{ Multiplicación:}", color=BLACK).set_stroke(BLACK).scale(0.8)
        divi = MathTex(" \\text{ División: }", color=BLACK).set_stroke(BLACK).scale(0.8)
        sqrt = MathTex(" \\text{ Raíz: }", color=BLACK).set_stroke(BLACK).scale(0.8)
        # Crear las expresiones matemáticas
        suma_expr = MathTex("\\frac{4}{3} + \\frac{1}{3} = \\frac{5}{3} \\in \\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(0.5)
        resta_expr = MathTex("\\frac{2}{5} - \\frac{1}{5} = \\frac{1}{5} \\in \\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(0.5)
        multi_expr = MathTex("\\frac{3}{2} \\times \\frac{5}{6} = \\frac{15}{12} \\in \\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(0.5)
        divi_expr = MathTex("\\frac{2}{3} \\div \\frac{3}{2} = \\frac{4}{9} \\in \\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(0.5)
        sqrt_expr = MathTex("\\sqrt{4} = 2 \\in \\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(0.4)
        numbers = MathTex("\\frac{1}{2},", "0.333\\ldots",", \\frac{3}{4}, 00.74, 0.252525\\ldots, -\\frac{6}{5}, \\frac{-195}{3}, -0.83, 2, 3, -1, 0", color = BLACK).set_stroke(BLACK).scale(0.6)
        box2 = SurroundingRectangle(numbers[1], buff= .1, color=RED)
        under_box = MathTex("\\frac{1}{3}", color = BLACK).set_stroke(BLACK).scale(0.6)
        N_1, N_2, N_3 = N[0], N[1], N[2]
        self.wait(1)
        self.play(Write(racional), run_time = 0.9)
        self.wait(1)
        self.play(racional.animate.shift(UP*3+LEFT*3.75))
        self.wait(1)
        # Inicialmente, mostrar solo N en el centro
        N_1.move_to(ORIGIN)
        self.play(Write(N_1))
        self.wait(1)
        
        # Mover N a la izquierda mientras se muestra el signo igual
        self.play(
            N_1.animate.shift(LEFT * 0.1),
            Write(N_2.next_to(N_1, RIGHT), buff = 0.1), run_time = 0.7            
        )
        self.wait(1)
        
        # Mover N y el signo igual a la izquierda mientras se muestra el resto de la expresión
        self.play(
            N_1.animate.shift(LEFT * 3),
            N_2.animate.shift(LEFT * 3)            
        )
        self.play(Write(N_3.next_to(N_2, RIGHT), buff = 0.1))
        self.wait(3)
        self.play(N.animate.scale(0.5), N.animate.next_to(racional, DOWN).scale(0.5).shift(RIGHT*0.6), run_time = 0.6)
        self.wait(2)
        self.play(Write(numbers))
        self.wait(2)
        self.play(Create(box2))
        self.play(Write(under_box.next_to(box2, DOWN)))
        self.wait(2)
        self.play(FadeOut(box2, under_box))
        self.play(FadeOut(numbers))
        #ahora ponemos lo de la suma resta multiplicación division y raiz        
        texts = VGroup(suma, resta, multi, divi, sqrt).arrange(DOWN*1.3, aligned_edge=RIGHT, buff=0.5)
        texts.next_to(N, DOWN).shift(DOWN*0.5)
        texts.shift(RIGHT*1)
        expr = VGroup(suma_expr, resta_expr, multi_expr, divi_expr, sqrt_expr).arrange(DOWN*0.9, aligned_edge=LEFT, buff=0.5)
        expr.next_to(texts, RIGHT).shift(RIGHT*0.5)
        self.play(Write(texts), run_time = 2)
        for i, text in enumerate(expr):
            self.play(Write(expr[i]), run_time=1)
            self.wait(1)
        self.play(FadeOut(texts, expr))
        self.wait(1)
        pero = MathTex("\\text{ Pero... }", color = BLACK).set_stroke(BLACK)
        not_in = MathTex("\\sqrt{2}  = 1.4142\\ldots", color=BLACK).set_stroke(BLACK)
        exp_not_in = MathTex(" \\notin \mathbb{Q}", color= BLACK).set_stroke(BLACK)
        self.play(Write(pero.next_to(N, DOWN).shift(LEFT*1.6+DOWN*0.5)))
        self.play(Write(not_in))
        self.wait(1)
        self.play(not_in.animate.shift(LEFT*0.5))
        self.play(Write(exp_not_in.next_to(not_in, RIGHT)))
        self.wait(2)
        self.play(FadeOut(N, racional, pero, not_in, exp_not_in))
        self.wait(1)

class scene6(Scene): # números irracionales
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        irra = MathTex("\\text{4. Números irracionales } ",
                            color = BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{I}"," = ", " \\text{ Números que no son racionales} "
                            , color = BLACK).set_stroke(BLACK).scale(0.9)
        # Crear los textos
        suma = MathTex("\\pi = 3.1415926535\\ldots", color=BLACK).set_stroke(BLACK)
        resta = MathTex("e = 2.7182818284\\ldots", color=BLACK).set_stroke(BLACK)
        multi = MathTex("\\sqrt{2} = 1.4142135623 \\ldots", color=BLACK).set_stroke(BLACK)
        divi = MathTex(" (1+\\sqrt{5})/2 = 1.6180339887 \\ldots", color=BLACK).set_stroke(BLACK)
        siete = MathTex(" \\sqrt{7} = 2.6457513110 \\ldots", color=BLACK).set_stroke(BLACK)
        N_1, N_2, N_3 = N[0], N[1], N[2]
        self.wait(1)
        self.play(Write(irra), run_time = 0.9)
        self.wait(1)
        self.play(irra.animate.shift(UP*3+LEFT*3.75))
        self.wait(1)
        # Inicialmente, mostrar solo N en el centro
        N_1.move_to(ORIGIN)
        self.play(Write(N_1))
        self.wait(1)
        # Mover N a la izquierda mientras se muestra el signo igual
        self.play(
            N_1.animate.shift(LEFT * 0.1),
            Write(N_2.next_to(N_1, RIGHT), buff = 0.1), run_time = 0.7            
        )
        self.wait(1)
        # Mover N y el signo igual a la izquierda mientras se muestra el resto de la expresión
        self.play(
            N_1.animate.shift(LEFT * 3),
            N_2.animate.shift(LEFT * 3)            
        )
        self.play(Write(N_3.next_to(N_2, RIGHT), buff = 0.1))
        self.wait(1)
        self.play(N.animate.scale(0.7), N.animate.next_to(irra, DOWN).scale(0.7).shift(RIGHT*0.6), run_time = 0.6)
        self.wait(2)
        #ahora ponemos lo de la suma resta multiplicación y division        
        texts = VGroup(suma, resta, multi, divi, siete).arrange(DOWN, aligned_edge=RIGHT, buff=0.5)
        texts.shift(DOWN*0.5)
        for i, text in enumerate(texts):
            self.play(Write(texts[i]), run_time = 1)
            self.wait(1)
        self.wait(1)
        self.play(FadeOut(N, irra, texts))
        self.wait(1)

class scene7(Scene): # números reales
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        reales = MathTex("\\text{ 5. Números reales}", color= BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{R}"," = ", " \\text{ Números racionales e irracionales} "
                            , color = BLACK).set_stroke(BLACK).scale(0.9)
        N_1, N_2, N_3 = N[0], N[1], N[2]
        self.wait(1)
        self.play(Write(reales), run_time = 0.9)
        self.wait(1)
        self.play(reales.animate.shift(UP*3+LEFT*3.75))
        self.wait(1)
        # Inicialmente, mostrar solo N en el centro
        N_1.move_to(ORIGIN)
        self.play(Write(N_1))
        self.wait(1)
        # Mover N a la izquierda mientras se muestra el signo igual
        self.play(
            N_1.animate.shift(LEFT * 0.1),
            Write(N_2.next_to(N_1, RIGHT), buff = 0.1), run_time = 0.7            
        )
        self.wait(1)
        # Mover N y el signo igual a la izquierda mientras se muestra el resto de la expresión
        self.play(
            N_1.animate.shift(LEFT * 3),
            N_2.animate.shift(LEFT * 3)            
        )
        self.play(Write(N_3.next_to(N_2, RIGHT), buff = 0.1))
        self.wait(1)
        self.play(N.animate.scale(0.7), N.animate.next_to(reales, DOWN).scale(0.7).shift(RIGHT*0.6), run_time = 0.6)
        self.wait(1)
        numbers = MathTex("\\ldots,-\\pi, -3, -2, -\\frac{1}{2}, 0, 1, \\frac{3}{2}, 2 , e, 3, \\pi, \\ldots", color = BLACK).set_stroke(BLACK).scale(0.95)
        self.play(Write(numbers))
        self.wait(4)
        self.play(FadeOut(numbers))
        self.wait(1)
        operations= MathTex("\\text{ Suma}", "\\text{ Resta}", "\\text{ Multiplicación}",
                             "\\text{ División}", "\\text{ Raíz}", color= BLACK).set_stroke(BLACK).scale(0.85)
        vg_operations = VGroup()
        for i in range(5):
            vg_operations.add(operations[i])
        vg_operations.arrange(DOWN, aligned_edge = RIGHT,buff=0.5)
        vg_operations.shift(LEFT*1)
        self.play(Write(vg_operations), run_time = 2)
        self.wait(1)
        self.play(vg_operations.animate.shift(LEFT*1.5))
        brace = Brace(vg_operations, direction = RIGHT, color = BLACK).set_stroke(BLACK)
        op_bas = MathTex("\\text{ Propiedades}", color=BLACK).set_stroke(BLACK).scale(0.65)
        op_bas.next_to(brace, RIGHT)
        self.play(FadeIn(brace, op_bas))
        self.wait(2)
        self.play(FadeOut(vg_operations, brace, op_bas))
        self.wait(1)
        aunque = MathTex("\\text{ Aunque\\ldots}", color= BLACK).set_stroke(BLACK).scale(0.85)
        aunque.next_to(N, DOWN).shift(LEFT*0.5)
        self.play(Write(aunque))
        complejo = MathTex("\\text{¿}\\sqrt{-1}\\text{?}", color = BLACK).set_stroke(BLACK)
        texto = Paragraph("Lo dejamos para más adelante en el curso cuando introduzcamos",
                          "el conjunto de los números complejos",
                        color = BLACK).set_stroke(BLACK).scale(0.5)
        self.play(Write(complejo))
        self.wait(2)
        texto.next_to(complejo, DOWN).shift(DOWN*1.3)
        self.play(Write(texto))
        self.wait(1.5)
        self.play(FadeOut(reales, N, aunque, complejo, texto))
        self.wait(1.5)

class scene8(MovingCameraScene): #moviendo la camara para mostrar visualmente los conjuntos
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        # Crear el primer círculo con la letra "N"
        small_circle = Circle(radius=3, color=BLACK).set_stroke(BLACK)
        N = MathTex("\\mathbb{N}", color=BLACK).move_to(small_circle.get_center()).set_stroke(BLACK).scale(4)
        Z = MathTex("\\mathbb{Z}", color=BLACK).set_stroke(BLACK).scale(4).shift((UP+RIGHT)*3.5)
        Q = MathTex("\\mathbb{Q}", color=BLACK).set_stroke(BLACK).scale(4).shift(RIGHT*9.5)
        I = MathTex("\\mathbb{I}", color=BLACK).set_stroke(BLACK).scale(4)
        R = MathTex("\\mathbb{R}", color=BLACK).set_stroke(BLACK).scale(9)
        self.wait(1.5)
        # Añadir el círculo y la letra "N" a la escena
        self.play(Create(small_circle), Write(N))
        self.play(small_circle.animate.set_fill(color = BLUE, opacity=0.5))
        self.wait(1)
        # Hacer un movimiento de cámara que se aleje (zoom out)
        self.play(self.camera.frame.animate.scale(2), small_circle.animate.set_stroke(width=10))
        self.wait(1)
        
        # Crear un círculo más grande que encierre al primero
        large_circle = Circle(radius=7, color=BLACK).set_stroke(BLACK, 10)
        
        # Mover el círculo grande para que esté centrado con el pequeño
        large_circle.move_to(small_circle.get_center())
        
        self.play(Create(large_circle), Write(Z))
        self.bring_to_front(small_circle, N)
        self.play(large_circle.animate.set_fill(color = ORANGE, opacity=0.5))
        
        # Añadir una pausa para que el círculo grande se quede un momento en pantalla
        self.wait(1)
        # Hacer un movimiento de cámara que se aleje (zoom out)
        self.play(self.camera.frame.animate.scale(2), large_circle.animate.set_stroke(width=15))
        self.wait(1)
        ellipse = Ellipse(width=26, height=22, color=BLACK).set_stroke(BLACK, 15)
        ellipse.move_to(small_circle.get_center())

        self.play(Create(ellipse), Write(Q))
        self.bring_to_front(large_circle, Z)
        self.bring_to_front(small_circle, N)
        self.play(ellipse.animate.set_fill(color = GREEN, opacity=0.5))
        self.wait(1)
        circle_i = Circle(radius=3, color=BLACK).set_stroke(BLACK, 15).shift(RIGHT*14.5+UP*9.5)
        I.move_to(circle_i.get_center())
        self.play(Create(circle_i), Write(I))
        self.play(circle_i.animate.set_fill(color = RED, opacity=0.5))
        self.wait(1)
        self.play(self.camera.frame.animate.scale(1.5))
        rectangulo = Rectangle(width=38, height=30, color = BLACK, stroke_width =20).set_stroke(BLACK)
        rectangulo.move_to(small_circle.get_center())
        R.next_to(rectangulo, UP).shift(LEFT*16+UP*1)
        self.play(Create(rectangulo), Write(R))
        self.bring_to_front(ellipse, Q)
        self.bring_to_front(large_circle, Z)
        self.bring_to_front(small_circle, N)
        self.play(rectangulo.animate.set_fill(color = PURPLE_C, opacity=0.5))
        self.wait(1)
        self.play(FadeOut(circle_i, I))
        self.wait(2)
        self.play(FadeOut(N, Z, Q, R, small_circle, large_circle, ellipse, rectangulo))
        self.wait(2)

class scene9(Scene): #recta real
    def construct(self):
        self.camera.background_color = "#FFFFD3"
        # Crear una recta numérica
        name = Tex("La recta real", color = BLACK).set_stroke(BLACK).scale(1.5)
        recta = NumberLine(
            x_range=[-5, 5, 1],  # Rango de la recta numérica
            length=10,           # Longitud de la recta numérica
            color=BLACK,          # Color de la recta numérica
            include_numbers=True, # Incluir números en la recta
            label_direction=DOWN,  # Dirección de las etiquetas de los números
        ).set_stroke(BLACK)
        # Cambiar el color de los números de la recta
        for number in recta.numbers:
            number.set_color(BLACK).set_stroke(BLACK)
        # Crear flechas en los extremos
        flecha_izquierda = Arrow(
            start=recta.get_start(),
            end=recta.get_start()+LEFT*0.5,
            color=BLACK,
            buff=0
        ).set_stroke(BLACK)

        flecha_derecha = Arrow(
            start=recta.get_end() ,
            end=recta.get_end()+ RIGHT * 0.5,
            color=BLACK,
            buff=0
        ).set_stroke(BLACK)
        # Añadir la recta y las flechas a la escena
        recta1 = VGroup(flecha_izquierda, flecha_derecha, recta)
        self.wait(1)
        self.play(Write(name))
        self.wait(2)
        self.play(name.animate.shift(UP*3+LEFT*4))
        self.wait(1)
        self.play(Write(recta1))

        # Crear un punto para π
        punto_pi = Dot(point=recta.n2p(PI), color=RED)
        etiqueta_pi = Text("π", color = BLACK).next_to(punto_pi, UP).set_stroke(BLACK)

        # Crear un punto para 0.5
        punto_05 = Dot(point=recta.n2p(0.5), color=GREEN)
        etiqueta_05 = Text("0.5", color = BLACK).next_to(punto_05, UP).set_stroke(BLACK)
        # Crear un punto para e
        punto_e = Dot(point=recta.n2p(-2.7182), color=BLUE)
        etiqueta_e = Text("-e", color = BLACK).next_to(punto_e, UP).set_stroke(BLACK)
        # crear punto para menos nueve medios
        punto_9 =Dot(point = recta.n2p(-4.5), color = ORANGE)
        etiqueta_9 = Text("-9/2", color = BLACK).next_to(punto_9, UP).set_stroke(BLACK).scale(0.75)

        self.play(FadeIn(punto_pi, etiqueta_pi))
        self.wait(1)
        self.play(FadeIn(punto_05, etiqueta_05))
        self.wait(1)
        self.play(FadeIn(punto_e, etiqueta_e))
        self.wait(1)
        self.play(FadeIn(punto_9, etiqueta_9))
        self.wait(1)
        self.play(FadeOut(punto_05, punto_pi, punto_e, punto_9,
                          etiqueta_05, etiqueta_pi, etiqueta_e, etiqueta_9))
        self.wait(1)
        self.play(FadeOut(recta1, name))
        # Esperar 2 segundos para visualizar la recta
        self.wait(2)

