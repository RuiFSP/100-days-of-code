import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()


def scrape_data():
    """
    This function launches the Chrome browser, navigates to a webpage, extracts
    data from a table, and saves it to a CSV file.
    """
    op = webdriver.ChromeOptions()
    op.add_experimental_option("detach", True)
    chrome_drive_path = Service(os.getenv('WEBDRIVER_PATH'))

    try:
        with webdriver.Chrome(service=chrome_drive_path, options=op) as driver:
            driver.maximize_window()
            driver.get("https://fbref.com/en/comps/32/Primeira-Liga-Stats#all_results2022-2023321")

            all_headers = driver.find_elements(By.XPATH, '//*[@id="results2022-2023321_overall"]/thead/tr/th')
            list_header_names = [header.text for header in all_headers[:-5]]

            # Exclude the first two header names ('', 'Rk')
            list_header_names = list_header_names[2:]

            rows = driver.find_elements(By.XPATH, '//*[@id="results2022-2023321_overall"]/tbody/tr')
            r = len(rows)

            # len method is used to get the size of that list
            c = len(list_header_names) + 1

            table = driver.find_element(By.ID, 'results2022-2023321_overall')
            data = []
            for row in table.find_elements(By.TAG_NAME, 'tr')[1:r]:
                cells = row.find_elements(By.TAG_NAME, 'td')[1:c]
                row_data = [cell.text for cell in cells]
                data.append(row_data)

            df = pd.DataFrame(data, columns=list_header_names)
            df.to_csv('data.csv', index=False)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


def plot_correlation():
    """
    Load the data from a CSV file, calculate the goal difference and the correlation coefficient, and plot the correlation.
    """
    # Load the data from the CSV file
    df = pd.read_csv('data.csv')

    # Calculate the goal difference (GF - GA)
    df['GD'] = df['GF'] - df['GA']

    # Calculate the correlation coefficient
    corr_coeff = np.corrcoef(df['GD'], df['Pts'])[0, 1]

    # Plot the correlation between the goal difference (GF - GA) and the total points (Pts)
    plt.scatter(df['GD'], df['Pts'])
    plt.xlabel('Goal Difference (GF - GA)')
    plt.ylabel('Total Points (Pts)')
    plt.title('Correlation between Goal Difference and Total Points')

    # Add trend line
    z = np.polyfit(df['GD'], df['Pts'], 1)
    p = np.poly1d(z)
    plt.plot(df['GD'], p(df['GD']), 'r--')

    # Add correlation value
    plt.text(0.05, 0.95, f"Correlation: {corr_coeff:.2f}", transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top')

    # Save the plot as a PNG file
    try:
        plt.savefig('correlation_plot.png')
        print('Plot saved successfully!')
    except Exception as e:
        print(f"An error occurred while saving the plot: {e}")

    plt.show()


if __name__ == '__main__':
    scrape_data()
    plot_correlation()
