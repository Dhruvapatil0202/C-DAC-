import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, geom_line, geom_col, geom_bar
data = pd.DataFrame({
    "x" : pd.Series([i for i in range(1, 11)]),
    "y" : pd.Series([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    'category': pd.Series(['a', 'a', 'a', 'b', 'b', 'b', 'a', 'b', 'a', 'b'])
})

def scatterplot():
    scatter_plot = (ggplot(data, aes(x = "x", y = "y", color = 'category')) + geom_point() + labs(title = 'Scatter Plot Example', x = 'X Axis', y = "Y Axis"))
    print(scatter_plot)

def lineplot():
    line_plot = (ggplot(data, aes(x = "x", y = "y", color = "category")) + geom_line() + labs(title = "line Plot Example", x = "X Axis", y = "Y Axis"))
    print(line_plot)

def bar():
    bar = (ggplot(data, aes(x = "category")) + geom_bar() + labs(title = "bar Plot Example", x = "X Axis", y = "Y Axis"))
    print(bar)

def bar2():
    bar_plot = (ggplot(data, aes(x="x", y="y", fill="category")) + geom_col() + labs(title="Bar Plot Example", x="X Axis", y="Y Axis"))
    print(bar_plot)

# scatterplot()
# lineplot()
bar()
# bar2()