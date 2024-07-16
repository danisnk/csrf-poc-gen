# CSRF PoC Generator

## Overview

The CSRF PoC Generator is a Python script designed to automate the creation of Proof of Concept (PoC) exploits for Cross-Site Request Forgery (CSRF) vulnerabilities in web applications. It includes both CLI and GUI versions for ease of use.

## Features

- **Automated PoC Generation:** Generates CSRF PoCs based on input parameters.
- **Command-Line Interface (CLI):** Simple CLI for easy execution.
- **Graphical User Interface (GUI):** Intuitive GUI for interactive use.
- **Customizable:** Supports various input file formats and HTTP protocols.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/csrf-poc-gen.git
    cd csrf-poc-gen
    ```

2. **Install dependencies:**

    Ensure Python 3.x and pip are installed. Then install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Interface (CLI)

Run the script using the CLI:

    python csrf-poc-generator-cli.py <filename> <protocol>
  

Example:

    python csrf-poc-generator-cli.py request.txt https

Replace `<filename>` with the path to your request file and `<protocol>` with the HTTP protocol (http or https).

### Graphical User Interface (GUI)

Launch the GUI version:

    python csrf-poc-generator-gui.py

Interact with the GUI to generate CSRF PoCs interactively.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
