# 6. Explore distributions of values

It can be useful to understand the range of values, and the distribution of those values, for the numerical columns in
your data.

## Histograms

Histograms are 'designed to show a dataset's distribution or
spread' [Reference: Depict, Chart chooser](https://depictdatastudio.com/charts/histograms/).

Create [histograms](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html#pandas.DataFrame.plot.hist)
to show the distribution of the 'participants_m' and 'participants_f' columns.

The histogram function has the following options `DataFrame.plot.hist(by=None, bins=10, **kwargs)`.

### Activity: Create histograms

You can either add the code to one of your existing functions, or create a new one.

1. Add import to the top of the module: `import matplotlib.pyplot as plt`.
2. Add code to a function to create a histogram from the data:

    ```python
    #Create a histogram of the DataFrame
    df.hist()

    # Show the plot
    plt.show() 
    ```
3. Run the code to generate the figure. It should generate a figure that has histograms for all the columns in the
   data.
4. Modify the code to use only specified columns `columns = ["participants_m", "participants_f"]` of the DataFrame e.g.
   `df[columns].hist()`
5. Run the code again to generate the figure.

The distributions don't really tell you much in this dataset. It may be more useful for larger datasets.

## Boxplot

### Identifying outliers

An outlier is a data point that significantly differs from the other observations in a dataset. It lies outside the
overall pattern of distribution and can be unusually high or low compared to the rest of the data. Outliers can result
from variability in the data, measurement errors, or experimental errors.

You can identify outliers using different techniques:

- Plot the data (e.g., histogram, scatter plot, boxplot)
- Use common sense
- Use statistical tests

In statistical terms, outliers are often defined as values that fall below the first quartile (Q1) minus 1.5 times the
interquartile range (IQR) or above the third quartile (Q3) plus 1.5 times the IQR. Mathematically, this can be expressed
as:

```text
Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Where:

- (Q1) is the first quartile (25th percentile)
- (Q3) is the third quartile (75th percentile)
- (IQR) is the interquartile range, calculated as (Q3 - Q1)

Values outside these bounds are considered outliers.

Since this course doesn't expect any knowledge of, nor teach, statistics then we will check for outliers by creating a
chart or 'plot'.

In this activity, you will
create [pandas boxplots](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.boxplot.html).

"A Box and Whisker Plot (or Box Plot) is a convenient way of visually displaying the data distribution through their
quartiles. The lines extending parallel from the boxes are known as the 'whiskers', which are used to indicate
variability outside the upper and lower quartiles. Outliers are sometimes plotted as individual dots that are in-line
with whiskers. Box plots can be drawn either vertically or
horizontally." [Source: Data Visualisation Catalogue](https://datavizcatalogue.com/methods/box_plot.html)

Box plots have a box from lower quartile to the upper quartile, with the median marked. 25% of the population is below
first quartile, 75% of the population is below third quartile.

![boxplot](../img/box_plot.png)

Source: [statinfer](https://statinfer.com/104-3-5-box-plots-and-outlier-dectection-using-python/)

Box plots can help to get an idea of the data distribution which in turn helps us to identify the outliers more
easily.

If the box is pushed to one side, and some values are far away from the box, then it is an indication of outliers.

The following code shows a basic example of creating a boxplot. Numpy is only used in this example to generate the
random numbers.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
df.boxplot()
df.plot.box()  # This syntax is also valid
plt.show()
```

### Activity: Create box plots

1. Add code to generate a box plot from the paralympics csv dataframe.

   Refer to
   the [pandas boxplot docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.boxplot.html).

2. Run the code and view the plots. Notice that it plots all the variables on the same scale.
3. Modify the code to see the sports variable in its own plot; or try to create subplots for each variable.

There are no outliers, however if you repeat this step again later after creating a new column for duration, you may
spot an outlier.

[Next activity](2-07-plot-timeseries.md)