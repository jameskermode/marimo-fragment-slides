import marimo

__generated_with = "0.13.0"
app = marimo.App(
    layout_file="layouts/demo.slides.json",
    html_head_file="fragment-slides.html",
)


# %% Slide 1 — Title
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Fragment Slides for Marimo

    Progressive reveal in slide presentations — like RISE fragments,
    but for [marimo](https://marimo.io).

    **Arrow keys** navigate slides *and* reveal fragments.
    """
    )
    return


# %% Slide 2 — Basic fragments
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Basic Fragments

    This content is visible immediately.

    <span class="fragment-start"></span>

    This paragraph **fades in** when you press the right arrow.

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    And this one appears on the *next* right-arrow press.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 3 — Math fragments
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Math Fragments

    Consider the **normal distribution**:

    <span class="fragment-start"></span>

    $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    Its **mean** is $\mu$ and **variance** is $\sigma^2$.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 4 — Multi-element fragments
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Multi-Element Fragments

    Markers group multiple paragraphs, lists, or math into a single reveal.

    <span class="fragment-start"></span>

    Everything between the markers is grouped into one fragment.

    Multiple paragraphs appear together as one step.

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    - Bullet one
    - Bullet two
    - Bullet three

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 5 — Interactive widget (define slider)
@app.cell(hide_code=True)
def _(mo):
    slider = mo.ui.slider(0, 10, value=5, label="Pick a number")
    return (slider,)


# %% Slide 5 — Interactive widget + fragment (read slider)
@app.cell(hide_code=True)
def _(mo, slider):
    mo.md(
        f"""
    ## Fragments with Widgets

    Fragments work alongside marimo's reactive widgets.

    {slider}

    <span class="fragment-start"></span>

    You picked **{slider.value}** — and this text was hidden until you
    pressed the right arrow.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 6 — Code fragment
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Code Fragments

    Fragments can reveal code blocks too:

    <span class="fragment-start"></span>

    ```python
    import marimo as mo

    app = marimo.App(
        layout_file="layouts/demo.slides.json",
        html_head_file="fragment-slides.html",
    )
    ```

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    That's all the setup you need.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 7 — How it works
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## How It Works

    <span class="fragment-start"></span>

    1. `fragment-slides.html` is injected via `html_head_file`
    2. CSS hides marker-delimited content
    3. JS intercepts arrow keys: **right** reveals, **left** hides
    4. Only applies in **run mode** (not edit mode)

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    Works with marimo's Swiper-based slide layout — no external
    dependencies required.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Slide 8 — Matplotlib fragment
@app.cell(hide_code=True)
def _(mo, np, plt):
    x = np.linspace(-4, 4, 200)
    _fig, _ax = plt.subplots(figsize=(8, 4))
    _ax.plot(x, np.exp(-x**2 / 2) / np.sqrt(2 * np.pi), linewidth=2)
    _ax.set_xlabel("x")
    _ax.set_ylabel("f(x)")
    _ax.set_title("Standard Normal PDF")
    _ax.grid(True, alpha=0.3)
    plt.tight_layout()

    mo.md(
        f"""
    ## Plot Fragments

    Plots appear on the slide as usual:

    {mo.as_html(_fig)}

    <span class="fragment-start"></span>

    The plot above is always visible. This caption fades in as a fragment.

    <span class="fragment-end"></span>
    """
    )
    return


# %% Imports (hidden utility cell)
@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (8, 5)
    return mo, np, plt


if __name__ == "__main__":
    app.run()
