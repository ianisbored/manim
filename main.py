from manim import *

WHITE = "#FBF1C7"
RED = "#CC241D"
ORANGE = "#d65d0e"
YELLOW = "#DFAB01"
GREEN = "#98971A"
BLUE = "#458588"
LBLUE = "#83a598"
CYAN = "#689D6A"
LBLUECYAN = "#76a181"
LBLUECYANBLUE = "#5e9385"
LBLUECYANBLUERED = "#955c51"
PURPLE = "#B16286"

MathTex.set_default(tex_template=TexTemplate(
    preamble=r"""
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{xcolor}
    \definecolor{WHITE}{HTML}{FBF1C7}
    \definecolor{RED}{HTML}{CC241D}
    \definecolor{ORANGE}{HTML}{d65d0e}
    \definecolor{YELLOW}{HTML}{DFAB01}
    \definecolor{GREEN}{HTML}{98971A}
    \definecolor{BLUE}{HTML}{458588}
    \definecolor{LBLUE}{HTML}{83A598}
    \definecolor{CYAN}{HTML}{689D6A}
    \definecolor{LBLUECYAN}{HTML}{76a181}
    \definecolor{LBLUECYANBLUE}{HTML}{5e9385}
    \definecolor{LBLUECYANBLUERED}{HTML}{955c51}
    \definecolor{PURPLE}{HTML}{B16286}
    """
))

class option1(Scene):
    def construct(self):
        Tex.set_default(color=WHITE)
        MathTex.set_default(color=WHITE)

        opt1 = Tex(r"\text{OPTION}", r"\text{ 1}", font_size=202).set_color_by_tex(r"\text{ 1}", YELLOW)
        title = Tex(r"\text{Ms. Marañon has to deposit }",
        r"\text{P400 }", 
        r"\text{every month.}", 
        font_size=48)

        title2 = Tex(r"\text{It earns }",
        r"\text{3\%}",
        r"\text{ annual interest,}",
        r"\text{ compounded monthly, }",
        r"\text{for }",
        r"\text{15 years.}", 
        font_size=35)

        opt1.to_edge(UP + LEFT)

        text_group = VGroup(title, title2)
        text_group.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        text_group.next_to(opt1, DOWN, aligned_edge=LEFT, buff=0.5)

        left = VGroup(opt1, text_group)
        left.arrange(DOWN, aligned_edge=LEFT)
        left.to_edge(LEFT)

        self.play(Write(left))
        self.wait(1.5)

        principal = title.get_part_by_tex(r"P400")
        rate = title2.get_part_by_tex(r"3\%")
        m = title2.get_part_by_tex(r"compounded monthly")
        time = title2.get_part_by_tex(r"15 years")

        self.play(principal.animate.set_color(RED))
        self.play(rate.animate.set_color(ORANGE))
        self.play(m.animate.set_color(YELLOW))
        self.play(time.animate.set_color(GREEN)) 

        self.wait(1.5)

        principalDef = MathTex(r"\text{R}", r"= 400",).set_color_by_tex(r"\text{R}", RED)
        rateDef = MathTex(r"\text{r}", r"= 3\%", r"\text{ or }", r"0.03").set_color_by_tex(r"\text{r}", ORANGE)
        mDef = MathTex(r"\text{m}", r"= 12",).set_color_by_tex(r"\text{m}", YELLOW)
        timeDef = MathTex(r"\text{t}", r"= 15",).set_color_by_tex(r"\text{t}", GREEN)
        iDef = MathTex(r"\text{i}", r" = \frac{r}{m} = \frac{0.03}{12} = 0.0025", font_size=35).set_color_by_tex(r"\text{i}", BLUE)
        nDef = MathTex(r"\text{n}", r" = mt = 12 \cdot 15 = 180", font_size=35).set_color_by_tex(r"\text{n}", CYAN)

        right = VGroup(principalDef, rateDef, mDef, timeDef, iDef, nDef)
        right.arrange(DOWN, aligned_edge=LEFT)
        right.to_edge(RIGHT, buff=1)

        self.play(Write(principalDef))
        self.play(Write(rateDef))
        self.play(Write(mDef))
        self.play(Write(timeDef))
        self.play(Write(iDef))
        self.play(Write(nDef))

        self.wait(3)
        
        self.play(Unwrite(right))
        self.play(Unwrite(left))

        
        oA = MathTex(r"\textcolor{PURPLE}{F} = \textcolor{RED}{R}",
                    r"{(1+\textcolor{BLUE}{i})^{\textcolor{CYAN}{n}} - 1 \over",
                    r"\textcolor{BLUE}{i}}")
        oA1 = MathTex(r"\textcolor{PURPLE}{F} = ", 
                    r"\textcolor{RED}{400}",
                    r"{(1+\textcolor{BLUE}{0.0025})^{\textcolor{CYAN}{180}} - 1 \over",
                    r"\textcolor{BLUE}{0.0025}}").move_to(oA)
        oA2 = MathTex(r"\textcolor{PURPLE}{F} = ", 
                    r"\textcolor{RED}{400}",
                    r"{(\textcolor{LBLUE}{1.0025})^{\textcolor{CYAN}{180}} - 1 \over",
                    r"\textcolor{BLUE}{0.0025}}").move_to(oA)
        oA3 = MathTex(r"\textcolor{PURPLE}{F} = ", 
                    r"\textcolor{RED}{400}",
                    r"{\textcolor{LBLUECYAN}{1.5674} - 1 \over",
                    r"\textcolor{BLUE}{0.0025}}").move_to(oA)
        oA4 = MathTex(r"\textcolor{PURPLE}{F} = ", 
                    r"\textcolor{RED}{400}",
                    r"{\textcolor{LBLUECYAN}{0.5674} \over",
                    r"\textcolor{BLUE}{0.0025}}").move_to(oA)
        oA5 = MathTex(r"\textcolor{PURPLE}{F} = ", 
                    r"\textcolor{RED}{400}",
                    r"\textcolor{LBLUECYANBLUE}{(226.96)}").move_to(oA)
        oA6 = MathTex(r"\textcolor{PURPLE}{F} = \textcolor{LBLUECYANBLUERED}{90,784}").move_to(oA)

        self.play(Write(oA))
        self.play(TransformMatchingShapes(oA, oA1), run_time=1)
        self.play(ReplacementTransform(oA1, oA2), run_time=1)
        self.play(ReplacementTransform(oA2, oA3), run_time=1)
        self.play(ReplacementTransform(oA3, oA4), run_time=1)
        self.play(TransformMatchingTex(oA4, oA5), run_time=1)
        self.play(ReplacementTransform(oA5, oA6), run_time=1)
        self.wait(3)