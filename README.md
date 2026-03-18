# marimo-fragment-slides

Progressive reveal (fragments) for [marimo](https://marimo.io) slide presentations — like [RISE](https://rise.readthedocs.io/) fragments, but for marimo.

https://github.com/user-attachments/assets/placeholder — *replace with a screen recording*

## What it does

In marimo's slide layout, content normally appears all at once per slide. **Fragment slides** lets you reveal content step-by-step using arrow keys:

- **Right arrow**: reveals the next hidden fragment (then advances the slide when all fragments are shown)
- **Left arrow**: hides the last visible fragment (then goes to the previous slide)

Works with text, math (KaTeX), code blocks, plots, and marimo widgets.

## Quick start

1. Copy `fragment-slides.html` into your project
2. Create a slide layout file (e.g. `layouts/demo.slides.json`):
   ```json
   { "type": "slides", "data": {} }
   ```
3. Wire it up in your notebook:
   ```python
   import marimo
   app = marimo.App(
       layout_file="layouts/demo.slides.json",
       html_head_file="fragment-slides.html",
   )
   ```
4. Run the demo: `marimo run demo.py`

## Usage

Place `<span class="fragment-start"></span>` and `<span class="fragment-end"></span>` markers around the content you want to reveal progressively inside `mo.md()`:

```python
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## My Slide

    This is visible immediately.

    <span class="fragment-start"></span>

    This fades in on the first right-arrow press.

    $$E = mc^2$$

    <span class="fragment-end"></span>

    <span class="fragment-start"></span>

    This fades in on the second press.

    - Including lists
    - And **bold**, *italic* text

    <span class="fragment-end"></span>
    """)
    return
```

Everything between a start/end marker pair is grouped into one fragment. Multiple paragraphs, lists, math, or code blocks within a pair all reveal together.

> **Why not `<div class="fragment">`?** Wrapping content in `<div>` tags creates an HTML block that prevents marimo's markdown parser from rendering inline formatting (`**bold**`, `*italic*`, etc.) inside the div. The span-marker approach avoids this because inline `<span>` elements don't interrupt markdown processing.

## How it works

`fragment-slides.html` injects a `<style>` block and a `<script>` block via marimo's `html_head_file` option:

1. **Mode detection** — presentation styles only apply in run mode (`marimo run`), not edit mode (`marimo edit`)
2. **Fragment processing** — a `MutationObserver` watches for new slides in the Swiper container and hides fragment content before it's displayed (preventing flash)
3. **Keyboard navigation** — intercepts `ArrowRight`/`ArrowLeft` at the capture phase; reveals or hides one fragment group before letting the default slide navigation fire
4. **Shadow DOM handling** — marimo renders math inside `<marimo-tex>` custom elements with shadow DOM; the script injects styles into the shadow root for smooth opacity transitions

## Presentation typography

The CSS also scales up fonts for presentation use (headings, body text, math, code, widgets). This is scoped to `body.marimo-run-mode` so it doesn't affect editing. You can customise or remove these rules in `fragment-slides.html`.

## Requirements

- [marimo](https://marimo.io) >= 0.10.0 (slide layout support)
- No other dependencies

## Files

```
fragment-slides.html          # CSS + JS — copy this into your project
demo.py                       # Example notebook with all fragment types
layouts/demo.slides.json      # Minimal slide layout config
```

## License

MIT
