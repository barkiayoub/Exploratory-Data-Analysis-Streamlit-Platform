# Exploratory Data Analysis App

The Exploratory Data Analysis (EDA) App is a Streamlit-based web application that allows users to perform comprehensive exploratory data analysis on their datasets. It provides an intuitive and user-friendly interface for uploading CSV files, visualizing the input data, and generating an interactive profiling report.

## About

This project simplifies the process of exploratory data analysis. Leveraging the power of [Streamlit](https://streamlit.io) for interactive web interfaces and [ydata_profiling](https://github.com/ydata-ai/ydata-profiling) for generating detailed profiling reports, the app enables quick insights into your data—all in one place. 

## Demo

Below is a GIF demonstrating how to use the app:

![App Demo](Demo\EDA-App-Demo.webm)

*Replace "path/to/your-demo.gif" with the actual path or URL to your GIF.*

## Features

- **CSV File Upload**: Easily upload your dataset in CSV format.
- **Data Preview**: View your dataset in a neat table format.
- **Interactive Profiling Report**: Automatically generate a comprehensive EDA report with insights and visualizations.
- **Example Dataset**: If no CSV is uploaded, the app can generate and analyze a random example dataset.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/barkiayoub/Exploratory-Data-Analysis-Streamlit-Platform.git
   cd Exploratory-Data-Analysis-Streamlit-Platform
   ```

2. **Install the Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the EDA App:

1. **Start the App with Streamlit**
   ```bash
   streamlit run eda_app.py
   ```

2. **Interact with the Application**
   - Use the sidebar to upload your CSV file.
   - The main page will display a preview of the dataset.
   - An interactive profiling report will be generated below the data preview.
   - If no file is uploaded, click on "Press to use Example Dataset" in the sidebar to analyze a randomly generated dataset.

<!-- ## Demo

Below is a GIF demonstrating how to use the app:

![App Demo](path/to/your-demo.gif)

*Replace "path/to/your-demo.gif" with the actual path or URL to your GIF.*

## Screenshots

Add a screenshot of the application (for example, the provided `data.jpg`) to showcase the UI:

![App Screenshot](data.jpg) -->

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, please reach out via:

- **GitHub**: [barkiayoub](https://github.com/barkiayoub)

Happy Analyzing!