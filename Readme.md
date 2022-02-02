# Hot News Api

## Built By [Cheruiyot Linus](https://github.com/Lenus254/)

## Description
This is a web application that displays a links to various news sources. On choosing a news source, it will preview the top news articles of the day.The application consumes news api.

You can view the site at:[Heroku](https://hotnews-api.herokuapp.com/)

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources
* Select the ones they prefer
* See the image,and description the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour                          | Input |                                                          Output |
|:-----------------------------------| :---------------: |----------------------------------------------------------------:|
| Display news sources               | **On page load** |                    List of various news sources is displayed in | **On Tab link click** | Clickable links to open news based on category |
| Display articles from a news source | **Click a news source** |              Redirected to a page with articles from the source |
| Display the preview of an article  | **On page load** |                     Each article displays an image,description  |
| To Read an entire article          | **Click an article** | Redirected to the news source's site to read the entire article |


## SetUp / Installation Requirements
### Prerequisites
* python3
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Lenus254/news_preview
        $ cd News_Preview

## Running the Application
* Creating the virtual environment

        $ python3.9 -m venv --without-pip myvirtual
        $ source myvirtual/bin/env
        

* Installing Flask and other Modules

        $ python3.9 -m pip install Flask
        $ python3.9 -m pip install Flask-Bootstrap
        $ python3.9 -m pip install Flask-Script

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3.9 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.9 manage.py tests

## Technologies Used
* Python3.9
* Flask

## License
MIT:
Copyright (c) 2022

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

