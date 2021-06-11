# coding : utf-8

"""
    Research Engine by Joseph Konka
"""

from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Select, Slider, Button, RangeSlider
from bokeh.models import (Button, ColumnDataSource, CustomJS, DataTable,
                          NumberFormatter, RangeSlider, TableColumn)
from bokeh.layouts import row, column

import pandas as pd

# Load data
data = pd.read_csv("data/database.csv")
nationalities = list(data["Nationality"].dropna().unique())
nationalities = sorted(nationalities)

# Create widgets
# 1. Research field
text_input = TextInput(title="Player's name")
select = Select(title="Nationality", value=nationalities[0], options=nationalities)
# 2. Total results
min_value = 15
max_value = 50
age_slider = RangeSlider(start=min_value, end=max_value, step=0.1, title="Age Range")
results_limit = Slider(start=5, end=50, value=11, step=1, title="Number of results")
# 3. Button
button = Button(label="Submit")

# Source
data_ = data[data["Nationality"]==select.value]
source = ColumnDataSource(data_[:results_limit.value])
# source = ColumnDataSource(data)

# Result table
data_table = DataTable(
    source=source,
    columns=[
        TableColumn(field="Name", title="Full Name"),
        TableColumn(field="Club", title="Club"),
        TableColumn(field="Nationality", title="Nationality"),
        TableColumn(field="Overall", title="Overall"),
        TableColumn(field="Value", title="Value"),
        # TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="Age", title="Age (years)")
    ],
    width=800,
    height=500
)

# Callbacks
def search():
    '''callback..'''
    data_ = data[data["Nationality"]==select.value]
    data_table.source.data = data_[:results_limit.value]
button.on_click(search)

# show(
#     row(
#         column(
#            text_input, select, results_limit, button),
#         data_table
#     )
# )

curdoc().add_root(
    row(
        column(
            text_input,
            select,
            # age_slider,
            results_limit,
            button
        ),
        data_table
    )
)

# Set HTML page title
curdoc().title = 'Research Engine - Joseph Konka'
