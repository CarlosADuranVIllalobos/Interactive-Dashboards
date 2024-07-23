# Interactive Dashboards with Tableau

This repository demonstrates how to create and share interactive data visualizations using Tableau, providing insights into complex datasets. It includes data preprocessing, visualization creation, and dashboard integration.

## Table of Contents

- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Visualization](#visualization)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The datasets used in this project are:
1. **COVID-19 World Vaccination Progress**: Contains information on vaccination progress across various countries.
2. **COVID-19 World Testing Progress**: Contains information on COVID-19 testing across various countries.
3. **COVID-19 Variants Worldwide Evolution**: Contains information on the evolution of COVID-19 variants across various countries.

### Citation of the Datasets

- Preda, Gabriel. (2021). COVID-19 World Vaccination Progress. Kaggle. https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress.
- Rajkumar, Sudalai. (2021). COVID-19 in India. Kaggle. https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india.
- Preda, Gabriel. (2021). COVID-19 Variants. Kaggle. https://www.kaggle.com/datasets/gpreda/covid19-variants.

## Project Structure

```plaintext
Interactive_Dashboards_Tableau/
├── data/
│   ├── cleaned_covid_combined_data.csv  # Combined cleaned dataset
├── notebooks/
│   ├── data_preprocessing.ipynb         # Data preprocessing and merging
├── tableau/
│   ├── dashboard.twb                    # Tableau workbook
├── README.md                            # Project README

## Usage

1. **Data Preprocessing**:
   - Execute the `data_preprocessing.ipynb` notebook to clean and preprocess the data.
   - [Data Preprocessing Notebook](notebooks/data_preprocessing.ipynb)

2. **Tableau Visualization**:
   - Open Tableau Desktop or Tableau Public.
   - Import the cleaned dataset (`cleaned_covid_data.csv`).
   - Create interactive visualizations and dashboards.
   - Save the Tableau workbook (`dashboard.twb`).

3. **Embed Dashboard**:
   - Publish your Tableau dashboard to Tableau Public.
   - Embed the Tableau Public dashboard in your Jupyter Notebook or web application using an iframe.

## Visualization

The project explores various interactive visualizations, including:

- **World Map**: Total confirmed cases by country.
- **Time Series Chart**: Trend of confirmed cases over time.
- **Bar Chart**: Vaccination progress by country.

The visualizations are created using Tableau's powerful data visualization tools.

## Results

### Interactive Dashboards

You can view the interactive dashboards created with Tableau [here](https://public.tableau.com/views/YOUR_DASHBOARD_URL).

### Data Insights

The visualizations provide insights into:

- The geographical distribution of COVID-19 cases.
- The temporal trend of vaccinations.
- Comparative analysis of vaccination progress among countries.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any feature requests or improvements.

## License

This project is licensed under the MIT License.

If you use this repository in your research, please cite it as shown in the right sidebar.

