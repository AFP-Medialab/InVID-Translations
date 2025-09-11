# InVID-Translations

## Directory Overview

This directory contains the translation files for the InVID browser plugin. The translations are stored in Tab-Separated Value (`.tsv`) files. The directory is structured by the UI components of the plugin.

## Key Files

*   `components/`: This directory contains the `.tsv` files with the translations. The files are named after the UI component they belong to (e.g., `NavBar.tsv`, `FeedBack.tsv`).
*   `validation.py`: A Python script used to validate the translations. It checks if the translations are correctly served by a web service.
*   `README.md`: Provides a brief description of the project.

## Usage

The `.tsv` files are used to provide internationalization for the InVID plugin. Each file represents a specific UI component and contains the translation keys and their values for different languages.

The `validation.py` script can be used to ensure the integrity of the translations. It takes a branch and a service URL as arguments and checks if the translations for each component are available.

**Example of running the validation script:**

```bash
python validation.py --branch <branch_name> --url <service_url>
```
