# Flask URL Shortener

Simple URL shortener application built using Python's `Flask` framework. The application generates a short URL for a
given long URL and stores the mapping between the short URL and the original URL in a `JSON` file. Users can access the
original URL by visiting the short URL.

## Live Demo

Check out the live version of this project: [URL Shortener](https://url-shortener-tau-ivory.vercel.app/)

## Features

- Shortens long URLs and generates a random string as the shortened URL.
- Stores the short URL and long URL mappings in a JSON file (`urls.json`).
- Redirects users from the short URL to the original long URL.
- Prevents duplicate shortened URLs for the same long URL.
- Simple front-end interface to input URLs.

