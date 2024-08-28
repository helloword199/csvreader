## CSV Reader

This Python script allows users to select and view data from different CSV files interactively.

### Features
- **Interactive Menu**: Choose from `cars.csv`, `animals.csv`, `cakes.csv`, or exit.
- **File Operations**: View file info, first two rows, or last two rows.
- **Navigation**: Continue with the file or return to the menu after each operation.

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **CSV Files**: The following CSV files should be available in your project directory:
  - `cars.csv`
  - `animals.csv`
  - `cakes.csv`

### Installation

#### Prerequisites
- **Python 3.x**: Make sure Python is installed on your machine.
- **Pip**: Ensure pip, Python's package installer, is available.

#### Setting Up the Project

1. **Clone the Repository**:

    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2. **Create a Virtual Environment (Optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    After setting up your virtual environment, install the required packages using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    This command reads the `requirements.txt` file and installs all the necessary libraries for the project.

4. **Run the Script**:

    Start the application:

    ```bash
    python your_script_name.py
    ```

### Creating `requirements.txt`

If you add new packages, update the `requirements.txt` file:

```bash
pip freeze > requirements.txt
