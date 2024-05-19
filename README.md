# API Data Fetcher

This repository contains a Python script with a Tkinter-based GUI to fetch and display citation data from a specified API endpoint. The script retrieves paginated data from the API, processes the data to extract citation details, and displays the results in a scrollable text box within the GUI.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Functions](#functions)
- [License](#license)

## Prerequisites

Ensure you have Python 3.6 or higher installed. Additionally, the script requires the `requests` and `tkinter` libraries.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Adityaasati/Beyond_chats.git
   cd data_fetch
   ```

2. Install the required Python libraries:
   ```sh
   pip install requests
   ```

## Usage

To run the script, execute the following command:
```sh
python data_fetch.py
```

A GUI window will appear. Enter the API URL in the input field and click the "Fetch Data" button to retrieve and display the citation data.

## Code Overview

### Main Components

- **GUI**: Built using Tkinter, it contains an entry field for the API URL, a button to trigger the data fetch, and a scrollable text area to display the results.
- **Data Fetching**: The `fetch_data` function retrieves paginated data from the specified API URL and processes it to extract citation details.

## Functions

### `func_citation(values)`

Processes the data to extract citation IDs and links.

- **Parameters:**
  - `values` (list): A list of data entries from the API response.
  
- **Returns:**
  - `data_list` (list): A list of dictionaries containing citation IDs and links.

### `fetch_data()`

Fetches data from the API URL provided in the entry field, processes it, and displays the results in the scrollable text box.

- **Functionality:**
  - Retrieves the API URL from the entry field.
  - Makes a GET request to fetch the data.
  - Processes paginated responses to extract citation details.
  - Displays the extracted citation data in the scrollable text box.
  - Handles errors and displays appropriate error messages using message boxes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
