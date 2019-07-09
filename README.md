![Logo](https://github.com/libratom/ratom-logos/blob/master/basic_variations/RATOM_Vector_Logo_v1_300px.png)

# ratom-notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/libratom/ratom-notebooks/master)

**These example notebooks are in development.**

A selection of Jupyter notebooks to demonstrate features of [libratom](https://github.com/libratom/libratom) and other utilities developed for the RATOM project.

## Using ratom-notebooks (simple)

The simplest way to interact with these notebooks is via [**mybinder**](https://gke.mybinder.org/), which automatically builds an executable environment you can interact with from a web browser. The following link will generate an environment from this repository:

[https://mybinder.org/v2/gh/libratom/ratom-notebooks/master](https://mybinder.org/v2/gh/libratom/ratom-notebooks/master)

Sample data from the redacted Enron email corpus will be automatically downloaded when this instance is created. You can view the sample files in the RevisedEDRMv1\_Complete folder that appears in the **Files** tab of the Jupyter instance.

In the **binder** folder, you’ll find three Jupyter notebooks:

**pst\_walk.ipynb**, a simple example demonstrating walking a PST file using libpff to identify the number of messages present.

**entities.ipynb**, which identifies all of the entities present in every message body and commits them to a sqlite3 database. A simple widget displays sample entities identified as the PST files are being processed.

**entities\_multiprocessing.ipynb**, which performs the same task but spreads the work across as many cores as are available. Note: this is intended to be run on a local or dedicated hosted instance; running this notebook in mybinder may reduce performance.

## Using ratom-notebooks (advanced)

More coming soon...

## License(s)

Logos, documentation, and other non-software products of the RATOM team are distributed under the terms of Creative Commons 4.0 Attribution. Software items in RATOM repositories are distributed under the terms of the MIT License. See the LICENSE file for additional details.

## Development Team and Support

Product of the RATOM team. See [https://ratom.web.unc.edu](https://ratom.web.unc.edu/) for up to date information.


