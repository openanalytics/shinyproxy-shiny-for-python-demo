# Code copied from https://shiny.posit.co/py/docs/overview.html
import matplotlib.pyplot as plt
import numpy as np
from shiny import ui, render, App

# Create some random data
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]

app_ui = ui.page_fixed(
    ui.h2("Playing with colormaps"),
    ui.markdown("""
        This app is based on a [Matplotlib example][0] that displays 2D data
        with a user-adjustable colormap. We use a range slider to set the data
        range that is covered by the colormap.

        [0]: https://matplotlib.org/3.5.3/gallery/userdemo/colormap_interactive_adjustment.html
    """),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_radio_buttons("cmap", "Colormap type",
                dict(viridis="Perceptual", gist_heat="Sequential", RdYlBu="Diverging")
            ),
            ui.input_slider("range", "Color range", -1, 1, value=(-1, 1), step=0.05),
        ),
        ui.output_plot("plot")
    )
)

def server(input, output, session):
    @output
    @render.plot
    def plot():
        fig, ax = plt.subplots()
        im = ax.imshow(data2d, cmap=input.cmap(), vmin=input.range()[0], vmax=input.range()[1])
        fig.colorbar(im, ax=ax)
        return fig


app = App(app_ui, server)
