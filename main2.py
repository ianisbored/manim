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
PRINCESS = "#c68078"

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
    \definecolor{PRINCESS}{HTML}{c68078}
    """
))

class option2(Scene):
    def construct(self):
        Tex.set_default(color=WHITE)
        MathTex.set_default(color=WHITE)

        opt2 = Tex(r"\text{OPTION}", r"\text{ 2}", font_size=202).set_color_by_tex(r"\text{ 2}", YELLOW)
        title = Tex(r"\text{Ms. Marañon has to invest }",
        r"\text{P650 }", 
        r"\text{monthly for }",
        font_size=48)

        title2 = Tex(r"\text{20 years}",
        r"\text{ with an annual interest rate of }",
        r"\text{3.5\%}",
        r"\text{ compounded monthly.}",
        font_size=35)

        opt2.to_edge(UP + LEFT)

        text_group = VGroup(title, title2)
        text_group.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        text_group.next_to(opt2, DOWN, aligned_edge=LEFT, buff=0.5)

        left = VGroup(opt2, text_group)
        left.arrange(DOWN, aligned_edge=LEFT)
        left.to_edge(LEFT)

        self.play(Write(left))
        self.wait(1.5)

        principal = title.get_part_by_tex(r"P650")
        rate = title2.get_part_by_tex(r"3.5\%")
        m = title2.get_part_by_tex(r"compounded monthly")
        time = title2.get_part_by_tex(r"20 years")

        self.play(principal.animate.set_color(RED))
        self.play(time.animate.set_color(GREEN))
        self.play(rate.animate.set_color(ORANGE))
        self.play(m.animate.set_color(YELLOW))

        self.wait(1.5)

        principalDef = MathTex(r"\text{R}", r"= 650",).set_color_by_tex(r"\text{R}", RED)
        rateDef = MathTex(r"\text{r}", r"= 3.5\%", r"\text{ or }", r"0.035").set_color_by_tex(r"\text{r}", ORANGE)
        mDef = MathTex(r"\text{m}", r"= 12",).set_color_by_tex(r"\text{m}", YELLOW)
        timeDef = MathTex(r"\text{t}", r"= 20",).set_color_by_tex(r"\text{t}", GREEN)
        iDef = MathTex(r"\text{i}", r" = \frac{r}{m} = \frac{0.0035}{12} = 0.0029", font_size=35).set_color_by_tex(r"\text{i}", BLUE)
        nDef = MathTex(r"\text{n}", r" = mt = 12 \cdot 20 = 240", font_size=35).set_color_by_tex(r"\text{n}", CYAN)

        right = VGroup(principalDef, rateDef, mDef, timeDef, iDef, nDef)
        right.arrange(DOWN, aligned_edge=LEFT)
        right.to_edge(RIGHT, buff=0.5)

        self.play(Write(principalDef))
        self.play(Write(rateDef))
        self.play(Write(mDef))
        self.play(Write(timeDef))
        self.play(Write(iDef))
        self.play(Write(nDef))

        self.wait(3)
        
        self.play(Unwrite(right))
        self.play(Unwrite(left))

        
        aD = MathTex(r"\textcolor{PURPLE}{F_{AD}} = (1+\textcolor{BLUE}{i})(\textcolor{RED}{R})",
                    r"{(1+\textcolor{BLUE}{i})^{\textcolor{CYAN}{n}} - 1 \over",
                    r"\textcolor{BLUE}{i}}")
        aD1 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = ",
                    r"(1+\textcolor{BLUE}{0.0029})(\textcolor{RED}{650})",
                    r"{(1+\textcolor{BLUE}{0.0029})^{\textcolor{CYAN}{240}} - 1 \over",
                    r"\textcolor{BLUE}{0.0029}}").move_to(aD)
        aD2 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = ",
                    r"(\textcolor{LBLUE}{1.0029})(\textcolor{RED}{650})",
                    r"{(\textcolor{LBLUE}{1.0029})^{\textcolor{CYAN}{240}} - 1 \over",
                    r"\textcolor{BLUE}{0.0029}}").move_to(aD)
        aD3 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = ",
                    r"(\textcolor{LBLUE}{1.0029})(\textcolor{RED}{650})",
                    r"{\textcolor{LBLUECYAN}{2.0037} - 1 \over",
                    r"\textcolor{BLUE}{0.0029}}").move_to(aD)
        aD4 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = ",
                    r"(\textcolor{LBLUE}{1.0029})(\textcolor{RED}{650})",
                    r"{\textcolor{LBLUECYAN}{1.0037} \over",
                    r"\textcolor{BLUE}{0.0029}}").move_to(aD)
        aD5 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = ",
                    r"(\textcolor{LBLUE}{1.0029})(\textcolor{RED}{650})",
                    r"{(\textcolor{LBLUECYANBLUE}{346.1034})}").move_to(aD)
        aD6 = MathTex(r"\textcolor{PURPLE}{F_{AD}} = \textcolor{LBLUECYANBLUERED}{225,619.6}").move_to(aD)
        
        self.play(Write(aD))
        self.play(TransformMatchingShapes(aD, aD1), run_time=1)
        self.play(ReplacementTransform(aD1, aD2), run_time=1)
        self.play(ReplacementTransform(aD2, aD3), run_time=1)
        self.play(ReplacementTransform(aD3, aD4), run_time=1)
        self.play(TransformMatchingTex(aD4, aD5), run_time=1)
        self.play(ReplacementTransform(aD5, aD6), run_time=1)
        self.wait(3)