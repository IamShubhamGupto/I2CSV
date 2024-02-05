import pandas as pd
import numpy as np
from faker import Faker
import argparse
import random
import matplotlib.pyplot as plt
import pickle
import os
import logging

logging.basicConfig(level=logging.INFO)

# Check if the directory exists
data_path = '../data'
if not os.path.exists(data_path):
    # If it does not exist, create it
    os.makedirs(data_path)
    os.makedirs(f'{data_path}/sheets')
    os.makedirs(f'{data_path}/pickles')
    logging.debug(f"Directory {data_path} was created.")

family_list = [ 'Comic Sans MS', 'SignPainter', 'Skia','Bradley Hand', 'Brush Script MT', 'Chalkduster']
weight_list = ['normal', 'bold', 'light']

# Initialize Faker to generate names
fake = Faker()

# Create the parser
parser = argparse.ArgumentParser(description='Generate synthetic data.')

parser.add_argument('--size', type=int, default=11, help='number of players per sheet')
parser.add_argument('--num_sheets', type=int, default=5, help='number of sheets to generate')

# Add arguments for mean and standard deviation
parser.add_argument('--mean_point', type=float, default=10, help='mean points value')
parser.add_argument('--stddev_point', type=float, default=3, help='standard deviation points value')

parser.add_argument('--mean_rebound', type=float, default=3, help='mean rebounds value')
parser.add_argument('--stddev_rebound', type=float, default=1, help='standard deviation rebound value')

parser.add_argument('--mean_assist', type=float, default=2, help='mean assists value')
parser.add_argument('--stddev_assist', type=float, default=0.6, help='standard deviation assists value')

parser.add_argument('--mean_steal', type=float, default=0.5, help='mean steal value')
parser.add_argument('--stddev_steal', type=float, default=0.1, help='standard deviation steal value')

parser.add_argument('--mean_block', type=float, default=0.5, help='mean blocks value')
parser.add_argument('--stddev_block', type=float, default=0.1, help='standard deviation blocks value')

parser.add_argument('--mean_turnover', type=float, default=0.5, help='mean blocks value')
parser.add_argument('--stddev_turnover', type=float, default=0.1, help='standard deviation blocks value')

parser.add_argument('--mean_foul', type=float, default=1, help='mean fouls value')
parser.add_argument('--stddev_foul', type=float, default=0.1, help='standard deviation blocks value')

if __name__ == '__main__':
    # Parse the arguments
    args = parser.parse_args()

    # Generate player names and jersey numbers, which will be constant across all sheets
    player_names = [fake.unique.first_name() for _ in range(args.size)]
    jersey_numbers = np.random.choice(range(1, 100), args.size, replace=False)

    # Create a list to hold all the sheets data
    all_sheets_data = []

    # Iterate over the number of sheets to generate the synthetic data
    for sheet in range(args.num_sheets):
        # Generate stats for each player using a normal distribution
        points = np.random.normal(args.mean_point, args.stddev_point, args.size)
        rebounds = np.random.normal(args.mean_rebound, args.stddev_rebound, args.size)
        assists = np.random.normal(args.mean_assist, args.stddev_assist, args.size)
        steals = np.random.normal(args.mean_steal, args.stddev_steal, args.size)
        blocks = np.random.normal(args.mean_block, args.stddev_block, args.size)
        turnovers = np.random.normal(args.mean_turnover, args.stddev_turnover, args.size)
        fouls = np.random.normal(args.mean_foul, args.stddev_foul, args.size)

        # Ensure non-negative values
        stats = [points, rebounds, assists, steals, blocks, turnovers, fouls]
        stats = [np.rint(np.abs(s)) for s in stats]

        # Create a DataFrame for the current sheet
        gt_sheet = {
            'Player': player_names,
            'Number': jersey_numbers,
            'Points': stats[0],
            'Rebounds': stats[1],
            'Assists': stats[2],
            'Steals': stats[3],
            'Blocks': stats[4],
            'Turnovers': stats[5],
            'Fouls': stats[6]
        }
        # Append the dataframe of the current sheet to the list
        all_sheets_data.append(gt_sheet)

        keys = list(gt_sheet.keys())
        random.shuffle(keys)

        df = pd.DataFrame(gt_sheet, columns=keys)
        # Create the totals row as a dictionary first
        totals_row = {key: 'Team Totals' if isinstance(gt_sheet[key][0], str) else sum(gt_sheet[key]) for key in keys}

        # Convert the totals_row to a DataFrame with matching columns order
        # Note: Wrapping totals_row in a list to ensure it's treated as a single row
        team_totals_df = pd.DataFrame([totals_row], columns=keys)

        # Assuming 'df' is your existing DataFrame created from 'gt_sheet' with shuffled columns
        # Append the team_totals_df to your existing DataFrame
        df = pd.concat([df, team_totals_df], ignore_index=True)

        # Create a figure and a plot
        fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size to match your actual data
        ax.axis('off')  # Hide the axes

        # Add a title with varying content and placement
        title = "Simple Basketball Stat Sheet"
        ax.set_title(title, fontdict={'fontsize': 14, 'fontweight': 'bold'}, loc='center')

        # Manually add each row of the table to allow unique styling
        table = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', colWidths=[0.1]*len(df.columns))

        table.auto_set_font_size(False)  # Disable automatic font size setting
        table.set_fontsize(12)  # Set a universal font size for all text in the table
        table.scale(1, 1.5)  # Adjust the scale for aesthetics

        # Customize the table cells
        for (i, j), cell in table.get_celld().items():
            if i == 0 or i == len(df):  # Header row or footer row
                cell.set_fontsize(10)
                cell.set_text_props(weight='bold')     
                cell.set_facecolor('#CCCCCC')  # Light grey color for footer
            else:
                fontsize = np.random.randint(8,10)
                weight = weight_list[np.random.randint(0, len(weight_list))]
                family = family_list[np.random.randint(0, len(family_list))]
                cell.set_text_props(fontsize=fontsize, weight=weight, family=family)
            if j == 0:  # First column
                cell.set_facecolor('#CCCCCC')  # Light grey color for the first column

        # Adjust layout
        plt.tight_layout()

        # Save the figure
        plt.savefig(f'../data/sheets/sheet_{sheet}_{args.size}_p{args.mean_point}_r{args.mean_rebound}_a{args.mean_assist}_s{args.mean_steal}_b{args.mean_block}_t{args.mean_turnover}_f{args.mean_foul}.png', dpi=300)
        plt.close()
        logging.debug(f"Sheet {sheet} was generated.")
    

    with open(f'../data/pickles/sheet_{args.size}_p{args.mean_point}_r{args.mean_rebound}_a{args.mean_assist}_s{args.mean_steal}_b{args.mean_block}_t{args.mean_turnover}_f{args.mean_foul}.pkl', 'wb') as f:
        pickle.dump(all_sheets_data, f)

    logging.debug(f"Data was saved to ../data/pickles/sheet_{args.size}_p{args.mean_point}_r{args.mean_rebound}_a{args.mean_assist}_s{args.mean_steal}_b{args.mean_block}_t{args.mean_turnover}_f{args.mean_foul}.pkl")

