# biospaCy

A Python Natural Language Processing package for labeling Entities in data. 

Built on spaCy.

Install package with:  

        pip3 install git+https://git@github.com/foscraft/biospaCy

The working.

        import biospacy

To produce text labels from a data set use:

        biospacy.text_labels ('path/to/your/dataset.csv', 'model_to_use','name_of_your_choice_for_the_dataset_output')

To get information about the package:

       biospacy.info()

To check Version:

        biospacy.version()


This package is under active development and will be available in Pypi in a few months.
