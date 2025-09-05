"""A script to process book data."""
import pandas as pd
from sql import id_author_dict
import csv
import os
import argparse


import pandas as pd


def open_file_as_df(file_path: str):
    '''returns csv as a pandas dataframe'''
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError('file path or name is wrong')


def remove_columns(file):
    '''keep only necessary columns'''
    file = file[['book_title', 'author_id',
                'Year released', 'Rating', 'ratings']]
    return file


def remove_na(file):
    '''removes data with null entries'''
    file = file.dropna()
    return file


def change_type(file):
    '''convert the type of columns and cleans data'''
    file['year'] = file['year'].astype(int)
    file['rating'] = file['rating'].str.replace(',', '.').astype(float)
    file['title'] = file['title'].str.split('(').str[0]
    file['ratings'] = file['ratings'].str.split("`").str[1].astype(int)
    file['author_name'] = file['author_name'].astype(int)
    return file


def rename_column(file):
    '''correctly formats the column names'''
    file = file.rename(columns={'book_title': 'title',
                                'Year released': 'year', 'Rating': 'rating', 'author_id': 'author_name'})
    return file


def replace_author_id_name(file):
    '''links auothor if to author name'''
    file['author_name'] = file['author_name'].map(id_author_dict())
    return file


def save_file(file):
    '''saves the file'''
    file.to_csv(('PROCESSED_DATA.csv'))


def cli_argument():
    '''required arguement of file path'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='file path of csv')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli_argument()
    file = open_file_as_df(args.file)
    file = remove_columns(file)
    file = remove_na(file)
    file = rename_column(file)
    file = change_type(file)
    file = replace_author_id_name(file)
    save_file(file)
    print(file.sort_values(by='rating', ascending=False))
