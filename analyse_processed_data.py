"""A script to analyse book data."""
import altair as alt
import pandas as pd


def count_decades(file_as_pd: pd.DataFrame) -> pd.DataFrame:
    '''adds a decade column with the count '''

    file_as_pd['decade'] = (file_as_pd['year'] // 10) * 10
    decade_counts = data['decade'].value_counts().reset_index()
    return decade_counts


def pie_chart(decade_info: pd.DataFrame):
    '''creates a pie chart the decade and no. of entries'''
    pie_chart = alt.Chart(decade_info).mark_arc().encode(
        alt.Theta('count', type='quantitative'),
        alt.Color('decade', type='nominal')
    )

    pie_chart.save('decade_releases.png')


def top_authors(file_as_pd: pd.DataFrame) -> pd.DataFrame:
    '''gives top 10 authors by ratings'''
    author_ratings = file_as_pd.groupby(
        'author_name')['ratings'].sum().reset_index()

    author_ratings = author_ratings.sort_values(
        'ratings', ascending=False).head(10)
    return author_ratings


def bar_chart_authors(top_authors: pd.DataFrame):
    '''creates a bar chart of the top 10 authors and the summed rating'''
    top_authors_chart = alt.Chart(top_authors).mark_bar(color='skyblue',).encode(
        alt.X("author_name").sort('-y'),
        alt.Y("ratings"),
    )

    top_authors_chart.save('top_authors.png')
