from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Slider, Button
from bokeh.models import (Button, ColumnDataSource, CustomJS, DataTable,
                          NumberFormatter, RangeSlider, TableColumn)
from bokeh.layouts import row, column

text_input = TextInput(title="Player's name")
results_limit = Slider(start=5, end=15, value=10, step=1, title="Number of results")
button = Button(label="Submit")

columns = [
    TableColumn(field="name", title="Employee Name"),
    TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
    TableColumn(field="years_experience", title="Experience (years)")
]

data_table = DataTable(source=ColumnDataSource({"name": ["John Doe"], "salary": [8000], "years_experience": [5]}), columns=columns, width=800)

# Callbacks
def search():
    '''callback..'''
    print(text_input.value)
    p.title.text = text_input.value
button.on_click(search)

# show(
#     row(
#         column(text_input, results_limit, button),
#         data_table
#     )
# )

curdoc().add_root(
    row(
        column(text_input, results_limit, button),
        data_table
    )
)